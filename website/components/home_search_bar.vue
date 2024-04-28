<script>
    import { ref, watch } from "vue"
    import Tag from "./tag.vue"

    export default
    {
        components:
        {
            Tag
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

            watch([query, tags], async (old_state, new_state) =>
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
                        output_properties : ["name", "type", "abbreviation"],
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
            }, { deep: true });

            function on_search_bar_search_internal()
            {
                context.emit("on_search_bar_search", query.value, tags.value);
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
            }

            function on_search_bar_query_escape(event)
            {
                search_bar_style.value = "";
                search_dropdown_class.value = "";
            }

            function on_search_bar_tag_remove(tag)
            {
                tags.value = tags.value.filter(item => item.name != tag.name || item.type != tag.type);
            }

            function on_search_bar_query_suggestion_select(query)
            {
                context.emit("on_search_bar_search", query, tags.value);
            }

            function on_search_bar_tag_suggestion_select(tag)
            {
                tags.value.push(tag);
            }

            return {
                query,
                query_suggestions,
                tags,
                tag_suggestions,
                search_bar_style,
                search_dropdown_class,
                on_search_bar_search_internal,
                on_search_bar_query_delete,
                on_search_bar_query_escape,
                on_search_bar_tag_remove,
                on_search_bar_query_suggestion_select,
                on_search_bar_tag_suggestion_select,
            }
        }
    };
</script>

<template>
    <div class="d-flex justify-content-center">
        <div class="position-relative w-100" style="max-width: 550px">
            <div class="form-control shadow w-100" :style="'border-bottom-right-radius: 0px; border-top-right-radius: 0px; border-color: color-mix(in srgb, var(--bs-border-color-translucent) 85%, var(--bs-black)); ' + search_bar_style">
                <div class="d-flex" style="height: 28px">                     
                    <img src="../assets/icons/search.svg" width="16px" class="ms-1 me-2">
                    <Tag v-for="tag of tags" :tag="tag" class="me-1" @on_tag_click="on_search_bar_tag_remove"></Tag>
                    <input class="flex-fill" style="border: none; outline: none;" size="1" v-model="query" type="text" placeholder="Describe your data" @keydown.delete="on_search_bar_query_delete" @keydown.enter="on_search_bar_search_internal" @keydown.escape="on_search_bar_query_escape">
                </div>
            </div>
            <ul :class="'dropdown-menu shadow position-absolute top-100 w-100 ' + search_dropdown_class" style="inset: 0px 0px auto 0px; border-top-left-radius: 0px; border-top-right-radius: 0px; border-top-width: 0px; border-color: color-mix(in srgb, var(--bs-border-color-translucent) 85%, var(--bs-black));">
                <li v-for="query of query_suggestions">
                    <button class="dropdown-item text-truncate" type="button" @click="on_search_bar_query_suggestion_select(query)"> 
                        {{query}} 
                    </button>
                </li>
                <li v-if="query_suggestions.length > 0 && tag_suggestions.length > 0">
                    <hr class="dropdown-divider" style="border-color: color-mix(in srgb, var(--bs-border-color-translucent) 85%, var(--bs-black));">
                </li>
                <li class="d-flex" style="padding-left: 12px; padding-right: 12px;">
                    <Tag v-for="tag of tag_suggestions" :tag="tag" class="me-1" @on_tag_click="on_search_bar_tag_suggestion_select"></Tag>
                </li>
            </ul>
        </div>
        <button class="btn btn-primary shadow" style="border-bottom-left-radius: 0px; border-top-left-radius: 0px;" type="button" @click="on_search_bar_search_internal">Search</button>
    </div>
</template>