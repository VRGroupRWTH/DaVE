export default
{
    props: ["technique"],
    template:
    `
    <div class="card card-body shadow-sm d-flex flex-row align-items-center justify-content-between">
        <span>Render Script</span>
        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#technique_wizzard_modal">Create</button>
        <div id="technique_wizzard_modal" class="modal fade" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    
                    <a href="/api/create_script?hallo=1" download>a</a>

                </div>
            </div>
        </div>
    </div>
    `
}