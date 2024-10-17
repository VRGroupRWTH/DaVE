import { Backend } from "./backend.js";
import { Database } from "./database.js";
import { log_page } from "./log.js";
import express from "express";

function parse_string(name, fallback)
{
    const index = process.argv.indexOf("--" + name);

    if(index != -1 && (index + 1) < process.argv.length)
    {
        return process.argv[index + 1];
    }

    return fallback;
}

function parse_number(name, fallback)
{
    let string = parse_string(name, null);

    if(string)
    {
        return parseInt(string);
    }

    return fallback;
}

function parse_flag(name)
{
    const index = process.argv.indexOf("--" + name);

    return (index != -1)
}

const website_path = parse_string("website", null);
const database_path = parse_string("database", "../database/");
const port = parse_number("port", "8080");

const app = express();
app.use(express.json());
app.use("/database", express.static(database_path));

const database = new Database();
database.load(database_path);

const backend = new Backend();
backend.setup(app, database);

if(website_path)
{
    app.use("/", (request, response, next) => 
    {
        log_page(request, database);
        
        next();
    });
    
    app.use("/", express.static(website_path));

    app.get("/*", (request, response) => 
    {
        response.sendFile(process.cwd() + "/" + website_path + "index.html");
    });
}

app.listen(port, () =>
{
    console.log("Listening on port " + port);
});