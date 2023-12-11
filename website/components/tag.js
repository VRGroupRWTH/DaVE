export default
{
    props: ["name", "type", "add_class", "is_removable"],
    emits: ["on_tag_click", "on_tag_remove"],
    setup(props, context)
    {
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
            on_tag_click_internal,
            on_tag_remove_internal
        }
    },
    template:
    `
        <template v-if="is_removable == 'true'">
            <button :class="'btn badge text-primary-emphasis bg-primary-subtle border-primary-subtle py-0 d-flex align-items-center ' + add_class" style="height: 25px;" v-if="type == 'technique'" @click="on_tag_click_internal">
                {{ name }}
                <img class="ms-1" src="symbols/x_circle_fill.svg" @click="on_tag_remove_internal">
            </button>
            <button :class="'btn badge text-success-emphasis bg-success-subtle border-success-subtle py-0 d-flex align-items-center ' + add_class" style="height: 25px;" v-if="type == 'domain'" @click="on_tag_click_internal">
                {{ name }}
                <img class="ms-1" src="symbols/x_circle_fill.svg" @click="on_tag_remove_internal">
            </button>
        </template>
        <template v-if="is_removable != 'true'">
            <button type="button" :class="'btn badge text-primary-emphasis bg-primary-subtle border-primary-subtle ' + add_class" style="height: 25px;" v-if="type == 'technique'" @click="on_tag_click_internal">
                {{ name }}
            </button>
            <button type="button" :class="'btn badge text-success-emphasis bg-success-subtle border-success-subtle ' + add_class" style="height: 25px;" v-if="type == 'domain'" @click="on_tag_click_internal">
                {{ name }}
            </button>
        </template>
    `
}