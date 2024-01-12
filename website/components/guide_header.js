export default
{
    template:
    `
    <div class="navbar navbar-expand bg-dark shadow-sm" data-bs-theme="dark">
        <div class="w-100 px-4 py-1 d-flex align-items-center justify-content-between">
            <div class="d-flex">
                <div class="d-flex align-items-center justify-content-start me-4">
                    <a href="/"><img src="symbols/dave_logo_dark.svg" width="38px"></a>
                </div>
                <div class="navbar-nav d-none d-lg-flex">
                    <a class="nav-link" href="/browser">Browser</a>
                    <a class="nav-link active" aria-current="page" href="/guide">Guide</a>
                    <a class="nav-link" href="/about">About</a>
                </div>
            </div>
            <button class="d-flex d-lg-none navbar-toggler" style="width: 38px; height: 38px;" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>
    </div>
    `
}