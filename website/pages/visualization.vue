<script>
    import { ref } from "vue";
    import VisualizationImages from "../components/visualization_images.vue";
    import VisualizationPreview from "../components/visualization_preview.vue";
    import VisualizationResources from "../components/visualization_resources.vue";
    import VisualizationWizard from "../components/visualization_wizard.vue";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import ContentContainer from "../components/content_container.vue";
    import Outline from "../components/outline.vue";
    import Tag from "../components/tag.vue";

    export default
    {
        components:
        {
            VisualizationImages,
            VisualizationPreview,
            VisualizationResources,
            VisualizationWizard,
            GlobalHeader,
            GlobalFooter,
            ContentContainer,
            Outline,
            Tag
        },
        setup()
        {
            let content = ref(null);
            let visualization = ref(
            {
                name: "",
                date: "",
                authors: [],
                tags: [],
                images: [],
                resources: [],
                datasets: [],
                templates: [],
                scene: "",
                description: ""
            });

            function on_visualization_tag_click(tag)
            {
                window.location = "/browser?tags=" + encodeURIComponent(tag.name + "+" + tag.type + "+" + tag.abbreviation);
            }

            return {
                content,
                visualization,
                on_visualization_tag_click
            }
        },
        async mounted()
        {
            const parameters = new URLSearchParams(window.location.search);

            const visualization_name = parameters.get("name");
            const visualization_request = 
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(
                {
                    visualization_name
                })
            }

            const response = await fetch("/api/fetch_visualization", visualization_request);

            if(response.ok)
            {
                this.visualization = await response.json();
            }
        }
    };
</script>

<template>
    <header class="sticky-top">
        <GlobalHeader>
            <h5 class="outline-headline">On this page</h5>
            <Outline :target="content" depth_max="1"></Outline>
        </GlobalHeader>
    </header>
    <main class="flex-fill">
        <div class="container d-flex">
            <div ref="content" class="me-lg-5 flex-fill" style="min-width: 0px;">
                <VisualizationImages :visualization="visualization" class="mt-4 mb-2 w-100" style="height: 350px"></VisualizationImages>
                <VisualizationPreview :visualization="visualization" class="mb-4"></VisualizationPreview>
                <div class="mb-4">
                    <h1 class="display-5" style="font-weight: 600;">{{ visualization.name }}</h1>
                    <div class="mb-2 fw-semibold">
                        <template v-for="(author, index) in visualization.authors">
                            <a :href="author.link" style="text-decoration: none; color: var(--bs-body-color)">{{ author.name }}</a>
                            <span v-if="index + 1 < visualization.authors.length" class="me-2">,</span>
                        </template>
                    </div>
                    <div class="d-flex ">
                        <Tag v-for="tag in visualization.tags" :tag="tag" class="me-1" @on_tag_click="on_visualization_tag_click"></Tag>
                    </div>
                </div>
                <ContentContainer>
                    <div class="my-4 content visualization-references" v-html="visualization.description"></div>
                </ContentContainer>
                <div id="Resources" outline_label="Resources" outline_indent="0" class="mb-4" style="scroll-margin-top: 80px;">
                    <div class="mt-4 content visualization-references">
                        <h2>
                            Resources
                            <a href="#Resources"> 
                                <img src='/assets/icons/link_45deg.svg' style='width: round(down, 1lh - 4px, 2px); position: absolute; top: 0.25lh;'>
                            </a>
                        </h2>
                    </div>
                    <VisualizationWizard :visualization="visualization"></VisualizationWizard>
                    <VisualizationResources :visualization="visualization"></VisualizationResources>
                </div>
                <div class="d-flex justify-content-center px-3">
                    <span class="text-secondary text-center">
                        If you have any suggestions, you can create an issue in the repository using this <a :href="'https://github.com/VRGroupRWTH/DaVE/issues/new?title=' + visualization.name + '&body=Please describe your issue as detailed as possible and change the name of the ticket accordingly. If you like, you can also assign labels to your issue.'">link.</a>
                    </span>
                </div>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="outline-headline">On this page</h5>
                    <Outline :target="content" depth_max="1"></Outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>