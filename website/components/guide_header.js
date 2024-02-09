export const GuideHeader =
{
    template:
    `
    <div class="navbar navbar-expand bg-dark shadow-sm" data-bs-theme="dark">
        <div class="container-xxl w-100 px-4 py-1 d-flex align-items-center justify-content-between">
            <div class="d-flex flex-fill">
                <div class="d-flex align-items-center justify-content-start me-4">
                    <a href="/"><img src="symbols/dave_logo_dark.svg" width="38px"></a>
                </div>
                <div class="navbar-nav d-flex flex-fill">
                    <a class="nav-link" href="/browser">Browser</a>
                    <a class="nav-link active" aria-current="page" href="/guide">Guide</a>
                    <a class="nav-link" href="/about">About</a>
                    <input type="text" class="form-control form-control-dark text-bg-dark browser-search-bar guide-search-bar-dark ms-auto d-none d-lg-block" style="" placeholder="Search">
                </div>
            </div>
            <button class="d-flex d-lg-none navbar-toggler" style="width: 38px; height: 38px;" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>
    </div>
    `
}