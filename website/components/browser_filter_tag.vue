<script>
    import { ref, watch } from "vue";
    import Tag from "./tag.vue";

    export default
    {
        components:
        {
            Tag
        },
        props: ["browser_filters"],
        emit: ["update:browser_filters"],
        setup(props, context)
        {
            let browser_tag_suggestion_query = ref("");
            let browser_tag_suggestions = ref([]);

            watch([browser_tag_suggestion_query, props.browser_filters], async (old_state, new_state) =>
            {
                const tag_request =
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(
                    {
                        query: browser_tag_suggestion_query.value,
                        query_property: "name",
                        output_properties: ["name", "type", "abbreviation"],
                        filter_all_visualizations: true
                    })
                };

                const tag_response = await (await fetch("/api/search_property", tag_request)).json();
                let tag_suggestions = [];

                for(const tag_candidate of tag_response)
                {
                    if(props.browser_filters.tags.some(tag => tag.name == tag_candidate.name))
                    {
                        continue;
                    }

                    if(tag_suggestions.some(tag => tag.name == tag_candidate.name))
                    {
                        continue;
                    }

                    tag_suggestions.push(tag_candidate);
                }

                browser_tag_suggestions.value = tag_suggestions;
            }, { immediate: true });

            function on_browser_tag_remove(tag)
            {
                let filters = props.browser_filters;
                filters.tags = filters.tags.filter(item =>
                {
                    return item.name != tag.name || item.type != tag.type; 
                });

                context.emit("update:browser_filters", filters);
            }

            function on_browser_tag_suggestion_open()
            {
                browser_tag_suggestion_query.value = "";
            }

            function on_browser_tag_suggestion_select(tag)
            {
                let filters = props.browser_filters;
                filters.tags.push(tag);

                context.emit("update:browser_filters", filters);
            }

            return {
                browser_tag_suggestion_query,
                browser_tag_suggestions,
                on_browser_tag_remove,
                on_browser_tag_suggestion_open,
                on_browser_tag_suggestion_select
            }
        }
    };
</script>

<template>
    <div class="border rounded d-flex align-items-center">
        <div class="flex-fill d-flex flex-wrap m-1">
            <Tag v-for="tag of browser_filters.tags" :tag="tag" is_removable="true" class="m-1" @on_tag_remove="on_browser_tag_remove"></Tag>
        </div>
        <div class="dropdown dropend-md align-self-end m-2">
            <button class="btn btn-primary d-flex align-items-center justify-content-center p-0" style="width: 28px; height: 28px;" input="button" data-bs-toggle="dropdown" @click="on_browser_tag_suggestion_open">
                <img src="../assets/icons/plus.svg" width="20px">
            </button>
            <div class="dropdown-menu p-3">
                <input class="form-control mb-3 browser-filter-tag-search-bar" style="min-width: 200px;" type="text" placeholder="Search" v-model="browser_tag_suggestion_query">
                <ul class="list-unstyled border rounded overflow-y-scroll" style="height: 150px;">
                    <li v-for="tag of browser_tag_suggestions">
                        <div class="dropdown-item d-flex align-items-center" @click="on_browser_tag_suggestion_select(tag)">
                            <div v-if="tag.type == 'dataset'" class="border rounded bg-primary-subtle border-primary-subtle me-2" style="width: 16px; height: 16px"></div>
                            <div v-if="tag.type == 'technique'" class="border rounded bg-danger-subtle border-danger-subtle me-2" style="width: 16px; height: 16px"></div>
                            <div v-if="tag.type == 'domain'" class="border rounded bg-success-subtle border-success-subtle me-2" style="width: 16px; height: 16px"></div>
                            <span>{{ tag.name }}</span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>