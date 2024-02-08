const Visualization = require("./visualization.js");
const fs = require("fs");
const fuzzysort = require("fuzzysort");

class Sorting
{
    static select(query, sorting)
    {
        if(query == "")
        {
            if(sorting == "relevance_ascending" || sorting == "relevance_descending")
            {
                return Sorting.name_descending;
            }
        }

        return Sorting.import(sorting);
    }

    static import(sorting)
    {
        switch(sorting)
        {
        case "relevance_ascending":
            return Sorting.relevance_ascending;
        case "relevance_descending":
            return Sorting.relevance_descending;
        case "name_ascending":
            return Sorting.name_ascending;
        case "name_descending":
            return Sorting.name_descending;
        case "date_ascending":
            return Sorting.date_ascending;
        case "date_descending":
            return Sorting.date_descending;
        default:
            break;
        }

        return Sorting.relevance_descending;
    }

    static relevance_ascending(candidate1, candidate2)
    {
        return candidate1.score - candidate2.score;
    }

    static relevance_descending(candidate1, candidate2)
    {
        return candidate2.score - candidate1.score;
    }

    static name_ascending(candidate1, candidate2)
    {
        return candidate2.name.localeCompare(candidate1.name);
    }

    static name_descending(candidate1, candidate2)
    {
        return candidate1.name.localeCompare(candidate2.name);
    }

    static date_ascending(candidate1, candidate2)
    {
        return candidate1.date - candidate2.date;
    }

    static date_descending(candidate1, candidate2)
    {
        return candidate2.date - candidate1.date;
    }
}

class Database
{
    #visualizations

    constructor()
    {
        this.#visualizations = [];
    }

    load(database_path)
    {
        const visualization_directory = fs.readdirSync(database_path);

        for(const visualization_path of visualization_directory)
        {
            let visualization = new Visualization();

            if(!visualization.load(database_path + visualization_path + "/"))
            {
                continue;
            }

            this.#visualizations.push(visualization);
        }
    }

    search_visualizations(query, sorting, filter)
    {
        let candidates = [];

        for(const visualization of this.#visualizations)
        {
            if(!filter(visualization))
            {
                continue;
            }

            let scores = [];
            scores.push(this.#search_score(query, visualization.get_name()));
            scores.push(this.#search_score(query, visualization.get_description()));

            let score_max = null;

            for(const score of scores)
            {
                if(score == null)
                {
                    continue;
                }

                if(score_max == null)
                {
                    score_max = score;
                }

                else
                {
                    score_max = Math.max(score_max, score);
                }
            }

            const candidate = 
            {
                score: score_max,
                name: visualization.get_name(),
                date: visualization.get_date(),
                value: visualization
            };

            candidates.push(candidate);
        }

        candidates.sort((candidate1, candidate2) =>
        {
            return sorting(candidate1, candidate2);
        });

        let results = [];

        for(const candidate of candidates)
        {
            results.push(candidate.value);
        }

        return results;
    }

    search_property(query, query_property, output_properties, filter)
    {
        let candidates = [];

        for(const visualization of this.#visualizations)
        {
            if(filter(visualization, null) && this.#search_has_properties(visualization, query_property, output_properties))
            {
                const candidate = this.#search_candidate(visualization, query, query_property, output_properties);

                if(candidate.score != null)
                {
                    candidates.push(candidate);
                }
            }

            for(const tag of visualization.get_tags())
            {
                if(filter(visualization, tag) && this.#search_has_properties(tag, query_property, output_properties))
                {
                    const candidate = this.#search_candidate(tag, query, query_property, output_properties);

                    if(candidate.score != null)
                    {
                        candidates.push(candidate);
                    }
                }
            }
        }

        let sorting = Sorting.select(query, "relevance_descending");

        candidates.sort((candidate1, candidate2) =>
        {
            return sorting(candidate1, candidate2);
        });

        let results = [];

        for(const candidate of candidates)
        {
            if(!results.includes(candidate.value))
            {
                results.push(candidate.value);
            }
        }

        return results;
    }

    #search_candidate(object, query, query_property, output_properties)
    {
        const exported = object.export();
        const score = this.#search_score(query, exported[query_property]);
        let value = {};

        for(const output_property of output_properties)
        {
            value[output_property] = exported[output_property];
        }

        return {
            score,
            name: exported[query_property],
            date: Date.now(),
            value
        };
    }

    #search_score(query, value)
    {
        if(query == "")
        {
            return 0;
        }

        const rating = fuzzysort.single(query, value);

        if(rating != null)
        {
            return rating.score;
        }

        return null;
    }

    #search_has_properties(object, query_property, output_properties)
    {
        const exported = object.export();

        if(!(query_property in exported))
        {
            return false;
        }

        for(const output_property of output_properties)
        {
            if(!(output_property in exported))
            {
                return false;
            }
        }

        return true;
    }

    get_visualization(visualization_name)
    {
        for(const visualization of this.#visualizations)
        {
            if(visualization.get_name() == visualization_name)
            {
                return visualization;
            }
        }

        return null;
    }
}

module.exports =
{
    Database,
    Sorting
}