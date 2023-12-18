import { computed } from "vue"

export default
{
    props: ["name", "type", "is_removable"],
    emits: ["on_tag_click", "on_tag_remove"],
    setup(props, context)
    {
        let tag_class = computed(() =>
        {
            switch(props.type)
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

        function on_tag_click_internal(event)
        {
            context.emit("on_tag_click", props.name, props.type);
        }

        function on_tag_remove_internal(event)
        {
            context.emit("on_tag_remove", props.name, props.type);

            event.stopPropagation();
        }

        return {
            tag_class,
            on_tag_click_internal,
            on_tag_remove_internal
        }
    },
    template:
    `
    <button class="btn badge py-0 d-flex align-items-center" :class="tag_class" style="height: 25px;" @click="on_tag_click_internal">
        {{ name }}
        <img v-if="is_removable" class="ms-1" src="symbols/x_circle_fill.svg" @click="on_tag_remove_internal">
    </button>
    `
}