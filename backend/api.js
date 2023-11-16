const {Database, Sorting} = require("./database.js");
const Tag = require("./tag.js");

class ServerAPI
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
        app.post("/api/fetch_example", async (request, response) => this.#on_fetch_example_request(request, response));
        app.post("/api/search_techniques", async (request, response) => this.#on_search_technqiues_request(request, response));
        app.post("/api/search_examples", async (request, response) => this.#on_search_examples_request(request, response));
        app.post("/api/search_property", async (request, response) => this.#on_search_property_request(request, response));
    }

    async #on_fetch_technique_request(request, response)
    {
        const technique_name = request.body.technique_name;

        const technique = this.#database.get_technique(technique_name);
        response.send(technique.export());
    }

    async #on_fetch_example_request(request, response)
    {
        const technique_name = request.body.technique_name;
        const example_name = request.body.example_name;

        const technique = this.#database.get_example(technique_name, example_name);
        response.send(technique.export());
    }

    async #on_search_technqiues_request(request, response)
    {
        const query = request.body.query;
        let sorting = Sorting.score_descending;
        let filter_tags = [];

        if("sorting" in request.body)
        {
            sorting = Sorting.import(request.body.sorting);
        }

        if("filter_tags" in request.body)
        {
            filter_tags = Tag.import(request.body.filter_tags);
        }

        const techniques = this.#database.search_techniques(query, sorting, (technique) =>
        {
            for(const filter_tag of filter_tags)
            {
                if(!technique.get_tags_combined().some(tag => tag.is_equal(filter_tag)))
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

    async #on_search_examples_request(request, response)
    {
        const query = request.body.query;
        let sorting = Sorting.score_descending;
        let filter_technique = null;
        let filter_author = null;
        let filter_tags = [];

        if("sorting" in request.body)
        {
            sorting = Sorting.import(request.body.sorting);
        }

        if("filter_technique" in request.body)
        {
            filter_technique = request.body.technique;
        }

        if("filter_author" in request.body)
        {
            filter_author = request.body.author;
        }

        if("filter_tags" in request.body)
        {
            filter_tags = Tag.import(request.body.filter_tags);
        }

        const examples = this.#database.search_examples(query, sorting, (technique, example) =>
        {
            if(filter_technique != null)
            {
                if(technique.get_name() != filter_technique)
                {
                    return false;
                }   
            }

            if(filter_author != null)
            {
                if(example.get_author() != filter_author)
                {
                    return false;
                }
            }

            for(const filter_tag of filter_tags)
            {
                if(!technique.get_tags_combined().some(tag => tag.is_equal(filter_tag)))
                {
                    return false;
                }
            }

            return true;
        });

        let result = [];

        for(const example of examples)
        {
            result.push(example.export());
        }

        response.send(result);
    }

    #on_search_property_request(request, response)
    {
        const query = request.body.query;
        const query_property = request.body.query_property;
        let output_properties = [request.body.query_property];
        let filter_all_techniques = false;
        let filter_all_examples = false;
        let filter_all_tags = false;

        if("output_properties" in request.body)
        {
            output_properties = request.body.output_properties;
        }

        if("filter_all_techniques" in request.body)
        {
            filter_all_techniques = request.body.filter_all_techniques;
        }

        if("filter_all_examples" in request.body)
        {
            filter_all_examples = request.body.filter_all_examples;
        }

        if("filter_all_tags" in request.body)
        {
            filter_all_tags = request.body.filter_all_tags;
        }

        const result = this.#database.search_property(query, query_property, output_properties, (technique, example, tag) =>
        {
            if(tag != null)
            {
                if(filter_all_tags)
                {
                    return false;
                }
            }

            else if(example != null)
            {
                if(filter_all_examples)
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
}

module.exports = ServerAPI;