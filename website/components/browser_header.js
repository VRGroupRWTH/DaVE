export default
{
    props: ["browser_query", "browser_sorting"],
    emits: ["update:browser_query", "update:browser_sorting"],
    setup(props, context)
    {
        const browser_sort_type_names = 
        {
            relevance: "Relevance",
            name: "Name",
            date: "Date"
        };

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

            if(props.browser_sorting.direction == "ascending")
            {
                direction = "descending";
            }

            else if(props.browser_sorting.direction == "descending")
            {
                direction = "ascending";
            }

            let sorting = props.browser_sorting;
            sorting.direction = direction;

            context.emit("update:browser_sorting", sorting);
        }

        return {
            browser_sort_type_names,
            on_browser_query_change,
            on_browser_sort_type_change,
            on_browser_sort_direction_toggle
        }
    },
    template:
    `
    <div class="navbar bg-dark shadow-sm">
        <div class="w-100 px-4 py-1" style="display: grid; grid-auto-flow: column; grid-auto-columns: 1fr;">
            <div class="d-flex align-items-center justify-content-start">
                <a href="/"><img src="symbols/dave_logo_dark.svg" width="38px"></a>
            </div>
            <div class="d-flex align-items-center justify-content-center">
                <input id="search_input" type="text" class="form-control form-control-dark text-bg-dark browser-search-bar" style="max-width: 500px;" placeholder="Search" :value="browser_query" @input="on_browser_query_change($event.target.value)">
            </div>
            <div class="d-flex align-items-center justify-content-end">
                <div class="dropdown">
                    <button class="btn btn-dark dropdown-toggle border border-white d-none d-md-block" style="border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        {{ browser_sort_type_names[browser_sorting.type] }}
                    </button>
                    <button class="btn btn-dark border border-white p-0 d-flex align-items-center justify-content-center d-md-none" style="width: 38px; height: 38px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        <img src="symbols/list.svg" width="20px">
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li v-for="(sort_type_name, sort_type) of browser_sort_type_names">
                            <div class="dropdown-item d-flex align-items-center" @click="on_browser_sort_type_change(sort_type)">
                                <img v-if="browser_sorting.type == sort_type" width="12px" style="margin-bottom: -2px" src="symbols/circle.svg">
                                <div v-else style="width: 12px;"></div>
                                <span class="ms-2">{{ sort_type_name }}</span>
                            </div>
                        </li>
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