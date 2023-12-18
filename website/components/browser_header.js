import { computed } from "vue";

export default
{
    props: ["browser_query", "browser_sorting"],
    emits: ["update:browser_query", "update:browser_sorting"],
    setup(props, context)
    {
        let browser_sort_type_name = computed(() =>
        {
            switch(props.browser_sorting.type)
            {
            case "relevance":
                return "Relevance";
            case "name":
                return "Name";
            case "date":
                return "Date";
            default:
                break;
            }

            return "";
        });

        function on_browser_query_change(query)
        {
            context.emit("update:browser_query", query);
        }

        function on_browser_sort_type_change(type)
        {
            let sorting = props.browser_sorting;
            sorting.type = type;

            context.emit("update:browser_sorting", sorting);
        }

        function on_browser_sort_direction_toggle()
        {
            let direction = "";

            if(props.browser_sort_direction == "ascending")
            {
                direction = "descending";
            }

            else if(browser_sort_direction.value == "descending")
            {
                direction = "ascending";
            }

            let sorting = props.browser_sorting;
            sorting.direction = direction;

            context.emit("update:browser_sorting", sorting);
        }

        return {
            browser_sort_type_name,
            on_browser_query_change,
            on_browser_sort_type_change,
            on_browser_sort_direction_toggle
        }
    },
    template:
    `
    <div class="navbar navbar-dark bg-dark shadow-sm">
        <div class="w-100 px-4 py-1" style="display: grid; grid-auto-flow: column; grid-auto-columns: 1fr;">
            <div class="d-flex align-items-center justify-content-start">
                <a href="/"><img src="symbols/dave_logo_dark.svg" width="38px"></a>
            </div>
            <div class="d-flex align-items-center justify-content-center">
                <input id="search_input" type="text" class="form-control form-control-dark text-bg-dark browser-search-bar" style="max-width: 500px;" placeholder="Query" :value="browser_query" @input="on_browser_query_change($event.target.value)">
            </div>
            <div class="d-flex align-items-center justify-content-end">
                <div class="dropdown">
                    <button class="btn btn-dark dropdown-toggle border border-white d-none d-md-block" style="border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        {{browser_sort_type_name}}
                    </button>
                    <button class="btn btn-dark border border-white p-0 d-flex align-items-center justify-content-center d-md-none" style="width: 38px; height: 38px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        <img src="symbols/list.svg" width="20px">
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li><a :class="'dropdown-item ' + (browser_sorting.type == 'relevance' ? 'active' : '')" @click="on_browser_sort_type_change('relevance')">Relevance</a></li>
                        <li><a :class="'dropdown-item ' + (browser_sorting.type == 'name' ? 'active' : '')" @click="on_browser_sort_type_change('name')">Name</a></li>
                        <li><a :class="'dropdown-item ' + (browser_sorting.type == 'date' ? 'active' : '')" @click="on_browser_sort_type_change('date')">Date</a></li>
                    </ul>
                </div>
                <button class="btn btn-dark border-start-0 border-white d-flex align-items-center justify-content-center p-0" style="width: 38px; height: 38px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;" type="button" @click="on_browser_sort_direction_toggle">
                    <img v-if="browser_sorting.direction == 'ascending'" src="symbols/sort_down.svg" width="20px">
                    <img v-if="browser_sorting.direction == 'descending'" src="symbols/sort_up.svg" width="20px">
                </button>
            </div>
        </div>
    </div>
    `
}