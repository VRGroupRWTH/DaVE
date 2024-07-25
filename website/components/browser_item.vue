<script>
    import { ref, computed, watch } from "vue"
    import * as bootstrap from "bootstrap";

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
            let browser_item_preview_icon = ref(null);
            let browser_item_tooltip_handle = ref(null);

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

            watch([browser_item_preview_icon], (old_state, new_state) =>
            {
                if(browser_item_tooltip_handle.value != null)
                {
                    browser_item_tooltip_handle.value.dispose();
                    browser_item_tooltip_handle.value = null;
                }

                if(browser_item_preview_icon.value != null)
                {
                    browser_item_preview_icon.value.setAttribute("data-bs-title", "Preview available");
                    browser_item_preview_icon.value.setAttribute("data-bs-placement", "left");
                    browser_item_tooltip_handle.value = new bootstrap.Tooltip(browser_item_preview_icon.value);
                }
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
                browser_item_preview_icon,
                browser_item_tooltip_handle,
                browser_item_filter_tags,
                browser_item_tags,
                on_browser_item_click_internal,
                on_browser_item_tag_click_internal
            };
        },
        unmounted()
        {
            if(this.browser_item_tooltip_handle != null)
            {
                this.browser_item_tooltip_handle.dispose();
                this.browser_item_tooltip_handle = null;
            }
        }
    };
</script>

<template>
    <div class="card h-100" style="cursor: pointer;" @click="on_browser_item_click_internal">
        <div style="position: relative; height: 200px;">
            <img ref="browser_item_preview_icon" v-if="browser_item.has_preview" src="/assets/icons/3d_view.svg" style="width: 30px; background-color: white; position: absolute; top: 14px; right: 14px;">
            <img :src="browser_item.images[0]" class="card-img-top p-3 pb-0 h-100" style="object-fit: contain;">
        </div>
        <div class="card-body">
            <h5 class="card-title">{{ browser_item.name }}</h5>
            <div class="d-flex flex-wrap" style="margin: -0.125rem">
                <Tag v-for="tag of browser_item_filter_tags" :tag="tag" style="margin: 0.125rem" is_highlighted="true" @on_tag_click="on_browser_item_tag_click_internal"></Tag>
                <Tag v-for="tag of browser_item_tags" :tag="tag" style="margin: 0.125rem" @on_tag_click="on_browser_item_tag_click_internal"></Tag>
            </div>
        </div>
    </div>
</template>