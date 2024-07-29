<script>
    import { ref } from "vue";
    import { VueComponent as PrivacyPolicyContent } from "../content/privacy_policy_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";
    import OutlineContainer from "../components/outline_container.vue";

    export default
    {
        components:
        {
            GlobalHeader,
            GlobalFooter,
            Outline,
            OutlineContainer,
            PrivacyPolicyContent
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
        <div class="container d-flex">
            <div ref="content" class="me-lg-4 flex-fill" style="min-width: 0px;">
                <div class="ps-2 py-5 mb-4">
                    <h1 class="mb-3 display-1 fw-semibold" style="font-size: min(5rem, max(1.625rem + 4.5vw, 3.5rem));">Privacy Policy</h1>
                    <h5 class="ms-1">Data Protection Policy as of February 2019</h5>
                </div>
                <OutlineContainer class="privacy-policy-content">
                    <PrivacyPolicyContent></PrivacyPolicyContent>
                </OutlineContainer>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="about-content pt-3 pb-1">On this page</h5>
                    <Outline :target="content" depth_max="0"></Outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>