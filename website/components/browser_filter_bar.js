import { ref } from "vue"
import Tag from "components/tag.js"
import BrowserFilterDate from "components/browser_filter_date.js"

export default
{
    components :
    {
        Tag,
        BrowserFilterDate
    },
    setup()
    {
        let browser_filter_tags = ref([]);
        let browser_filter_date_begin = ref("");
        let browser_filter_date_end = ref("");

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
                if(browser_filter_tags.value.some(tag => tag.name == tag_suggestion.name))
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

            browser_filter_tags.value.push(tag);
        }

        return {
            browser_filter_tags,
            browser_filter_date_begin,
            browser_filter_date_end,
            browser_tag_suggestion_query,
            browser_tag_suggestions,
            on_browser_tag_suggestion_open,
            on_browser_tag_suggestion_query_change,
            on_browser_tag_suggestion_select
        }
    },
    template:
    `
    <div>
        <button class="btn btn-toggle border-0 w-100 d-flex align-items-end browser-filter-toggle-arrow" type="button" data-bs-toggle="collapse" data-bs-target="#browser_filter_bar_collapse">
            <img src="symbols/caret_down_fill.svg" width="20px">
            <div class="ms-1">Filters</div>
        </button>
        <div id="browser_filter_bar_collapse" class="collapse px-4 pt-2">
            <ul class="list-unstyled">
                <li>
                    <label class="form-label" for="browser_filter_date_range">Date</label>
                    <input id="browser_filter_date_range" class="form-range" type="range" min="0" max="5">
                    <browser-filter-date></browser-filter-date>
                </li>
                <li>
                    <label class="form-label" for="browser_filter_tag_widget">Tags</label>
                    <div id="browser_filter_tag_widget" class="border rounded d-flex align-items-center p-1">
                        <div class="flex-fill me-1 d-flex flex-wrap align-items-center">
                            <tag v-for="tag in browser_filter_tags" :name="tag.name" :type="tag.type" is_removable="true" add_class="me-1"></tag>
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
                </li>
            </ul>
        </div>
    </div>
    `
}