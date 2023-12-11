const {Database, Sorting} = require("./database.js");
const Tag = require("./tag.js");

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
            response.send([]);
        }
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
}

module.exports = Backend;