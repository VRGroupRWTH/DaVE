Vue.createApp(
{
    setup()
    {
        let location_tags = Vue.ref([]);
        let location_technique_overviews = Vue.ref([]);
        let sorting = "relevance";

        function parse_url(url)
        {
            let query = "";
            let query_tags = [];

            let arguments = url.substring(url.indexOf('?') + 1);
            arguments = arguments.replaceAll("%20", " ");

            for(const argument of arguments.split('&'))
            {
                const argument_name = argument.substring(0, argument.indexOf("="));

                if(argument_name == "query")
                {
                    query = argument.substring(argument.indexOf("=") + 1);
                }

                else if(argument_name == "query_tags")
                {
                    const tag_values = argument.substring(argument.indexOf("=") + 1).split("+");

                    for(let index = 1; index < tag_values.length; index += 2)
                    {
                        let tag = 
                        {
                            name: tag_values[index - 1],
                            type: tag_values[index]
                        }

                        query_tags.push(tag);
                    }
                }
            }

            return [query, query_tags];
        }

        async function fetch_tags()
        {
            const tag_request_options =
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({})
            };

            const tag_request = "/api/tags";
            const tags = await (await fetch(tag_request, tag_request_options)).json();

            location_tags.value = tags;
        }

        async function fetch_technique_overviews()
        {
            const search_input = document.getElementById("search_input");
            const general_author_input = document.getElementById("general_author_input");

            const query = search_input.value;
            
            const technique_request_options =
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(
                {
                    query,
                    filter_tags : location_tags.value
                })
            };

            let techniques = await (await fetch("/api/search_techniques", technique_request_options)).json();

            for(let technique of techniques)
            {
                if(technique.images.length < 0)
                {
                    technique.preview_image = null;
                }

                else
                {
                    technique.preview_image = technique.images[0];
                }
            }

            location_technique_overviews.value = techniques;
        }

        function on_query_input(event)
        {
            fetch_technique_overviews();
        }

        function on_sorting_change(sorting)
        {
            sorting = sorting;

            fetch_technique_overviews();
        }

        function on_technique_click(technique)
        {
            window.location = "/technique?technique=" + technique;
        }

        return {
            location_technique_overviews,
            location_tags,
            parse_url,
            fetch_technique_overviews,
            on_query_input,
            on_sorting_change,
            on_technique_click
        };
    },

    mounted()
    {
        const [query, query_tags] = this.parse_url(window.location.search);

        const search_input = document.getElementById("search_input");
        search_input.value = query;
        this.location_tags = query_tags;

        this.fetch_technique_overviews();
    }
}).mount('#browser');