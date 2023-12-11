import { ref } from "vue"
import Tag from "components/tag.js"

export default
{
    components :
    {
        tag : Tag
    },
    emits: ["on_search_bar_search"],
    setup(props, context)
    {
        let query = ref("");
        let query_suggestions = ref([]);
        const query_suggestion_limit = 5;

        let tags = ref([]);
        let tag_suggestions = ref([]);
        const tag_suggestion_limt = 3;

        let search_bar_style = ref("");
        let search_dropdown_class = ref("");

        async function fetch_suggestions()
        {
            const query_request =
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(
                {
                    query : query.value,
                    query_property : "name",
                    filter_all_tags : true
                })
            };

            const tag_request =
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(
                {
                    query : query.value,
                    query_property : "name",
                    output_properties : ["name", "type"],
                    filter_all_techniques : true
                })
            };

            const query_response = await (await fetch("/api/search_property", query_request)).json();
            const tag_response = await (await fetch("/api/search_property", tag_request)).json();

            query_suggestions.value = [];
            tag_suggestions.value = [];

            for(const query_suggestion of query_response)
            {
                query_suggestions.value.push(query_suggestion.name);
            }

            for(const tag_suggestion of tag_response)
            {
                if(tags.value.some(tag => tag.name == tag_suggestion.name))
                {
                    continue;
                }

                if(tag_suggestions.value.some(tag => tag.name == tag_suggestion.name))
                {
                    continue;
                }

                tag_suggestions.value.push(tag_suggestion);
            }

            query_suggestions.value.length = Math.min(query_suggestions.value.length, query_suggestion_limit); 
            tag_suggestions.value.length = Math.min(tag_suggestions.value.length, tag_suggestion_limt);

            if((query.value.length > 0 || tags.value.length > 0) && (query_suggestions.value.length > 0 || tag_suggestions.value.length > 0))
            {
                search_bar_style.value = "border-bottom-left-radius: 0px;";
                search_dropdown_class.value = "show";
            }

            else
            {
                search_bar_style.value = "";
                search_dropdown_class.value = "";
            }
        }

        function on_search_bar_search_internal()
        {
            context.emit("on_search_bar_search", query.value, tags.value);
        }

        function on_search_bar_query_change()
        {
            fetch_suggestions();
        }

        function on_search_bar_query_delete(event)
        {
            if(event.target.selectionStart > 0)
            {
                return;
            }

            if(tags.value.length <= 0)
            {
                return;
            }

            tags.value.pop();

            fetch_suggestions();
        }

        function on_search_bar_query_escape(event)
        {
            search_bar_style.value = "";
            search_dropdown_class.value = "";
        }

        function on_search_bar_tag_remove(name, type)
        {
            tags.value = tags.value.filter(tag => tag.name != name);

            fetch_suggestions();
        }

        function on_search_bar_query_suggestion_select(query)
        {
            context.emit("on_search_bar_search", query, tags.value);
        }

        function on_search_bar_tag_suggestion_select(name, type)
        {
            const tag = 
            {
                name,
                type
            };

            tags.value.push(tag);

            fetch_suggestions();
        }

        return {
            query,
            query_suggestions,
            tags,
            tag_suggestions,
            search_bar_style,
            search_dropdown_class,
            on_search_bar_search_internal,
            on_search_bar_query_change,
            on_search_bar_query_delete,
            on_search_bar_query_escape,
            on_search_bar_tag_remove,
            on_search_bar_query_suggestion_select,
            on_search_bar_tag_suggestion_select,
        }
    },
    template:
    `
    <div class="d-flex justify-content-center">
        <div class="position-relative w-100" style="max-width: 700px">
            <div class="form-control shadow-sm w-100" :style="'border-bottom-right-radius: 0px; border-top-right-radius: 0px; border-color: var(--bs-border-color-translucent); ' + search_bar_style">
                <div class="d-flex">                     
                    <tag v-for="tag in tags" :name="tag.name" :type="tag.type" add_class="me-1" @on_tag_click="on_search_bar_tag_remove"></tag>
                    <input class="flex-fill" style="border: none; outline: none;" size="1" v-model="query" type="text" placeholder="Query" @input="on_search_bar_query_change" @keydown.delete="on_search_bar_query_delete" @keydown.enter="on_search_bar_search_internal" @keydown.escape="on_search_bar_query_escape">
                </div>
            </div>
            <ul :class="'dropdown-menu shadow-sm position-absolute top-100 w-100 ' + search_dropdown_class" style="inset: 0px 0px auto 0px; border-top-left-radius: 0px; border-top-right-radius: 0px; border-top-width: 0px;">
                <li v-for="query in query_suggestions">
                    <button class="dropdown-item" type="button" @click="on_search_bar_query_suggestion_select(query)"> 
                        {{query}} 
                    </button>
                </li>
                <li v-if="query_suggestions.length > 0 && tag_suggestions.length > 0">
                    <hr class="dropdown-divider">
                </li>
                <li class="d-flex" style="padding-left: 12px; padding-right: 12px;">
                    <tag v-for="tag in tag_suggestions" :name="tag.name" :type="tag.type" add_class="me-1" @on_tag_click="on_search_bar_tag_suggestion_select"></tag>
                </li>
            </ul>
        </div>
        <button class="btn btn-primary shadow-sm" style="border-bottom-left-radius: 0px; border-top-left-radius: 0px;" type="button" @click="on_search_bar_search_internal">Search</button>
    </div>
    `
}