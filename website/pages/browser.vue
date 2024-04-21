<script>
    import { ref, watch } from "vue"
    import BrowserHeader from "../components/browser_header.vue"
    import BrowserFilter from "../components/browser_filter.vue"
    import BrowserItem from "../components/browser_item.vue"
    import GlobalFooter from "../components/global_footer.vue"

    function setup_query()
    {
        const parameters = new URLSearchParams(window.location.search);
        let query = "";

        if(parameters.get("query") != null)
        {
            query = parameters.get("query");
        }

        return query;
    }

    function setup_filter_tags()
    {
        const parameters = new URLSearchParams(window.location.search);
        let tags = [];

        if(parameters.get("tags") != null)
        {
            const items = parameters.get("tags").split("+");

            for(let index = 0; index < items.length - 1; index += 3)
            {
                let tag = 
                {
                    name: items[index],
                    type: items[index + 1],
                    abbreviation: items[index + 2]
                };

                tags.push(tag);
            }
        }

        return tags;
    }

    async function setup_filter_date()
    {
        const visualization_request = 
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(
            {
                query: ""
            })
        }

        let visualization_response = await (await fetch("/api/search_visualizations", visualization_request)).json();

        let begin = "01 Jan 1900";
        let end = "01 Feb 1900";

        if(visualization_response.length > 0)
        {
            begin = visualization_response[0].date;
            end = visualization_response[0].date;

            for(const visualization of visualization_response)
            {
                const date_begin = new Date(begin);
                const date_end = new Date(end);
                const date_visualization = new Date(visualization.date);

                if(date_visualization < date_begin)
                {
                    begin = visualization.date;
                }

                if(date_visualization > date_end)
                {
                    end = visualization.date;
                }
            }

            let date_begin = new Date(begin);
            let date_end = new Date(end);

            date_begin.setDate(1);
            date_begin.setHours(0, 0, 0, 0);
            date_end.setDate(1);
            date_end.setHours(0, 0, 0, 0);
            
            if(date_end.getMonth() >= 11)
            {
                date_end.setMonth(0);
                date_end.setFullYear(date_end.getFullYear() + 1);
            }

            else
            {
                date_end.setMonth(date_end.getMonth() + 1);
            }

            begin = date_begin.toString();
            end = date_end.toString();
        }

        return {
            begin,
            end
        }
    }

    export default
    {
        components:
        {
            "browser-header": BrowserHeader,
            "browser-filter": BrowserFilter,
            "browser-item": BrowserItem,
            "shared-footer": GlobalFooter
        },
        setup()
        {
            let browser_items = ref([]);
            let browser_is_loading = ref(true);
            let browser_query = ref("");

            let browser_sorting = ref(
            {
                type: "relevance",
                direction: "descending"
            });
            
            let browser_filters = ref(
            {
                date_min: "01 Jan 1900",
                date_max: "01 Feb 1900",
                date_begin: "01 Jan 1900",
                date_end: "01 Feb 1900",
                tags: [],
                authors: []
            });

            watch([browser_query, browser_sorting, browser_filters], async (old_state, new_state) =>
            {
                const loading_timer = setTimeout(() =>
                {
                    browser_is_loading.value = true;    
                }, 100);

                const visualization_request =
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(
                    {
                        query: browser_query.value,
                        sorting: browser_sorting.value.type + "_" + browser_sorting.value.direction,
                        filter_date_begin: browser_filters.value.date_begin, 
                        filter_date_end: browser_filters.value.date_end,
                        filter_tags: browser_filters.value.tags
                    })
                };

                let visualization_response = await (await fetch("/api/search_visualizations", visualization_request)).json();
                browser_items.value = [];

                for(const visualization of visualization_response)
                {
                    const browser_item = 
                    {
                        name: visualization.name,
                        tags: visualization.tags,
                        images: visualization.images
                    };

                    browser_items.value.push(browser_item);
                }

                clearTimeout(loading_timer);
                browser_is_loading.value = false;
            }, { deep: true});

            function on_browser_item_click(item)
            {
                window.location = "/visualization?name=" + encodeURIComponent(item.name);
            }

            function on_browser_item_tag_click(tag)
            {
                if(!browser_filters.value.tags.some(filter_tag => filter_tag.name == tag.name))
                {
                    browser_filters.value.tags.push(tag);
                }
            }

            return {
                browser_items,
                browser_is_loading,
                browser_query,
                browser_sorting,
                browser_filters,
                setup_query,
                setup_filter_date,
                setup_filter_tags,
                on_browser_item_click,
                on_browser_item_tag_click
            }
        },
        async mounted()
        {
            const query = setup_query();
            const filter_tags = setup_filter_tags();
            const filter_date = await setup_filter_date();

            this.browser_query = query;
            this.browser_filters.date_min = filter_date.begin;
            this.browser_filters.date_max = filter_date.end;
            this.browser_filters.date_begin = filter_date.begin;
            this.browser_filters.date_end = filter_date.end;
            this.browser_filters.tags = filter_tags;
        }
    };
</script>

<template>
    <header class="sticky-top">
            <browser-header v-model:browser_query="browser_query" v-model:browser_sorting="browser_sorting"></browser-header>
            <browser-filter class="border-bottom d-lg-none bg-white" v-model:browser_filters="browser_filters"></browser-filter>
    </header>
    <main>
        <div class="d-flex bg-body-tertiary">
            <browser-filter class="sticky-top card m-3 align-self-start flex-shrink-0 d-none d-lg-block" style="width: 300px; top: 82px;" v-model:browser_filters="browser_filters"></browser-filter>
            <div class="flex-fill my-3 me-3 ms-3 ms-lg-0">
                <div v-if="browser_is_loading" class="d-flex align-items-center justify-content-center" style="height: 300px;">
                    <div class="spinner-border text-body-tertiary" role="status"></div>
                    <span class="ms-2 text-body-tertiary fw-semibold fs-4">Loading visualizations</span>
                </div>
                <div v-else-if="browser_items.length > 0" class="row row-cols-1 row-cols-md-2 row-cols-lg-2 row-cols-xxl-3 g-3">
                    <div v-for="item of browser_items" class="col">
                        <browser-item :browser_item="item" :browser_filters="browser_filters" @on_browser_item_click="on_browser_item_click(item)" @on_browser_item_tag_click="on_browser_item_tag_click"></browser-item>
                    </div>
                </div>
                <div v-else class="d-flex align-items-center justify-content-center" style="height: 300px;">
                    <img src="../assets/icons/not_found.svg" style="width: 32px; margin-bottom: -6px;">
                    <span class="ms-2 text-body-tertiary fw-semibold fs-4">No visualizations found</span>
                </div>
            </div>
        </div>
    </main>
    <footer>
        <shared-footer class="container-fluid px-4"></shared-footer>
    </footer>
</template>