<script>
    import { ref } from "vue";
    import { VueComponent as GuideContent } from "../content/guide_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";

    export default
    {
        components:
        {
            GuideContent,
            "shared-header": GlobalHeader,
            "shared-footer": GlobalFooter,
            "outline": Outline
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
            <outline :target="content"></outline>
        </shared-header>
    </header>
    <main>
        <div class="container d-flex">
            <div ref="content" class="guide-content me-lg-4 flex-fill">
                <h1 class="display-2 ps-2 py-5 mb-4" style="font-weight: 350;">Guide</h1>
                <GuideContent></GuideContent>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="about-content pt-3 pb-1">On this page</h5>
                    <outline :target="content"></outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary">
        <shared-footer class="container"></shared-footer>
    </footer>
</template>