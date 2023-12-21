export default
{
    props: ["browser_item"],
    setup(props, context)
    {

    },
    template:
    `
    <div class="card">
        {{ browser_item.name }}
    </div>
    `
}