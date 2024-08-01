<script>
    import { ref } from "vue";
    import { VueComponent as PrivacyPolicyContent } from "../content/privacy_policy_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import ContentContainer from "../components/content_container.vue";
    import Outline from "../components/outline.vue";

    export default
    {
        components:
        {
            PrivacyPolicyContent,
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
            <h5 class="pt-3 pb-1">On this page</h5>
            <Outline :target="content" depth_max="0"></Outline>
        </GlobalHeader>
    </header>
    <main class="flex-fill">
        <div class="headline-background shadow-sm">
            <div class="container">
                <div class="headline">
                    <h1 class="mb-3">Privacy Policy</h1>
                    <h5 class="ms-1">Data Protection Policy as of February 2019</h5>
                </div>
            </div>
        </div>
        <div class="container d-flex">
            <div ref="content" class="me-lg-4 flex-fill" style="min-width: 0px;">
                <ContentContainer class="content">
                    <PrivacyPolicyContent></PrivacyPolicyContent>
                </ContentContainer>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 128px; z-index: 0;">
                    <h5 class="about-content pb-1">On this page</h5>
                    <Outline :target="content" depth_max="0"></Outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>