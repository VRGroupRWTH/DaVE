<script>
    import { ref } from "vue";
    import { VueComponent as GuideExtendDaveContent } from "../content/guide_extend_dave_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";
    import OutlineContainer from "../components/outline_container.vue";

    export default
    {
        components:
        {
            GuideExtendDaveContent,
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
                <h1 class="display-1 ps-2 py-5 mb-4 fw-semibold">Extending DaVE</h1>
                <OutlineContainer class="guide-content">
                    <GuideExtendDaveContent></GuideExtendDaveContent>
                </OutlineContainer>
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