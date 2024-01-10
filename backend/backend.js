const {Database, Sorting} = require("./database.js");
const Tag = require("./tag.js");
const AdmZip = require("adm-zip");
const fs = require("fs");

class Backend
{
    #database

    constructor()
    {
        this.#database = new Database();
    }

    setup(app)
    {
        this.#database.load("database/");

        app.post("/api/fetch_visualization", async (request, response) => this.#on_fetch_visualization_request(request, response));
        app.post("/api/search_visualizations", async (request, response) => this.#on_search_visualizations_request(request, response));
        app.post("/api/search_property", async (request, response) => this.#on_search_property_request(request, response));
        app.get("/api/create_script", async (request, response) => this.#on_create_script(request, response));
    }

    async #on_fetch_visualization_request(request, response)
    {
        const visualization_name = request.body.visualization_name;
        const visualization = this.#database.get_visualization(visualization_name);

        if(visualization != null)
        {
            response.send(visualization.export());
        }

        else
        {
            response.sendStatus(404);
        }
    }

    async #on_search_visualizations_request(request, response)
    {
        const query = request.body.query;
        let sorting = Sorting.score_descending;
        let filter_date_begin = null;
        let filter_date_end = null;
        let filter_tags = [];

        if("sorting" in request.body)
        {
            sorting = Sorting.import(request.body.sorting);
        }

        if("filter_date_begin" in request.body)
        {
            filter_date_begin = new Date(request.body.filter_date_begin);
        }

        if("filter_date_end" in request.body)
        {
            filter_date_end = new Date(request.body.filter_date_end);
        }

        if("filter_tags" in request.body)
        {
            filter_tags = Tag.import(request.body.filter_tags);
        }

        const visualizations = this.#database.search_visualizations(query, sorting, (visualization) =>
        {
            const date = new Date(visualization.get_date());

            if(filter_date_begin != null)
            {
                if(date < filter_date_begin)
                {
                    return false;
                }
            }

            if(filter_date_end != null)
            {
                if(date > filter_date_end)
                {
                    return false;
                }
            }

            for(const filter_tag of filter_tags)
            {
                if(!visualization.get_tags().some(tag => tag.is_equal(filter_tag)))
                {
                    return false;
                }
            }

            return true;
        });

        let result = [];

        for(const visualization of visualizations)
        {
            result.push(visualization.export());
        }

        response.send(result);
    }

    #on_search_property_request(request, response)
    {
        const query = request.body.query;
        const query_property = request.body.query_property;
        let output_properties = [request.body.query_property];
        let filter_all_visualizations = false;
        let filter_all_tags = false;

        if("output_properties" in request.body)
        {
            output_properties = request.body.output_properties;
        }

        if("filter_all_visualizations" in request.body)
        {
            filter_all_visualizations = request.body.filter_all_visualizations;
        }

        if("filter_all_tags" in request.body)
        {
            filter_all_tags = request.body.filter_all_tags;
        }

        const result = this.#database.search_property(query, query_property, output_properties, (visualization, tag) =>
        {
            if(tag != null)
            {
                if(filter_all_tags)
                {
                    return false;
                }
            }

            else if(visualization != null)
            {
                if(filter_all_visualizations)
                {
                    return false;
                }
            }

            return true;
        });

        response.send(result);
    }

    async #on_create_script(request, response)
    {
        const required_parameters = 
        [
            "visualization",
            "technique",
            "command"
        ];

        for(const parameter of required_parameters)
        {
            if(!(parameter in request.query))
            {
                response.sendStatus(400);

                return;
            }
        }

        const visualization = this.#database.get_visualization(request.query.visualization);

        if(visualization == null)
        {
            response.sendStatus(404);

            return;
        }

        const templates = visualization.get_templates();
        const technique = request.query.technique;
        let template = null;
        let command = null;

        for(const template_item of templates)
        {
            if(!template_item.techniques.some(technique_item => technique_item == technique))
            {
                continue;
            }

            for(const command_item of template_item.commands)
            {
                if(command_item.type == request.query.command)
                {
                    command = command_item;
                    template = template_item;

                    break;
                }
            }

            if(command != null || template != null)
            {
                break;
            }
        }

        if(template == null || command == null)
        {
            response.sendStatus(404);

            return;
        }

        let container_path = "";
        let container_files = [];

        if("path" in template.container)
        {
            const file = 
            {
                path: this.#get_file_name(template.container.path),
                buffer: fs.readFileSync(template.container.path)
            }

            container_path = file.path;
            container_files.push(file);
        }

        else if("url" in template.container)
        {
            container_path = template.container.url;
        }

        else
        {
            response.sendStatus(404);

            return;
        }

        let dataset_path = "";
        let dataset_files = [];

        if("dataset" in request.query)
        {
            dataset_path = request.query.dataset;
        }

        else
        {
            const dataset = visualization.get_dataset();

            if("path" in dataset)
            {
                const paths = this.#find_matching_files(dataset.path);

                for(const path of paths)
                {
                    const file =
                    {
                        path: "dataset/" + this.#get_file_name(path),
                        buffer: fs.readFileSync(path)
                    };

                    dataset_files.push(file);
                }

                if(paths.length > 1)
                {
                    dataset_path = "dataset/";
                }

                else if(paths.length > 0)
                {
                    dataset_path = "dataset/" + this.#get_file_name(paths[0]);
                }
            }

            else if("url" in dataset)
            {
                const dataset_request =
                {
                    method: "GET"
                };

                const dataset_response = await fetch(dataset.url, dataset_request);

                if(dataset_response.ok)
                {
                    const file = 
                    {
                        path: "dataset/" + this.#get_file_name(dataset.url),
                        buffer: Buffer.from(await dataset_response.arrayBuffer()),
                    };

                    dataset_path = file.path;
                    dataset_files.push(file);
                }
            }
        }

        let constants =
        [
            "CONTAINER=" + container_path,
            "DATASET=" + dataset_path,
            "TECHNIQUE=" + technique,
            "COMMAND=" + command.run,
            "COMMAND_TYPE=" + command.type
        ];

        const trace_file = fs.readFileSync(template.trace).toString();
        const script_file = fs.readFileSync(template.script).toString();
        const script_lines = script_file.split("\n");

        let script_compiled = script_lines[0] + "\n";

        for(const constant of constants)
        {
            script_compiled += constant + "\n";
        }

        for(let index = 1; index < script_lines.length; index++)
        {
            script_compiled += script_lines[index];

            if(index < script_lines.length - 1)
            {
                script_compiled += "\n";
            }
        }

        const trace_file_name = this.#get_file_name(template.trace);
        const script_file_name = this.#get_file_name(template.script);

        let archive = new AdmZip();
        archive.addFile(trace_file_name, Buffer.from(trace_file));
        archive.addFile(script_file_name, Buffer.from(script_compiled));

        for(const file of container_files)
        {
            archive.addFile(file.path, file.buffer);
        }

        for(const file of dataset_files)
        {
            archive.addFile(file.path, file.buffer);
        }

        response.send(archive.toBuffer());
    }

    #find_matching_files(file_query)
    {
        let paths = [];
        let path_stack = [];

        

        

        return path;
    }

    #get_file_name(file_path)
    {
        const offset = file_path.lastIndexOf("/");

        if(offset == -1)
        {
            return file_path;
        }

        return file_path.substr(offset + 1);
    }
}

module.exports = Backend;