<script>
    import { VueComponent as ImprintContent } from "../content/imprint_content.md";
    import GlobalHeader from "../components/global_header.vue"
    import GlobalFooter from "../components/global_footer.vue"
    import ContentContainer from "../components/content_container.vue";

    export default
    {
        components:
        {
            ImprintContent,
            GlobalHeader,
            GlobalFooter,
            ContentContainer
        }
    };
</script>
<template>
    <header>
        <GlobalHeader></GlobalHeader>
    </header>
    <main class="flex-fill">
        <div class="headline-background shadow-sm">
            <div class="container">
                <div class="headline">
                    <h1>Imprint</h1>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="col-12 col-lg-10">
                <ContentContainer class="mt-4 content">
                    <ImprintContent></ImprintContent>
                </ContentContainer>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>