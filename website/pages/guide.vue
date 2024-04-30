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
                <h1 class="display-1 ps-2 py-5 mb-4 fw-semibold">Guide</h1>
                <div class="card mb-4 shadow-sm title-underline" style="overflow: clip" outline_label="How to use DaVE?" outline_indent="0" id="How_to_use_DaVE">
                    <div class="row g-0">
                        <div class="col-md-3 d-flex align-items-center justify-content-center p-3 bg-body-tertiary">
                            <img src="/images/guide_how_to_extend_dave.svg" class="img-fluid rounded-start" alt="">
                        </div>
                        <div class="col-md-9">
                            <div class="card-body">
                                <h4 class="card-title fw-semibold">How to use DaVE?</h4>
                                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                <a href="/guide_use_dave" class="stretched-link"></a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card mb-4 shadow-sm title-underline" style="overflow: clip" outline_label="Extending DaVE" outline_indent="0" id="Extending_DaVE">
                    <div class="row g-0">
                        <div class="col-md-3 d-flex align-items-center justify-content-center p-3 bg-body-tertiary">
                            <img src="/images/guide_how_to_extend_dave.svg" class="img-fluid rounded-start" alt="">
                        </div>
                        <div class="col-md-9">
                        <div class="card-body">
                            <h4 class="card-title fw-semibold">Extending DaVE</h4>
                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
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
    .title-underline:hover h4
    {
        text-decoration: underline;
        text-decoration-thickness: 2px; 
    }
</style>