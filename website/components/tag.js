import { ref, computed, watch } from "vue"

const tag_types = 
[
    "technique",
    "domain"
];

export function equal_tags(tag1, tag2)
{
    return tag1.name == tag2.name && tag1.type == tag2.type;
}

export function compare_tags(tag1, tag2)
{
    const type_index1 = tag_types.indexOf(tag1.type);
    const type_index2 = tag_types.indexOf(tag2.type);

    if(type_index1 == type_index2)
    {
        return tag1.name.localeCompare(tag2.name);
    }

    return type_index1 - type_index2;
}

export function sort_tags(tags)
{
    return tags.sort(compare_tags);
}

export const Tag =
{
    props: ["tag", "is_removable", "is_highlighted"],
    emits: ["on_tag_click", "on_tag_remove"],
    setup(props, context)
    {
        let tag_button = ref(null);
        let tag_tooltip_handle = ref(null);

        let tag_name = computed(() =>
        {
            if(props.tag.abbreviation != "")
            {
                return props.tag.abbreviation;
            }

            return props.tag.name;
        });

        let tag_class = computed(() =>
        {
            let class_list = "";

            switch(props.tag.type)
            {
            case "technique":
                class_list = "text-primary-emphasis bg-primary-subtle border-primary-subtle";
                break;
            case "domain":
                class_list = "text-success-emphasis bg-success-subtle border-success-subtle";
                break;
            default:
                break;
            }

            if("is_highlighted" in props)
            {
                if(props.is_highlighted)
                {
                    switch(props.tag.type)
                    {
                    case "technique":
                        class_list += " tag-highlight-technique";
                        break;
                    case "domain":
                        class_list += " tag-highlight-domain";
                        break;
                    default:
                        break;
                    }
                }
            }

            return class_list;
        });

        watch([props, tag_button], (old_state, new_state) =>
        {
            if(tag_tooltip_handle.value != null)
            {
                tag_tooltip_handle.value.dispose();
                tag_tooltip_handle.value = null;
            }

            if(tag_button.value != null && props.tag.abbreviation != "")
            {
                tag_button.value.setAttribute("data-bs-title", props.tag.name);
                tag_tooltip_handle.value = new bootstrap.Tooltip(tag_button.value);
            }
        });

        function on_tag_click_internal(event)
        {
            context.emit("on_tag_click", props.tag);

            event.stopPropagation();
        }

        function on_tag_remove_internal(event)
        {
            context.emit("on_tag_remove", props.tag);

            event.stopPropagation();
        }

        return {
            tag_button,
            tag_tooltip_handle,
            tag_name,
            tag_class,
            on_tag_click_internal,
            on_tag_remove_internal,
        }
    },
    unmounted()
    {
        if(this.tag_tooltip_handle != null)
        {
            this.tag_tooltip_handle.dispose();
            this.tag_tooltip_handle = null;
        }
    },
    template:
    `
    <button ref="tag_button" class="btn badge d-flex align-items-center px-2 py-1" :class="tag_class" @click="on_tag_click_internal" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="none">
        <span style="line-height: 18px;">{{ tag_name }}</span>
        <div v-if="is_removable=='true'" class="ms-1 tag-removable-image" @click="on_tag_remove_internal"></div>
    </button>
    `
}