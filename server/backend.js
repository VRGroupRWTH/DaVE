import { request } from "https";
import { Database, Sorting } from "./database.js"
import { Tag } from "./tag.js"
import adm_zip from "adm-zip";
import fs from "fs";

export class Backend
{
    #database

    constructor()
    {
        this.#database = new Database();
    }

    setup(app, database_path)
    {
        this.#database.load(database_path);

        app.post("/api/fetch_visualization", async (request, response) => this.#on_fetch_visualization_request(request, response));
        app.post("/api/search_visualizations", async (request, response) => this.#on_search_visualizations_request(request, response));
        app.post("/api/search_property", async (request, response) => this.#on_search_property_request(request, response));
        app.post("/api/search_author", async (request, response) => this.#on_search_author_request(request, response))
        app.get("/api/create_script", async (request, response) => this.#on_create_script(request, response));
        app.get("/api/download_resources", async (request, response) => this.#on_download_resources(request, response));
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
        let sorting = Sorting.name_descending;
        let filter_date_begin = null;
        let filter_date_end = null;
        let filter_tags = [];
        let filter_authors = [];
        let filter_check_container_docker = false;
        let filter_check_container_singularity = false;
        let filter_check_execution_local = false;
        let filter_check_execution_mpi = false;
        let filter_check_execution_slurm = false;
        let filter_check_other_preview = false;

        if("sorting" in request.body)
        {
            sorting = Sorting.select(query, request.body.sorting);
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

        if("filter_authors" in request.body)
        {
            filter_authors = request.body.filter_authors;
        }

        if("filter_check_container_docker" in request.body)
        {
            filter_check_container_docker = request.body.filter_check_container_docker;
        }

        if("filter_check_container_singularity" in request.body)
        {
            filter_check_container_singularity = request.body.filter_check_container_singularity;
        }

        if("filter_check_execution_local" in request.body)
        {
            filter_check_execution_local = request.body.filter_check_execution_local;
        }

        if("filter_check_execution_mpi" in request.body)
        {
            filter_check_execution_mpi = request.body.filter_check_execution_mpi;
        }

        if("filter_check_execution_slurm" in request.body)
        {
            filter_check_execution_slurm = request.body.filter_check_execution_slurm;
        }

        if("filter_check_other_preview" in request.body)
        {
            filter_check_other_preview = request.body.filter_check_other_preview;
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

            for(const filter_author of filter_authors)
            {
                if(!visualization.get_authors().some(author => author.name == filter_author))
                {
                    return false;
                }
            }

            if(filter_check_container_docker)
            {
                if(!visualization.supports_docker())
                {
                    return false;
                }
            }

            if(filter_check_container_singularity)
            {
                if(!visualization.supports_singularity())
                {
                    return false;
                }
            }

            if(filter_check_execution_local)
            {
                if(!visualization.supports_local())
                {
                    return false;
                }
            }

            if(filter_check_execution_mpi)
            {
                if(!visualization.supports_mpi())
                {
                    return false;
                }
            }

            if(filter_check_execution_slurm)
            {
                if(!visualization.supports_slurm())
                {
                    return false;
                }
            }

            if(filter_check_other_preview)
            {
                if(visualization.get_scene() == null || visualization.get_scene() == "")
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

    async #on_search_author_request(request, response)
    {
        const query = request.body.query;

        const result = this.#database.search_author(query);
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

        let files = [];
        let constants = 
        [
            "CONTAINER_PLATFORM='" + technique + "'",
            "COMMAND='" + command.run + "'",
            "EXEC_TYPE='" + command.type + "'"
        ];

        this.#build_container_file(files, constants, template.container);
        this.#build_dataset_files(files, constants, request.query, visualization);
        this.#build_trace_file(files, constants, template.trace);
        this.#build_script_file(files, constants, template.script);

        let archive = new adm_zip();

        for(const file of files)
        {
            archive.addFile(file.path, file.buffer);

            if(file.path.endsWith(".zip"))
            {
                let entry = archive.getEntry(file.path);
                entry.header.method = 0; // Store uncompressed since data is already compressed
            }
        }

        response.send(archive.toBuffer());
    }

    async #on_download_resources(request, response)
    {
        if(!("visualization" in request.query))
        {
            response.sendStatus(400);

            return;
        }
        
        const visualization = this.#database.get_visualization(request.query.visualization);

        if(visualization == null)
        {
            response.sendStatus(404);

            return;
        }

        if(!("resources" in request.query))
        {
            response.sendStatus(400);

            return;
        }

        const resources = visualization.get_resources();
        const resource_indices = request.query.resources.split("+");
        let archive = new adm_zip();

        for(const resource_index of resource_indices)
        {
            if(resource_index >= resources.length)
            {
                response.sendStatus(400);

                return;
            }

            const resource = resources[resource_index];
            const file_name = resource.name;
            let file_buffer = []

            if("path" in resource)
            {
                file_buffer = fs.readFileSync(resource.path);
            }

            else
            {
                response.sendStatus(500);

                return;
            }

            archive.addFile(file_name, file_buffer);

            if(file_name.endsWith(".zip"))
            {
                let entry = archive.getEntry(file_name);
                entry.header.method = 0; // Store uncompressed since data is already compressed
            }
        }

        response.send(archive.toBuffer());
    }

    #build_container_file(files, constants, container)
    {
        if("path" in container)
        {
            const constant = "CONTAINER_URL='" + this.#get_file_name(container.path) + "'";
            constants.push(constant);

            const file = 
            {
                path: this.#get_file_name(container.path),
                buffer: fs.readFileSync(container.path)
            };

            files.push(file);
        }

        else if("url" in container)
        {
            const constant = "CONTAINER_URL='" + container.url + "'";
            constants.push(constant)
        }
    }

    #build_dataset_files(files, constants, query, visualization)
    {
        if("datasets" in query)
        {
            const datasets = query.datasets.split("+");

            for(let index = 0; index < datasets.length; index += 2)
            {
                const dataset_identifier = datasets[index];
                const dataset_path = datasets[index + 1];

                const constant = dataset_identifier.toUpperCase() + "_PATH='" + dataset_path + "'";
                constants.push(constant);
            }
        }

        else
        {
            const datasets = visualization.get_datasets();

            for(const dataset of datasets)
            {
                if("path" in dataset)
                {
                    const constant = dataset.identifier.toUpperCase() + "_PATH='data/" + this.#get_file_name(dataset.path) + "'";
                    constants.push(constant);

                    for(const file_name of this.#get_matching_files(dataset.path))
                    {
                        const file = 
                        {
                            path: "data/" + this.#get_file_name(file_name),
                            buffer: fs.readFileSync(file_name)
                        };

                        files.push(file);
                    }
                }
                
                else if("url" in dataset)
                {
                    const constant = dataset.identifier.toUpperCase() + "_URL='" + dataset.url + "'";
                    constants.push(constant);
                }
            }
        }
    }

    #build_trace_file(files, constants, trace)
    {
        const constant = "TRACE='" + this.#get_file_name(trace) + "'";
        constants.push(constant);

        const file = 
        {
            path: this.#get_file_name(trace),
            buffer: fs.readFileSync(trace)
        };

        files.push(file);
    }

    #build_script_file(files, constants, script)
    {
        const script_file = fs.readFileSync(script).toString();
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

        const file = 
        {
            path: this.#get_file_name(script),
            buffer: Buffer.from(script_compiled)
        };

        files.push(file);
    }

    #get_matching_files(query)
    {
        const offset = query.lastIndexOf("/");
        let query_path = "";
        let query_expression = "^" + query + "$";

        if(offset != -1)
        {
            query_path = query.substr(0, offset + 1);
            query_expression = ("^" + query.substr(offset + 1) + "$").replaceAll("*", ".*");
        }

        let files = [];

        for(const file of fs.readdirSync(query_path))
        {
            const file_stats = fs.lstatSync(query_path + file);

            if(!file_stats.isFile())
            {
                continue;
            }

            if(file.match(query_expression) == null)
            {
                continue;
            }

            files.push(query_path + file);
        }

        return files;
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