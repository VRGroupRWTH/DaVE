<script>
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
        }
    };
</script>

<template>
    <nav class="navbar navbar-expand bg-dark shadow-sm" data-bs-theme="dark">
        <div class="container-fluid px-3 align-items-center" style="display: grid; grid-auto-flow: column; grid-template-columns: 1fr 2fr 1fr">
            <div class="d-flex justify-content-start">
                <div class="navbar-nav align-items-center">
                    <a class="navbar-brand" href="/"><img src="../assets/icons/dave_logo_dark.svg" width="40px" height="40px"></a>
                    <a class="nav-link d-none d-xl-block active" href="/browser">Browser</a>
                    <div class="dropdown d-none d-xl-block">
                        <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Guide</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="/guide">Overview</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="/guide_use_dave">How to use DaVE?</a></li>
                            <li><a class="dropdown-item" href="/guide_extend_dave">Extending DaVE</a></li>
                        </ul>
                    </div>
                    <a class="nav-link d-none d-xl-block" href="/about">About</a>
                </div>
            </div>
            <div class="d-flex justify-content-center">
                <input class="form-control browser-header-search-bar" style="max-width: 500px;" type="text" placeholder="Search" :value="browser_query" @input="on_browser_query_change($event.target.value)">
            </div>
            <div class="d-flex justify-content-end">
                <div class="dropdown">
                    <button class="focus-ring focus-ring-secondary btn border dropdown-toggle d-none d-md-block browser-header-dropdown" style="border-color: #495057 !important; --bs-focus-ring-color: rgba(255, 255, 255, 0.55); color: var(--bs-body-color); height: 40px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        {{ browser_sort_type_names[browser_sorting.type] }}
                    </button>
                    <button class="navbar-toggler d-flex align-items-center justify-content-between p-2 d-md-none" style="border-color: #495057 !important; width: 40px; height: 40px; border-top-right-radius: 0px; border-bottom-right-radius: 0px;" type="button" data-bs-toggle="dropdown">
                        <span class="navbar-toggler-icon browser-header-toggle"></span>
                    </button>
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li v-for="(sort_type_name, sort_type) of browser_sort_type_names">
                            <div class="dropdown-item d-flex align-items-center" @click="on_browser_sort_type_change(sort_type)">
                                <img v-if="browser_sorting.type == sort_type" width="12px" style="margin-bottom: -2px" src="../assets/icons/circle.svg">
                                <div v-else style="width: 12px;"></div>
                                <span class="ms-2">{{ sort_type_name }}</span>
                            </div>
                        </li>
                    </ul>
                </div>
                <button class="btn btn-dark border border-start-0 d-flex align-items-center justify-content-center p-0" style="width: 40px; height: 40px; border-color: #495057 !important; border-top-left-radius: 0px; border-bottom-left-radius: 0px;" type="button" @click="on_browser_sort_direction_toggle">
                    <img v-if="browser_sorting.direction == 'ascending'" src="../assets/icons/sort_ascending.svg" width="20px">
                    <img v-if="browser_sorting.direction == 'descending'" src="../assets/icons/sort_descending.svg" width="20px">
                </button>
            </div>
        </div>
    </nav>
</template>