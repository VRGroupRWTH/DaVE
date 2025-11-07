<script>
    import { ref } from "vue";
    import { VueComponent as PrivacyPolicyContentEn } from "../content/privacy_policy_content_en.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import ContentContainer from "../components/content_container.vue";
    import Outline from "../components/outline.vue";

    export default
    {
        components:
        {
            PrivacyPolicyContentEn,
            GlobalHeader,
            GlobalFooter,
            ContentContainer,
            Outline
        },
        setup()
        {
            let content = ref(null);

            function on_language_change()
            {
                window.location = "/privacy_policy_de";
            }

            return {
                content,
                on_language_change
            }
        }
    };
</script>
<template>
    <header class="sticky-top">
        <GlobalHeader language="De" @on_language_change="on_language_change">
            <h5 class="outline-headline">On this page</h5>
            <Outline :target="content" depth_max="0"></Outline>
        </GlobalHeader>
    </header>
    <main class="flex-fill">
        <div class="headline-background shadow-sm">
            <div class="container">
                <div class="headline">
                    <h1 class="mb-3">Privacy Policy</h1>
                    <h5 class="ms-1">Pursuant to Article 13 GDPR</h5>
                </div>
            </div>
        </div>
        <div class="container d-flex">
            <div ref="content" class="me-lg-5 flex-fill" style="min-width: 0px;">
                <ContentContainer class="content">
                    <PrivacyPolicyContentEn></PrivacyPolicyContentEn>
                </ContentContainer>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 128px; z-index: 0;">
                    <h5 class="outline-headline">On this page</h5>
                    <Outline :target="content" depth_max="0"></Outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>