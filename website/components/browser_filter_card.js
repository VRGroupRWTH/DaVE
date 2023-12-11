export default
{
    props: ["add_class"],
    emits: ["on_browser_filter_tag_add"],
    setup()
    {
        
    },
    template:
    `
    <div :class="'card shadow-sm ' + add_class">
        <button class="btn btn-toggle toggle-arrow rounded border-0 d-inline-flex align-items-center" type="button" data-bs-toggle="collapse" data-bs-target="#collapse_tags" aria-expanded="true" aria-controls="collapse_tags">
            <div class="h5 m-0">
                Tags
            </div>
        </button>
    </div>
    `
}