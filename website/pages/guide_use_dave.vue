<script>
    import { ref } from "vue";
    import { VueComponent as GuideUseDaveContent } from "../content/guide_use_dave_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import ContentContainer from "../components/content_container.vue";
    import Outline from "../components/outline.vue";

    export default
    {
        components:
        {
            GuideUseDaveContent,
            GlobalHeader,
            GlobalFooter,
            ContentContainer,
            Outline
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
        <GlobalHeader>
            <h5 class="outline-headline">On this page</h5>
            <outline :target="content" depth_max="1"></outline>
        </GlobalHeader>
    </header>
    <main class="flex-fill">
        <div class="headline-background shadow-sm">
            <div class="container">
                <div class="headline">
                    <h1>How to use DaVE?</h1>
                </div>
            </div>
        </div>
        <div class="container d-flex">
            <div ref="content" class="me-lg-5 flex-fill" style="min-width: 0px;">
                <ContentContainer class="content">
                    <GuideUseDaveContent></GuideUseDaveContent>
                </ContentContainer>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 128px; z-index: 0;">
                    <h5 class="outline-headline">On this page</h5>
                    <outline :target="content" depth_max="1"></outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>