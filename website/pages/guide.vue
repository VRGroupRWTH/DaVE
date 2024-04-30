<script>
    import { ref } from "vue";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";
    import OutlineContainer from "../components/outline_container.vue";

    export default
    {
        components:
        {
            "shared-header": GlobalHeader,
            "shared-footer": GlobalFooter,
            Outline,
            OutlineContainer
        },
        setup()
        {
            let content = ref(null);

            return {
                content
            }
        }
    };
</script>

<template>
    <header class="sticky-top">
        <shared-header>
            <h5 class="pt-3 pb-1">On this page</h5>
            <outline :target="content" depth_max="1"></outline>
        </shared-header>
    </header>
    <main class="flex-fill">
        <div class="container d-flex">
            <div ref="content" class="me-lg-4 flex-fill" style="min-width: 0px;">
                <h1 class="display-1 ps-2 py-5 mb-4 fw-semibold" style="font-size: min(5rem, max(1.625rem + 4.5vw, 3.5rem));">Guide</h1>
                <div class="card mb-4 shadow-sm title-underline" style="overflow: clip;" outline_label="How to use DaVE?" outline_indent="0" id="How_to_use_DaVE">
                    <div class="row g-0">
                        <div class="col-md-2 card-border bg-body-tertiary">
                            <img src="/images/guide_how_to_use_dave.svg" class="img-fluid h-100" alt="" style="width: 100%; padding: 16px; max-height: 275px">
                        </div>
                        <div class="col-md-10">
                            <div class="card-body p-4">
                                <h2 class="card-title fw-semibold">How to use DaVE?</h2>
                                <p class="card-text">
                                    Learn how you can narrow down your search results by using tags, and get more information on how the containers provided by DaVE are built up.
                                </p>
                                <a href="/guide_use_dave" class="stretched-link"></a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card mb-4 shadow-sm title-underline" style="overflow: clip;" outline_label="Extending DaVE" outline_indent="0" id="Extending_DaVE">
                    <div class="row g-0">
                        <div class="col-md-2 card-border bg-body-tertiary" style="position: relative">
                            <img src="/images/guide_how_to_extend_dave.svg" class="img-fluid" alt="" style="object-fit: cover; width:100%; object-position: top left; max-height: 275px; height: 100%; filter: brightness(98%)">
                        </div>
                        <div class="col-md-10">
                        <div class="card-body p-4">
                            <h2 class="card-title fw-semibold">Extending DaVE</h2>
                            <p class="card-text">
                                Create your own examples and become a contributor by exploring how the database of DaVE is structured and by getting an introduction on how you can derive your own example from already existing ones.
                            </p>
                            <a href="/guide_extend_dave" class="stretched-link"></a>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="guide-content pt-3 pb-1">On this page</h5>
                    <outline :target="content" depth_max="1"></outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <shared-footer class="container"></shared-footer>
    </footer>
</template>

<style scoped>
    .title-underline:hover h2
    {
        text-decoration: underline;
        text-decoration-thickness: 2px; 
    }
    
    .card-border
    {
        border-bottom: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color) !important;
    }

    @media (min-width: 768px)
    {
        .card-border
        {
            border-right: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color) !important;
            border-bottom: 0px !important;
        }
    }
</style>