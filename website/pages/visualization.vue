<script>
    import { ref } from "vue";
    import VisualizationImages from "../components/visualization_images.vue";
    import VisualizationPreview from "../components/visualization_preview.vue";
    import VisualizationResources from "../components/visualization_resources.vue";
    import VisualizationWizard from "../components/visualization_wizard.vue";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";
    import OutlineContainer from "../components/outline_container.vue";
    import Tag from "../components/tag.vue";

    export default
    {
        components:
        {
            "visualization-images" : VisualizationImages,
            "visualization-preview": VisualizationPreview,
            "visualization-resources": VisualizationResources,
            "visualization-wizard": VisualizationWizard,
            "shared-header": GlobalHeader,
            "shared-footer": GlobalFooter,
            "outline": Outline,
            "outline-container": OutlineContainer,
            "tag": Tag
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
        <shared-header>
            <h5 class="mt-3 mb-2">Example</h5>
            <div class="d-flex justify-content-center mb-3 py-4 alert alert-light">
                <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#visualization_wizard">
                    <div class="d-flex align-items-center">
                        <div>Download</div>
                        <img class="ms-2" src="../assets/icons/download.svg">
                    </div>
                </button>
            </div>
            <h5 class="mb-2">On this page</h5>
            <outline :target="content" depth_max="1"></outline>
        </shared-header>
    </header>
    <main class="flex-fill">
        <div class="container d-flex">
            <div ref="content" class="me-lg-4 flex-fill" style="min-width: 0px;">
                <visualization-images :visualization="visualization" class="mt-4 mb-2 w-100" style="height: 350px"></visualization-images>
                <visualization-preview :visualization="visualization" class="mb-4"></visualization-preview>
                <div class="mb-4">
                    <h1 class="mb-0" style="font-size: 3rem">{{ visualization.name }}</h1>
                    <div class="mb-2 ms-1 fw-semibold">
                        <template v-for="(author, index) in visualization.authors">
                            <a :href="author.link" style="text-decoration: none; color: var(--bs-body-color)">{{ author.name }}</a>
                            <span v-if="index + 1 < visualization.authors.length" class="me-2">,</span>
                        </template>
                    </div>
                    <div class="d-flex ms-1">
                        <tag v-for="tag in visualization.tags" :tag="tag" class="me-1" @on_tag_click="on_visualization_tag_click"></tag>
                    </div>
                </div>
                <outline-container>
                    <div class="mb-4 visualization-description" v-html="visualization.description"></div>
                </outline-container>
                <visualization-resources class="mb-4" :visualization="visualization"></visualization-resources>
                <div class="d-flex justify-content-center">
                    <span class="text-secondary">
                        If you have any suggestions, you can creation an issue in the repository using this <a href="/anonymity">link.</a>
                    </span>
                </div>
                <visualization-wizard :visualization="visualization" id="visualization_wizard"></visualization-wizard>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="mb-2">Example</h5>
                    <div class="d-flex justify-content-center mb-3 py-4 alert alert-light">
                        <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#visualization_wizard">
                            <div class="d-flex align-items-center">
                                <div>Download</div>
                                <img class="ms-2" src="../assets/icons/download.svg">
                            </div>
                        </button>
                    </div>
                    <h5 class="mb-2">On this page</h5>
                    <outline :target="content" depth_max="1"></outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <shared-footer class="container"></shared-footer>
    </footer>
</template>