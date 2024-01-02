const Visualization = require("./visualization.js");
const fs = require("fs");

class Sorting
{
    static import(sorting)
    {
        switch(sorting)
        {
        case "score_ascending":
            return Sorting.score_ascending;
        case "score_descending":
            return Sorting.score_descending;
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

        return Sorting.score_descending;
    }

    static score_ascending(candidate1, candidate2)
    {
        return candidate2.score - candidate1.score;
    }

    static score_descending(candidate1, candidate2)
    {
        return candidate1.score - candidate2.score;
    }

    static name_ascending(candidate1, candidate2)
    {
        return candidate1.get_name().localCompare(candidate2.get_name());
    }

    static name_descending(candidate1, candidate2)
    {
        return candidate2.get_name().localCompare(candidate1.get_name());
    }

    static date_ascending(candidate1, candidate2)
    {
        return candidate1.value.get_date() - candidate2.value.get_date();
    }

    static date_descending(candidate1, candidate2)
    {
        return candidate2.value.get_date() - candidate1.value.get_date();
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

            let score = this.#search_score(query, visualization.get_name());
            score = Math.min(score, this.#search_score(query, visualization.get_description()));
            score = Math.min(score, this.#search_score(query, visualization.get_date().toString()));

            for(const tag of visualization.get_tags())
            {
                score = Math.min(score, this.#search_score(query, tag.get_name()));
                score = Math.min(score, this.#search_score(query, tag.get_type()));
            }

            const candidate = 
            {
                value: visualization,
                score
            };

            candidates.push(candidate);
        }

        candidates.sort((candidate1, candidate2) =>
        {
            return sorting(candidate1, candidate2);
        });

        let result = [];

        for(const candidate of candidates)
        {
            result.push(candidate.value);
        }

        return result;
    }

    search_property(query, query_property, output_properties, filter)
    {
        let candidates = [];

        for(const visualization of this.#visualizations)
        {
            if(filter(visualization, null) && this.#search_has_properties(visualization, query_property, output_properties))
            {
                const candidate = this.#search_candidate(visualization, query, query_property, output_properties);

                if(candidate.score < 10)
                {
                    candidates.push(candidate);
                }
            }

            for(const tag of visualization.get_tags())
            {
                if(filter(visualization, tag) && this.#search_has_properties(tag, query_property, output_properties))
                {
                    const candidate = this.#search_candidate(tag, query, query_property, output_properties);

                    if(candidate.score < 10)
                    {
                        candidates.push(candidate);
                    }
                }
            }
        }

        candidates.sort((candidate1, candidate2) =>
        {
            return Sorting.score_descending(candidate1, candidate2);
        });

        let result = [];

        for(const candidate of candidates)
        {
            result.push(candidate.value);
        }

        return result;
    }

    #search_candidate(object, query, query_property, output_properties)
    {
        const exported = object.export();
        let score = this.#search_score(query, exported[query_property]);
        let value = {};

        for(const output_property of output_properties)
        {
            value[output_property] = exported[output_property];
        }

        return {
            score,
            value
        };
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

    // Levenshtein Distance
    #search_score(query, string)
    {
        return this.#search_score_internal(query, string, 0);
    }

    #search_score_internal(query, string, current_score)
    {
        if(query.length == 0)
        {
            return string.length;
        }

        if(string.length == 0)
        {
            return query.length;
        }

        if(query[0] == string[0])
        {
            return this.#search_score_internal(query.substring(1), string.substring(1), current_score);
        }

        const max_score = 10;
        const next_score = current_score + 1;

        if(next_score > max_score)
        {
            return 1;
        }

        const score1 = this.#search_score_internal(query.substring(1), string, next_score);
        const score2 = this.#search_score_internal(query, string.substring(1), next_score);
        const score3 = this.#search_score_internal(query.substring(1), string.substring(1), next_score);

        return 1 + Math.min(score1, score2, score3);
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