<script>
    import { ref } from "vue";
    import { VueComponent as AboutContent } from "../content/about_content.md";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import ContentContainer from "../components/content_container.vue";
    import Outline from "../components/outline.vue";

    export default
    {
        components:
        {
            AboutContent,
            GlobalHeader,
            GlobalFooter,
            ContentContainer,
            Outline
        },
        setup()
        {
            let content = ref(null);
            let contacts = ref(
            [
                { name: "Tim Gerrits", position: "Organization", e_mail: "gerrits@vis.rwth-aachen.de" },
                { name: "Christoph Garth", position: "Organization", e_mail: "garth@rptu.de" },
                { name: "Jens Koenen", position: "Web Development", e_mail: "koenen@vis.rwth-aachen.de" },
                { name: "Marvin Petersen", position: "Containers", e_mail: "m.petersen@rptu.de" }
            ]);

            return {
                content,
                contacts
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
                    <h1>About</h1>
                </div>
            </div>
        </div>
        <div class="container d-flex">
            <div ref="content" class="me-lg-4 flex-fill" style="min-width: 0px;">
                <ContentContainer class="content">
                    <AboutContent></AboutContent>
                </ContentContainer>
                <div class="px-4 mt-4">
                    <div class="row row-cols-1 row-cols-lg-2">
                        <div class="col" v-for="contact in contacts">
                            <div class="alert alert-light">
                                <div class="ms-4 my-1">
                                    <h5 class="text-body mb-0">{{ contact.name }}</h5>
                                    <div class="mb-2">{{ contact.position }}</div>
                                    <div class="d-flex align-items-center" style="position: relative;">
                                        <a class="stretched-link" :href="'mailto:' + contact.e_mail"><img class="me-2" src="../assets/icons/e_mail.svg" width="16px"></a>
                                        <div>{{ contact.e_mail }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
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