import { ref, computed, watch } from "vue"

export default
{
    props: ["tag", "is_removable"],
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
            switch(props.tag.type)
            {
            case "technique":
                return "text-primary-emphasis bg-primary-subtle border-primary-subtle";
            case "domain":
                return "text-success-emphasis bg-success-subtle border-success-subtle";
            default:
                break;
            }

            return "";
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