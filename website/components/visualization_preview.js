import { ref } from "vue"

export default
{
    props: ["visualization"],
    setup(props)
    {
        let visualization_preview_container = ref(null);
        let visualization_preview_state = ref("closed");
        let visualization_preview_valid = ref(false);

        if(props.visualization.scene != "")
        {
            visualization_preview_valid.value = true;
        }

        async function on_visualization_preview_open()
        {
            visualization_preview_state.value = "loading";

            const full_screen_renderer = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance(
            {
                container: visualization_preview_container.value
            });
            const renderer = full_screen_renderer.getRenderer();
            const render_window = full_screen_renderer.getRenderWindow();
    
            const scene_importer = vtk.IO.Core.vtkHttpSceneLoader.newInstance(
            {
                renderer,
                fetchGzip: true
            });
            scene_importer.setUrl(props.visualization.scene);
            scene_importer.onReady(() =>
            {
                render_window.render();

                visualization_preview_state.value = "open";
            });
        }

        function on_visualization_preview_close()
        {
            visualization_preview_state.value = "closed";
        }

        return {
            visualization_preview_container,
            visualization_preview_state,
            visualization_preview_valid,
            on_visualization_preview_open,
            on_visualization_preview_close
        }
    },
    template:
    `
    <div>
        <div v-if="visualization_preview_valid && visualization_preview_state == 'closed'" class="d-flex align-items-center justify-content-end" style="height: 40px">
            <button class="btn btn-primary" type="button" @click="on_visualization_preview_open">Preview</button>
        </div>
        <div v-else class="d-flex align-items-center justify-content-end" style="height: 40px">
            <button class="btn-close float-end" type="button" @click="on_visualization_preview_close"></button>
        </div>
        <div v-if="visualization_preview_state == 'closed'">
            <div id="visualization_preview_carousel" class="carousel carousel-dark slide">
                <div class="carousel-inner">
                    <div v-for="(image, index) of visualization.images" :class="'carousel-item ' + ((index == 0) ? 'active' : '')">
                        <img :src="image" style="object-fit: contain; width: 100%; height: 300px;">
                    </div>
                    <div class="w-100 h-100 d-flex align-items-center justify-content-between" style="position: absolute; z-index: 1;">
                        <button style="border: 0; background: none;" type="button" data-bs-target="#visualization_preview_carousel" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon"></span>
                        </button>
                        <button style="border: 0; background: none;" type="button" data-bs-target="#visualization_preview_carousel" data-bs-slide="next">
                            <span class="carousel-control-next-icon"></span>
                        </button>
                    </div>
                </div>
                <div class="carousel-indicators">
                    <button v-for="(image, index) of visualization.images" :class="((index == 0) ? 'active' : '')" type="button" data-bs-target="#visualization_preview_carousel" :data-bs-slide-to="index"></button>
                </div>
            </div>
        </div>
        <div v-else-if="visualization_preview_state == 'loading'" class="d-flex align-items-center justify-content-center" style="width: 100%; height: 300px;">
            <div class="spinner-border text-body-tertiary" role="status"></div>
            <span class="ms-2 text-body-tertiary fw-semibold fs-4">Loading preview</span>
        </div>
        <div ref="visualization_preview_container" :style="'width: 100%; height: 300px; ' + ((visualization_preview_state == 'open') ? '' : 'display: none;')"></div>
    </div>
    `
}