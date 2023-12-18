import { ref } from "vue"
import Tag from "components/tag.js"

export default
{
    components :
    {
        Tag
    },
    props: ["browser_filter_tags"],
    emit: ["on_browser_filter_tags_change"],
    setup(props, context)
    {
        let browser_tag_suggestion_query = ref("");
        let browser_tag_suggestions = ref([]);

        async function fetch_tag_suggestions()
        {
            const tag_request =
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(
                {
                    query : browser_tag_suggestion_query.value,
                    query_property : "name",
                    output_properties : ["name", "type"],
                    filter_all_techniques : true
                })
            };

            const tag_response = await (await fetch("/api/search_property", tag_request)).json();

            browser_tag_suggestions.value = [];

            for(const tag_suggestion of tag_response)
            {
                if(props.browser_filter_tags.value.some(tag => tag.name == tag_suggestion.name))
                {
                    continue;
                }

                if(browser_tag_suggestions.value.some(tag => tag.name == tag_suggestion.name))
                {
                    continue;
                }

                browser_tag_suggestions.value.push(tag_suggestion);
            }
        }

        function on_browser_tag_suggestion_open()
        {
            browser_tag_suggestion_query.value = "";

            fetch_tag_suggestions();
        }

        function on_browser_tag_suggestion_query_change()
        {
            fetch_tag_suggestions();
        }

        function on_browser_tag_suggestion_select(name, type)
        {
            const tag = 
            {
                name,
                type
            };

            let browser_filter_tags = props.browser_filter_tags;
            browser_filter_tags.push(tag);

            context.emit("on_browser_filter_tags_change", browser_filter_tags)
        }

        return {
            browser_tag_suggestion_query,
            browser_tag_suggestions,
            on_browser_tag_suggestion_open,
            on_browser_tag_suggestion_query_change,
            on_browser_tag_suggestion_select
        }
    },
    template:
    `
    <div class="border rounded d-flex align-items-center p-1">
        <div class="flex-fill me-1 d-flex flex-wrap align-items-center">
            <tag v-for="tag in browser_filter_tags" :name="tag.name" :type="tag.type" is_removable class="me-1"></tag>
        </div>
        <div class="dropdown align-self-end">
            <button class="btn btn-primary d-flex align-imtems-center justify-content-center p-1" input="button" data-bs-toggle="dropdown" @click="on_browser_tag_suggestion_open">
                <img src="symbols/plus.svg" width="20px">
            </button>
            <div class="dropdown-menu dropdown-menu-end p-2">
                <input class="form-control form-control-sm mb-2" type="text" placeholder="Search" v-model="browser_tag_suggestion_query" @input="on_browser_tag_suggestion_query_change">
                <ul class="list-unstyled border rounded overflow-y-scroll" style=" min-height: 50px; max-height: 80px;">
                    <li v-for="tag in browser_tag_suggestions">
                        <tag :name="tag.name" :type="tag.type" add_class="mb-1" add_style="width: 100px; text-align: left;" @on_tag_click="on_browser_tag_suggestion_select"></tag>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    `
}