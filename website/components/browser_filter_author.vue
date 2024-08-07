<script>
    import { ref, watch } from "vue";
    
    export default
    {
        props: ["browser_filters"],
        emit: ["update:browser_filters"],
        setup(props, context)
        {
            let browser_author_suggestion_query = ref("");
            let browser_author_suggestions = ref([]);

            watch([browser_author_suggestion_query, props.browser_filters], async (old_state, new_state) =>
            {
                const author_request =
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(
                    {
                        query: browser_author_suggestion_query.value
                    })
                };

                const author_response = await (await fetch("/api/search_author", author_request)).json();
                let author_suggestions = [];

                for(const author_candidate of author_response)
                {
                    if(props.browser_filters.authors.some(author => author.name == author_candidate.name))
                    {
                        continue;
                    }

                    if(author_suggestions.some(author => author.name == author_candidate.name))
                    {
                        continue;
                    }

                    author_suggestions.push(author_candidate);
                }

                browser_author_suggestions.value = author_suggestions;
            }, { immediate: true });

            function on_browser_author_remove(author)
            {
                let filters = props.browser_filters;
                filters.authors = filters.authors.filter(item =>
                {
                    return item.name != author.name || item.type != author.type; 
                });

                context.emit("update:browser_filters", filters);
            }

            function on_browser_author_suggestion_open()
            {
                browser_author_suggestion_query.value = "";
            }

            function on_browser_author_suggestion_select(author)
            {
                let filters = props.browser_filters;
                filters.authors.push(author);

                context.emit("update:browser_filters", filters);
            }

            return {
                browser_author_suggestion_query,
                browser_author_suggestions,
                on_browser_author_remove,
                on_browser_author_suggestion_open,
                on_browser_author_suggestion_select
            }
        }
    };
</script>

<template>
    <div class="border rounded d-flex align-items-center">
        <div class="flex-fill d-flex flex-wrap m-1">
            <template v-for="author of browser_filters.authors">
                <button class="btn badge text-secondary-emphasis bg-secondary-subtle border-secondary-subtle d-flex align-items-center px-2 py-1">
                    <span style="line-height: 18px;">{{ author }}</span>
                    <div class="ms-1 tag-removable-image" @click="on_browser_author_remove(author)"></div>
                </button>
            </template>
        </div>
        <div class="dropdown dropend-md align-self-end m-2">
            <button class="btn btn-primary d-flex align-items-center justify-content-center p-0" style="width: 28px; height: 28px;" input="button" data-bs-toggle="dropdown" @click="on_browser_author_suggestion_open">
                <img src="../assets/icons/plus.svg" width="20px">
            </button>
            <div class="dropdown-menu p-3">
                <input class="form-control mb-3 browser-filter-tag-search-bar" style="min-width: 200px;" type="text" placeholder="Search" v-model="browser_author_suggestion_query">
                <ul class="list-unstyled border rounded overflow-y-scroll" style="height: 150px;">
                    <li v-for="author of browser_author_suggestions">
                        <div class="dropdown-item d-flex align-items-center" @click="on_browser_author_suggestion_select(author)">
                            <div class="border rounded bg-secondary-subtle border-secondary-subtle me-2" style="width: 16px; height: 16px"></div>
                            <span>{{ author }}</span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>