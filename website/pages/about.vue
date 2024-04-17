<script>
    import { ref } from "vue";
    import { VueComponent as AboutContent } from "../content/about_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";
    import OutlineContainer from "../components/outline_container.vue";

    export default
    {
        components:
        {
            AboutContent,
            GlobalHeader,
            GlobalFooter,
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
        <GlobalHeader>
            <h5 class="pt-3 pb-1">On this page</h5>
            <Outline :target="content" depth_max="1"></Outline>
        </GlobalHeader>
    </header>
    <main>
        <div class="container d-flex">
            <div ref="content" class="about-content me-lg-4 flex-fill" style="min-width: 0px;">
                <h1 class="display-2 ps-2 py-5 mb-4 fw-semibold">About</h1>
                <OutlineContainer>
                    <AboutContent></AboutContent>
                </OutlineContainer>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="about-content pt-3 pb-1">On this page</h5>
                    <Outline :target="content" depth_max="1"></Outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary">
        <GlobalFooter class="container mt-4"></GlobalFooter>
    </footer>
</template>