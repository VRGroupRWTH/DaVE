<script>
    import { computed } from "vue"
    import { sort_tags, equal_tags } from "../components/tag.vue";
    import Tag from "../components/tag.vue";

    export default
    {
        components:
        {
            Tag
        },
        props: ["browser_item", "browser_filters"],
        emits: ["on_browser_item_click", "on_browser_item_tag_click"],
        setup(props, context)
        {
            let browser_item_filter_tags = computed(() =>
            {
                const filter_tags = props.browser_filters.tags;
                let tags = [];

                for(const tag of props.browser_item.tags)
                {
                    if(filter_tags.some(item => equal_tags(item, tag)))
                    {
                        tags.push(tag);
                    }
                }

                return sort_tags(tags);
            });

            let browser_item_tags = computed(() =>
            {
                const filter_tags = props.browser_filters.tags;
                let tags = [];

                for(const tag of props.browser_item.tags)
                {
                    if(!filter_tags.some(item => equal_tags(item, tag)))
                    {
                        tags.push(tag);
                    }
                }

                return sort_tags(tags);
            });

            function on_browser_item_click_internal()
            {
                context.emit("on_browser_item_click", props.browser_item);
            }

            function on_browser_item_tag_click_internal(tag)
            {
                context.emit("on_browser_item_tag_click", tag);
            }

            return {
                browser_item_filter_tags,
                browser_item_tags,
                on_browser_item_click_internal,
                on_browser_item_tag_click_internal
            };
        }
    };
</script>

<template>
    <div class="card h-100" style="cursor: pointer;" @click="on_browser_item_click_internal">
        <img :src="browser_item.images[0]" class="card-img-top m-3 mb-0" style="height: 150px; object-fit: contain;">
        <div class="card-body">
            <h5 class="card-title">{{ browser_item.name }}</h5>
            <div class="d-flex flex-wrap" style="margin: -0.125rem">
                <tag v-for="tag of browser_item_filter_tags" :tag="tag" style="margin: 0.125rem" is_highlighted="true" @on_tag_click="on_browser_item_tag_click_internal"></tag>
                <tag v-for="tag of browser_item_tags" :tag="tag" style="margin: 0.125rem" @on_tag_click="on_browser_item_tag_click_internal"></tag>
            </div>
        </div>
    </div>
</template>