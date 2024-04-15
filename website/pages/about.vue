<script>
    import { ref } from "vue";
    import { VueComponent as AboutContent } from "../content/about_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";

    export default
    {
        components:
        {
            AboutContent,
            GlobalHeader,
            GlobalFooter,
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
            <h5 class="pt-3 pb-1">On this page</h5>
            <Outline :target="content"></Outline>
        </GlobalHeader>
    </header>
    <main>
        <div class="container d-flex">
            <div ref="content" class="about-content me-lg-4 flex-fill">
                <h1 class="display-2 ps-2 py-5 mb-4" style="font-weight: 350;">About</h1>
                <AboutContent></AboutContent>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="about-content pt-3 pb-1">On this page</h5>
                    <Outline :target="content"></Outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>