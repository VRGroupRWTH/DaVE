import { ref, watch } from "vue"

export const VisualizationPreview =
{
    props: ["visualization"],
    setup(props)
    {
        let visualization_preview_state = ref("closed");
        let visualization_preview_valid = ref(false);

        let visualization_preview_container = ref(null);
        let visualization_preview_renderer = ref(null);
        let visualization_preview_full_screen_renderer = ref(null);

        if(props.visualization.scene != "")
        {
            visualization_preview_valid.value = true;
        }

        async function on_visualization_preview_open()
        {
            visualization_preview_state.value = "loading";
            visualization_preview_renderer.value = vtk.Rendering.Core.vtkRenderer.newInstance();

            const scene_importer = vtk.IO.Core.vtkHttpSceneLoader.newInstance(
            {
                renderer: visualization_preview_renderer.value,
                fetchGzip: true
            });
            scene_importer.setUrl(props.visualization.scene);
            scene_importer.onReady(() =>
            {
                visualization_preview_state.value = "open";
            });
        }

        function on_visualization_preview_close()
        {
            visualization_preview_state.value = "closed";

            if(visualization_preview_full_screen_renderer.value != null)
            {
                visualization_preview_full_screen_renderer.value.removeRenderer(visualization_preview_renderer.value);
                visualization_preview_full_screen_renderer.value.delete();

                visualization_preview_full_screen_renderer.value = null;
            }

            visualization_preview_renderer.value = null;
        }

        watch([visualization_preview_container], (old_state, new_state) =>
        {
            if(visualization_preview_container.value != null)
            {
                visualization_preview_full_screen_renderer.value = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance(
                {
                    container: visualization_preview_container.value
                });

                let render_window = visualization_preview_full_screen_renderer.value.getRenderWindow();
                render_window.addRenderer(visualization_preview_renderer.value);
                render_window.render();
            }
        });

        return {
            visualization_preview_container,
            visualization_preview_state,
            visualization_preview_valid,
            visualization_preview_renderer,
            visualization_preview_full_screen_renderer,
            on_visualization_preview_open,
            on_visualization_preview_close
        }
    },
    template:
    `
    <div>
        <!--<template v-if="visualization_preview_valid">
            <div v-if="visualization_preview_state == 'closed'" class="d-flex align-items-center justify-content-end" style="height: 40px">
                <button class="btn btn-primary" type="button" @click="on_visualization_preview_open">Preview</button>
            </div>
            <div v-else class="d-flex align-items-center justify-content-end" style="height: 40px">
                <button class="btn-close float-end" type="button" @click="on_visualization_preview_close"></button>
            </div>
        </template>-->
        <div style="width: 100%; height: 350px;">
            <div v-if="visualization_preview_state == 'closed'" id="visualization_preview_carousel" class="carousel carousel-dark slide w-100 h-100">
                <div class="carousel-inner w-100 h-100">
                    <div v-for="(image, index) of visualization.images" :class="'carousel-item w-100 h-100 ' + ((index == 0) ? 'active' : '')">
                        <img :src="image" class=" w-100 h-100" style="object-fit: contain;">
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
            <div v-else-if="visualization_preview_state == 'loading'" class="d-flex align-items-center justify-content-center w-100 h-100">
                <div class="spinner-border text-body-tertiary" role="status"></div>
                <span class="ms-2 text-body-tertiary fw-semibold fs-4">Loading preview</span>
            </div>
            <div v-else-if="visualization_preview_state == 'open'" ref="visualization_preview_container" class="w-100 h-100"></div>
        </div>
        <div class="alert alert-success d-flex justify-content-between align-items-center py-2 mt-2">
            <div>
                Interactive live demo available!
            </div>
            <div v-if="visualization_preview_state == 'closed'" class="d-flex align-items-center justify-content-end" style="height: 40px">
                <button class="btn btn-outline-success" type="button" @click="on_visualization_preview_open">Show</button>
            </div>
        </div>
    </div>
    `
}