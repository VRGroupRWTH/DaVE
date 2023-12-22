import Tag from "components/tag.js"

export default
{
    components:
    {
        Tag
    },
    props: ["browser_item"],
    emits: ["on_browser_item_click", "on_browser_item_tag_click"],
    setup(props, context)
    {
        function on_browser_item_click_internal()
        {

        }

        return {
            on_browser_item_click_internal
        };
    },
    template:
    `
    <div class="card" @click="">
        <img :src="browser_item.images[0]" class="card-img-top" style="height: 150px; object-fit: contain;">
        <div class="card-body">
            <h5 class="card-title">{{ browser_item.name }}</h5>
            <div class="d-flex flex-wrap">
                <tag v-for="tag of browser_item.tags" :name="tag.name" :type="tag.type" class="me-1"></tag>
            </div>
        </div>
    </div>
    `
}