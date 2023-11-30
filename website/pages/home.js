const app = Vue.createApp(
{
    setup()
    {
        let location_search_tags = Vue.ref([]);
        let location_search_name_suggestions = Vue.ref([]);
        let location_search_tag_suggestions = Vue.ref([]);

        async function fetch_search_suggestions(query)
        {
            const search_bar = document.getElementById("search_bar");
            const search_suggestions = document.getElementById("search_suggestions");

            const name_suggestion_request =
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(
                {
                    query,
                    query_property : "name",
                    filter_all_tags : true
                })
            };

            const tag_suggestion_request =
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(
                {
                    query,
                    query_property : "name",
                    output_properties : ["name", "type"],
                    filter_all_techniques : true,
                    filter_all_examples : true
                })
            };

            const name_suggestions = await (await fetch("/api/search_property", name_suggestion_request)).json();
            const tag_suggestions = await (await fetch("/api/search_property", tag_suggestion_request)).json();

            if(name_suggestions.length > 0 || tag_suggestions.length > 0)
            {
                let names = [];
                let tags = [];

                for(const suggestion of name_suggestions)
                {
                    names.push(suggestion.name);
                }

                for(const suggestion of tag_suggestions)
                {
                    if(tags.some(tag => tag.name == suggestion.name))
                    {
                        continue;
                    }

                    if(location_search_tags.value.some(tag => tag.name == suggestion.name))
                    {
                        continue;
                    }

                    tags.push(suggestion);
                }

                names.length = Math.min(names.length, 5); 
                tags.length = Math.min(tags.length, 3);

                location_search_name_suggestions.value = names;
                location_search_tag_suggestions.value = tags;

                search_bar.style.borderBottomLeftRadius = "0px";
                search_suggestions.classList.add("show");
            }

            else
            {
                search_bar.style.borderBottomLeftRadius = "var(--bs-border-radius)";
                search_suggestions.classList.remove("show");
            }
        }

        function perform_search(query, query_tags)
        {
            let search_url = "/browser?query=" + query + "&query_tags=";

            if(query_tags.length > 0)
            {
                search_url += query_tags[0].name + "+" + query_tags[0].type;

                for(let index = 1; index < query_tags.length; index++)
                {
                    search_url += "+" + query_tags[index].name + "+" + query_tags[index].type;
                }
            }

            search_url = search_url.replaceAll(" ", "%20");

            window.location = search_url;
        }

        async function on_query_change(event)
        {
            const search_input = document.getElementById("search_input");
            const query = search_input.value;

            fetch_search_suggestions(query)
        }

        async function on_query_tag_add(tag)
        {
            location_search_tags.value.push(tag);

            const search_input = document.getElementById("search_input");
            const query = search_input.value;
    
            fetch_search_suggestions(query);
        }

        async function on_query_tag_remove(tag)
        {
            location_search_tags.value = location_search_tags.value.filter(value => value.name != tag.name);

            const search_input = document.getElementById("search_input");
            const query_string = search_input.value;

            fetch_search_suggestions(query_string);
        }

        async function on_query_delete(event)
        {
            const search_input = document.getElementById("search_input");

            const query = search_input.value;
            const query_tags = location_search_tags.value;

            if(query.length > 0)
            {
                return;
            }

            if(query_tags.length <= 0)
            {
                return;
            }

            location_search_tags.value.pop();
        }

        function on_query_suggestion_click(suggestion)
        {
            const query = suggestion;
            const query_tags = location_search_tags.value;
            
            perform_search(query, query_tags);
        }

        function on_query_search(event)
        {
            const search_input = document.getElementById("search_input");

            const query = search_input.value;
            const query_tags = location_search_tags.value;

            perform_search(query, query_tags);
        }

        function on_test(name, type)
        {
            console.log(name + " " + type);
        }

        return {
            location_search_tags,
            location_search_name_suggestions,
            location_search_tag_suggestions,
            on_query_change,
            on_query_delete,
            on_query_tag_add,
            on_query_tag_remove,
            on_query_suggestion_click,
            on_query_search,
            on_test
        };
    }
});

app.component("ctag", ctag);
app.mount('#home');