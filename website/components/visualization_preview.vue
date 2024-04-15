import { ref, watch, computed } from "vue"

export const VisualizationPreview =
{
    props: ["visualization"],
    setup(props)
    {
        let visualization_preview_modal = ref(null);
        let visualization_preview_state = ref("closed");
        let visualization_preview_valid = computed(() =>
        {
            return props.visualization.scene != "";
        });

        let visualization_preview_container = ref(null);
        let visualization_preview_renderer = ref(null);
        let visualization_preview_full_screen_renderer = ref(null);
        let visualization_preview_scene_count = 0;

        async function on_visualization_preview_open()
        {
            visualization_preview_state.value = "loading";
            visualization_preview_renderer.value = vtk.Rendering.Core.vtkRenderer.newInstance();
            visualization_preview_scene_count = 0;

            const scene_importer = vtk.IO.Core.vtkHttpSceneLoader.newInstance(
            {
                renderer: visualization_preview_renderer.value,
                fetchGzip: true
            });
            scene_importer.setUrl(props.visualization.scene);
            scene_importer.onReady(() =>
            {
                const metadata = scene_importer.getMetadata();
                visualization_preview_scene_count++;

                if(visualization_preview_scene_count >= metadata.scene.length)
                {
                    visualization_preview_state.value = "open";
                }
            });
        }

        function on_visualization_preview_close()
        {
            visualization_preview_state.value = "closed";

            if(visualization_preview_full_screen_renderer.value != null)
            {
                let render_window = visualization_preview_full_screen_renderer.value.getRenderWindow();
                render_window.removeRenderer(visualization_preview_renderer.value);

                visualization_preview_full_screen_renderer.value.delete();
                visualization_preview_full_screen_renderer.value = null;
            }

            visualization_preview_renderer.value = null;
        }

        watch([visualization_preview_modal], (old_state, new_state) =>
        {
            if(visualization_preview_modal.value != null)
            {
                visualization_preview_modal.value.addEventListener('shown.bs.modal', event =>
                {
                    on_visualization_preview_open();
                });

                visualization_preview_modal.value.addEventListener('hidden.bs.modal', event =>
                {
                    on_visualization_preview_close();
                });
            }
        });

        watch([visualization_preview_container, visualization_preview_modal], (old_state, new_state) =>
        {
            if(visualization_preview_container.value != null)
            {
                visualization_preview_full_screen_renderer.value = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance(
                {
                    container: visualization_preview_container.value,
                    rootContainer: visualization_preview_modal.value
                });

                visualization_preview_renderer.value.resetCamera();

                let render_window = visualization_preview_full_screen_renderer.value.getRenderWindow();
                render_window.addRenderer(visualization_preview_renderer.value);
                render_window.render();
                
            }
        });

        return {
            visualization_preview_modal,
            visualization_preview_state,
            visualization_preview_valid,
            visualization_preview_container,
            visualization_preview_renderer,
            visualization_preview_full_screen_renderer
        }
    },
    template:
    `
    <div v-bind="$attrs">
        <div v-if="visualization_preview_valid" class="alert alert-success d-flex justify-content-between align-items-center py-2">
            <div>Interactive preview available!</div>
            <button class="btn btn-outline-success" type="button" data-bs-toggle="modal" data-bs-target="#visualization_preview_modal">Show</button>
        </div>
    </div>
    <div id="visualization_preview_modal" ref="visualization_preview_modal" class="modal fade" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered modal-xl">
            <div class="modal-content">
                <div class="modal-body" style="height: 75vh;">
                    <button class="btn-close" style="position: absolute; top: 1.5rem; right: 1.5rem; z-index: 1;" type="button" data-bs-dismiss="modal"></button>
                    <div v-if="visualization_preview_state == 'loading'" class="d-flex align-items-center justify-content-center w-100 h-100">
                        <div class="spinner-border text-body-tertiary" role="status"></div>
                        <span class="ms-2 text-body-tertiary fw-semibold fs-4">Loading preview</span>
                    </div>
                    <div v-else-if="visualization_preview_state == 'open'" ref="visualization_preview_container" class="w-100 h-100"></div>
                </div>
            </div>
        </div>
    </div>
    `
}