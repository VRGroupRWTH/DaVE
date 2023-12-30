const {Database, Sorting} = require("./database.js");
const Tag = require("./tag.js");
const AdmZip = require("adm-zip");

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

        app.post("/api/fetch_technique", async (request, response) => this.#on_fetch_technique_request(request, response));
        app.post("/api/search_techniques", async (request, response) => this.#on_search_technqiues_request(request, response));
        app.post("/api/search_property", async (request, response) => this.#on_search_property_request(request, response));
        app.get("/api/create_script", async (request, response) => this.#on_create_script(request, response));
    }

    async #on_fetch_technique_request(request, response)
    {
        const technique_name = request.body.technique_name;
        const technique = this.#database.get_technique(technique_name);

        if(technique != null)
        {
            response.send(technique.export());
        }

        else
        {
            response.sendStatus(404);
        }
    }

    async #on_search_technqiues_request(request, response)
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

        const techniques = this.#database.search_techniques(query, sorting, (technique) =>
        {
            const date = new Date(technique.get_date());

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
                if(!technique.get_tags().some(tag => tag.is_equal(filter_tag)))
                {
                    return false;
                }
            }

            return true;
        });

        let result = [];

        for(const technique of techniques)
        {
            result.push(technique.export());
        }

        response.send(result);
    }

    #on_search_property_request(request, response)
    {
        const query = request.body.query;
        const query_property = request.body.query_property;
        let output_properties = [request.body.query_property];
        let filter_all_techniques = false;
        let filter_all_tags = false;

        if("output_properties" in request.body)
        {
            output_properties = request.body.output_properties;
        }

        if("filter_all_techniques" in request.body)
        {
            filter_all_techniques = request.body.filter_all_techniques;
        }

        if("filter_all_tags" in request.body)
        {
            filter_all_tags = request.body.filter_all_tags;
        }

        const result = this.#database.search_property(query, query_property, output_properties, (technique, tag) =>
        {
            if(tag != null)
            {
                if(filter_all_tags)
                {
                    return false;
                }
            }

            else if(technique != null)
            {
                if(filter_all_techniques)
                {
                    return false;
                }
            }

            return true;
        });

        response.send(result);
    }

    #on_create_script(request, response)
    {
        const required_parameters = 
        [
            "technique_name",
            "technique_container",
            
        ];

        if(!("technique_name" in request.query))
        {
            response.sendStatus(400);

            return;
        }

        if(!("template_index" in request.query))
        {
            response.sendStatus(400);

            return;
        }

        if(!("command_type" in request.query))
        {
            response.sendStatus(400);

            return;
        }

        const technique_name = request.query.technique_name;
        const technique_container = request.query.technique_container;
        const template_index = parseInt(request.query.template_index);
        const command_type = request.query.command_type;

        let dataset_path = "./dataset/";
        let dataset_included = true;

        if("dataset_path" in request.query)
        {
            dataset_path = request.query.dataset_path;
        }

        if("dataset_included" in request.query)
        {
            dataset_included = request.query.dataset_included;
        }

        const technique = this.#database.get_technique(technique_name);
        
        if(technique == null)
        {
            response.sendStatus(404);

            return;
        }

        const templates = technique.get_templates(); 

        if(template_index == NaN)
        {
            response.sendStatus(400);

            return;
        }

        if(template_index < 0 || template_index >= templates.length)
        {
            response.sendStatus(404);

            return;
        }

        const template = templates[template_index];
        let command = null;

        for(const item of template.commands)
        {
            if(item.type == command_type)
            {
                command = item;

                break;
            }
        }

        if(command == null)
        {
            response.sendStatus(404);

            return;
        }

        let constants = "";
        constants += "TECHNIQUE=" + technique_container + "\n";
        constants += "COMMAND_TYPE=" + command.type + "\n";
        constants += "COMMAND=" + command.run + "\n";
        constants += "DATASET=" + dataset_path + "\n";

        if("path" in template.container)
        {
            constants += "CONTAINER=" + template.container.path + "\n";
        }

        else if("url" in )
        {
            constants += "CONTAINER=" + template.container.path + "\n";
        }


        const trace_file = fs.readFileSync(template.trace).toString();
        const script_file = fs.readFileSync(template.script).toString();


        //TECHNIQUE=
        //COMMAND_TYPE
        //COMMAND
        //CONTAINER
        //DATASET



        //TODO: Alter script file and add constants
        //TODO: Load dataset if included


        let archive = new AdmZip();
        archive.addLocalFile("/home/me/some_picture.png");





        response.send(archive.toBuffer());
    }
}

module.exports = Backend;