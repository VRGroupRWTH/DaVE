<script>
    import { ref } from "vue";

    export default
    {
        setup()
        {
            let header_search_query = ref("");
            let header_links = ref(
            [
                { link: "/browser", label: "Browser" },
                { link: "/guide", label: "Guide" },
                { link: "/about", label: "About" }
            ]);

            function is_active_link(link)
            {
                return window.location.pathname.endsWith(link);
            }

            function on_shared_header_search()
            {
                let search_url = "/browser";

                if(header_search_query.value.length > 0)
                {
                    search_url += "?query=" + header_search_query.value;
                }

                window.location = search_url;
            }

            return {
                header_links,
                header_search_query,
                is_active_link,
                on_shared_header_search
            };
        }
    };
</script>

<template>
    <nav class="navbar navbar-expand bg-dark shadow-sm" data-bs-theme="dark" v-bind="$attrs">
        <div class="container-lg d-flex align-items-center justify-content-between">
            <div class="navbar-nav align-items-center">
                <a class="navbar-brand" href="/">
                    <img src="../assets/icons/dave_logo_dark.svg" width="40px" height="40px">
                </a>
                <a class="nav-link" :class="is_active_link('/browser') ? 'active' : ''" href="/browser">Browser</a>
                <div class="dropdown">
                    <a class="nav-link dropdown-toggle" :class="(is_active_link('/guide') || is_active_link('/guide_use_dave') || is_active_link('/guide_extend_dave')) ? 'active' : ''" data-bs-toggle="dropdown">Guide</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="/guide">Overview</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="/guide_use_dave">How to use DaVE?</a></li>
                        <li><a class="dropdown-item" href="/guide_extend_dave">Extending DaVE</a></li>
                    </ul>
                </div>
                <a class="nav-link" :class="is_active_link('/about') ? 'active' : ''" href="/about">About</a>
            </div>
            <div>
                <input class="form-control shared-header-search-bar d-none d-lg-block" style="width: 250px;" type="text" placeholder="Search" v-model="header_search_query" @keydown.enter="on_shared_header_search">
                <button class="navbar-toggler d-flex align-items-center justify-content-between p-2 d-lg-none" style="border-color: #495057 !important; width: 40px; height: 40px;" type="button" data-bs-toggle="offcanvas" data-bs-target="#shared_header_offcanvas">
                    <span class="navbar-toggler-icon shared-header-toggle"></span>
                </button>
            </div>
        </div>
    </nav>
    <div id="shared_header_offcanvas" class="offcanvas offcanvas-end" style="" tabindex="-1">
        <div class="offcanvas-header p-4 pb-0">
            <input type="text" class="form-control guide-search-bar flex-fill" placeholder="Search" >
            <button type="button" class="btn-close btn-close ms-3" data-bs-dismiss="offcanvas"></button>
        </div>
        <div class="offcanvas-body pt-4 px-4">
            <slot></slot>
        </div>
    </div>
</template>