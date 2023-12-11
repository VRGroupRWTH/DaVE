import { ref } from "vue";

export default
{
    props: ["browser_query"],
    emits: ["on_browser_query_change", "on_browser_sorting_change"],
    setup(props, context)
    {
        let browser_query = ref(props.browser_query);
        let browser_sort_type = ref("Relevance");
        let browser_sort_direction = ref("Descending");

        function on_browser_sort_type_change(sort_type)
        {
            browser_sort_type.value = sort_type;

            context.emit("on_browser_sorting_change", browser_sort_type.value.toLowerCase(), browser_sort_direction.value.toLowerCase());
        }

        function on_browser_sort_direction_toggle()
        {
            if(browser_sort_direction.value == "Ascending")
            {
                browser_sort_direction.value = "Descending";
            }

            else if(browser_sort_direction.value == "Descending")
            {
                browser_sort_direction.value = "Ascending";
            }

            context.emit("on_browser_sorting_change", browser_sort_type.value.toLowerCase(), browser_sort_direction.value.toLowerCase());
        }

        return {
            browser_query,
            browser_sort_type,
            browser_sort_direction,
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
                <input id="search_input" type="text" class="form-control form-control-dark text-bg-dark browser-search-bar" style="max-width: 500px;" placeholder="Query" v-model="browser_query" @input="on_browser_query_change(browser_query.value)">
            </div>
            <div class="d-flex align-items-center justify-content-end">
                <div class="dropdown">
                    <button class="btn btn-dark dropdown-toggle border border-white d-none d-md-block" style="border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        {{browser_sort_type}}
                    </button>
                    <button class="btn btn-dark border border-white p-0 d-flex align-items-center justify-content-center d-md-none" style="width: 38px; height: 38px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        <img src="symbols/list.svg" width="20px">
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li><a :class="'dropdown-item ' + (browser_sort_type == 'Relevance' ? 'active' : '')" @click="on_browser_sort_type_change('Relevance')">Relevance</a></li>
                        <li><a :class="'dropdown-item ' + (browser_sort_type == 'Name' ? 'active' : '')" @click="on_browser_sort_type_change('Name')">Name</a></li>
                        <li><a :class="'dropdown-item ' + (browser_sort_type == 'Date' ? 'active' : '')" @click="on_browser_sort_type_change('Date')">Date</a></li>
                    </ul>
                </div>
                <button class="btn btn-dark border-start-0 border-white d-flex align-items-center justify-content-center p-0" style="width: 38px; height: 38px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;" type="button" @click="on_browser_sort_direction_toggle">
                    <img v-if="browser_sort_direction == 'Ascending'" src="symbols/sort_down.svg" width="20px">
                    <img v-if="browser_sort_direction == 'Descending'" src="symbols/sort_up.svg" width="20px">
                </button>
            </div>
        </div>
    </div>
    `
}