<script src="https://unpkg.com/vtk.js@29.3.0/vtk.js"></script>
<body id="app"></body>
<script type="module">
    import { createApp, ref } from "vue"
    import { VisualizationImages } from "components/visualization_images.js"
    import { VisualizationPreview } from "components/visualization_preview.js"
    import { VisualizationResources } from "components/visualization_resources.js"
    import { VisualizationWizard } from "components/visualization_wizard.js"
    import { SharedHeader } from "components/shared_header.js"
    import { SharedFooter } from "components/shared_footer.js"
    import { Outline } from "components/outline.js"
    import { Tag } from "components/tag.js"

    createApp(
    {
        components:
        {
            "visualization-images" : VisualizationImages,
            "visualization-preview": VisualizationPreview,
            "visualization-resources": VisualizationResources,
            "visualization-wizard": VisualizationWizard,
            "shared-header": SharedHeader,
            "shared-footer": SharedFooter,
            "outline": Outline,
            "tag": Tag
        },
        setup()
        {
            let content = ref(null);
            let visualization = ref(
            {
                name: "",
                date: "",
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
        },
        template:
        `
        <header class="sticky-top">
            <shared-header>
                <h5 class="mt-3 mb-2">Example</h5>
                <div class="d-flex justify-content-center mb-3 py-4 alert alert-light">
                    <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#visualization_wizard">
                        <div class="d-flex align-items-center">
                            <div>Download</div>
                            <img class="ms-2" src="symbols/download.svg">
                        </div>
                    </button>
                </div>
                <h5 class="mb-2">On this page</h5>
                <outline :target="content"></outline>
            </shared-header>
        </header>
        <main>
            <div class="container d-flex">
                <div ref="content" class="me-lg-4 flex-fill" style="min-width: 0px;">
                    <visualization-images :visualization="visualization" class="mt-4 mb-2 w-100" style="height: 350px"></visualization-images>
                    <visualization-preview :visualization="visualization" class="mb-4"></visualization-preview>
                    <div class="mb-4">
                        <h1 class="mb-2" style="font-size: 3rem">{{ visualization.name }}</h1>
                        <div class="d-flex">
                            <tag v-for="tag in visualization.tags" :tag="tag" class="me-1" @on_tag_click="on_visualization_tag_click"></tag>
                        </div>
                    </div>
                    <div class="mb-4 visualization-description" v-html="visualization.description"></div>
                    <visualization-resources class="mb-4" :visualization="visualization"></visualization-resources>
                    <visualization-wizard :visualization="visualization" id="visualization_wizard"></visualization-wizard>
                </div>
                <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                    <div class="sticky-top" style="top: 100px; z-index: 0;">
                        <h5 class="mb-2">Example</h5>
                        <div class="d-flex justify-content-center mb-3 py-4 alert alert-light">
                            <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#visualization_wizard">
                                <div class="d-flex align-items-center">
                                    <div>Download</div>
                                    <img class="ms-2" src="symbols/download.svg">
                                </div>
                            </button>
                        </div>
                        <h5 class="mb-2">On this page</h5>
                        <outline :target="content"></outline>
                    </div>
                </div>
            </div>
        </main>
        <footer class="bg-body-tertiary">
            <shared-footer class="container"></shared-footer>
        </footer>
        `
    }).mount("#app");
</script>