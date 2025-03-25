import fs from "fs";
import yaml from "yaml";
import path from "path";

const LOG_FILE_NAME = "./log/log.yaml";
const LOG_PAGES = 
[
    "/",
    "/home",
    "/guide",
    "/guide_use_dave",
    "/guide_extend_dave",
    "/about",
    "/browser",
    "/visualization",
    "/imprint",
    "/privacy_policy"
];

export const LogCategory =
{
    Page: "page",
    Visualization: "visualization",
    Resource: "resource",
    Script: "script"
};

function read_log_file()
{
    const directory = path.dirname(LOG_FILE_NAME);

    if(!fs.existsSync(directory))
    {
        fs.mkdirSync(directory)
    }

    if(!fs.existsSync(LOG_FILE_NAME))
    {
        return {};
    }

    let file = "";

    try 
    {
        file = fs.readFileSync(LOG_FILE_NAME).toString();
    }

    catch(exception)
    {
        console.log("Can't read log file '" + LOG_FILE_NAME + "'");

        return {};
    }

    try
    {
        return yaml.parse(file);
    }

    catch(exception)
    {
        console.log("Can't parse log file '" + LOG_FILE_NAME + "'");
    }

    return {};
}

function write_log_file(log)
{
    const directory = path.dirname(LOG_FILE_NAME);

    if(!fs.existsSync(directory))
    {
        fs.mkdirSync(directory)
    }

    let file = "";

    try
    {
        file = yaml.stringify(log);
    }

    catch(exception)
    {
        console.log("Can't stringify log file");

        return;
    }

    if(fs.existsSync(LOG_FILE_NAME + ".backup"))
    {
        try
        {
            fs.rmSync(LOG_FILE_NAME + ".backup");
        }
        
        catch(exception)
        {
            console.log("Can't remove backup log file '" + LOG_FILE_NAME + ".backup'");

            return;
        }
    }

    if(fs.existsSync(LOG_FILE_NAME))
    {
        try
        {
            fs.renameSync(LOG_FILE_NAME, LOG_FILE_NAME + ".backup");
        }

        catch(exception)
        {
            console.log("Can't rename to backup log file '" + LOG_FILE_NAME + ".backup'");

            return;
        }
    }

    try 
    {
        fs.writeFileSync(LOG_FILE_NAME, file, { flag: "w" });
    }

    catch(exception)
    {
        console.log("Can't write log file '" + LOG_FILE_NAME + "'");

        return;
    }
}

export function log_access(category, name)
{
    let log = read_log_file();

    if(!(category in log))
    {
        log[category] = {};
    }

    if(!(name in log[category]))
    {
        log[category][name] = 1;
    }

    else
    {
        let current = log[category][name];

        if(typeof current != "number")
        {
            console.log("Logged access count is not a number. Resetting access count to zero");

            current = 0;
        }

        log[category][name] = current + 1;
    }

    write_log_file(log);    
}

export function log_page(request, database)
{
    if(LOG_PAGES.indexOf(request.path) < 0)
    {
        return;
    }

    log_access(LogCategory.Page, request.path);

    if(request.path == "/visualization")
    {
        const url = request.originalUrl;
        const search = url.substr(url.indexOf("?"));
        const parameters = new URLSearchParams(search);

        const visualization_name = parameters.get("name");
        const visualization = database.get_visualization(visualization_name);

        if(visualization != null)
        {
            log_access(LogCategory.Visualization, "/" + visualization.get_path());
        }
    }
}