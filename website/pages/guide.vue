<script>
    import { ref } from "vue";
    import { VueComponent as GuideContent } from "../content/guide_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";
    import OutlineContainer from "../components/outline_container.vue";

    export default
    {
        components:
        {
            GuideContent,
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
    <main>
        <div class="container d-flex">
            <div ref="content" class="guide-content me-lg-4 flex-fill" style="min-width: 0px;">
                <h1 class="display-1 ps-2 py-5 mb-4 fw-semibold">Guide</h1>
                <OutlineContainer>
                    <GuideContent></GuideContent>
                </OutlineContainer>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="about-content pt-3 pb-1">On this page</h5>
                    <outline :target="content" depth_max="1"></outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary">
        <shared-footer class="container mt-4"></shared-footer>
    </footer>
</template>