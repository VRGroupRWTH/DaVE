<script>
    import { ref, watch, computed } from "vue";

    import "@kitware/vtk.js/IO/Core/DataAccessHelper/HttpDataAccessHelper";
    import '@kitware/vtk.js/Rendering/Profiles/Geometry';
    import '@kitware/vtk.js/Rendering/Profiles/Volume';
    
    import vtkFullScreenRenderWindow from "@kitware/vtk.js/Rendering/Misc/FullScreenRenderWindow";
    import vtkRenderer from "@kitware/vtk.js/Rendering/Core/Renderer";
    import vtkHttpSceneLoader from "@kitware/vtk.js/IO/Core/HttpSceneLoader";
    import vtkScalarBarActor from '@kitware/vtk.js/Rendering/Core/ScalarBarActor';
    
    export default
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
                visualization_preview_renderer.value = vtkRenderer.newInstance();
                visualization_preview_scene_count = 0;

                const scene_importer = vtkHttpSceneLoader.newInstance(
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
                    visualization_preview_full_screen_renderer.value = vtkFullScreenRenderWindow.newInstance(
                    {
                        container: visualization_preview_container.value,
                        rootContainer: visualization_preview_modal.value
                    });

                    for(const actor of visualization_preview_renderer.value.getActors())
                    {
                        const mapper = actor.getMapper();

                        if(mapper.getColorByArrayName() == "")
                        {
                            continue;
                        }

                        const axis_style = 
                        {
                            fontColor: "black",
                            fontFamily: "Segoe UI",
                            fontSize: "16",
                            fontStyle: "600"
                        };

                        const tick_style = 
                        {
                            fontColor: "black",
                            fontFamily: "Segoe UI",
                            fontSize: "16",
                            fontStyle: "500"
                        };

                        const bar_layout = (helper) =>
                        {
                            const textSizes = helper.updateTextureAtlas();                      
                            const lastSize = helper.getLastSize();
                            const container_width = lastSize[0];
                            const container_height = lastSize[1];

                            helper.getBarActor().setVisibility(true);
                            helper.getTmActor().setVisibility(true);

                            if (helper.getLastAspectRatio() > 1.0)
                            {
                                const bar_size = 16;
                                const bar_min_height = 100;
                                const bar_margin_top = 48;
                                const bar_margin_bottom = 48;
                                const bar_margin_right = 8;
                                const tick_margin = 4;
                                const title_margin = 8;

                                let box_width = textSizes.titleHeight + textSizes.tickWidth + title_margin + tick_margin + bar_size;
                                let box_height = container_height - bar_margin_top - bar_margin_bottom;

                                if(box_height < bar_min_height)
                                {
                                    helper.getBarActor().setVisibility(false);
                                    helper.getTmActor().setVisibility(false);

                                    return;
                                }

                                let box_left =  container_width - box_width - bar_margin_right;
                                let box_bottom = bar_margin_bottom;

                                let box_size = helper.getBoxSizeByReference();
                                box_size[0] = (box_width / container_width) * 2.0;
                                box_size[1] = (box_height / container_height) * 2.0;

                                let box_position = [0, 0];
                                box_position[0] = (box_left / container_width) * 2.0 - 1.0;
                                box_position[1] = (box_bottom / container_height) * 2.0 - 1.0;
                                helper.setBoxPosition(box_position);

                                helper.setAxisTitlePixelOffset(title_margin);
                                helper.setTickLabelPixelOffset(tick_margin);
                            }
                            
                            else
                            {
                                const bar_size = 16;
                                const bar_margin_left = 48;
                                const bar_margin_right = 48;
                                const bar_margin_bottom = 8;
                                const tick_margin = 4;
                                const title_margin = 4;

                                let box_width = container_width - bar_margin_left - bar_margin_right;
                                let box_height = textSizes.titleHeight + textSizes.tickHeight + title_margin + tick_margin + bar_size;

                                let box_left = bar_margin_left;
                                let box_bottom = bar_margin_bottom;

                                let box_size = helper.getBoxSizeByReference();
                                box_size[0] = (box_width / container_width) * 2.0;
                                box_size[1] = (box_height / container_height) * 2.0;

                                let box_position = [0, 0];
                                box_position[0] = (box_left / container_width) * 2.0 - 1.0;
                                box_position[1] = (box_bottom / container_height) * 2.0 - 1.0;
                                helper.setBoxPosition(box_position);

                                const title_offset = tick_margin + textSizes.tickHeight + title_margin;

                                helper.setAxisTitlePixelOffset(title_offset);
                                helper.setTickLabelPixelOffset(tick_margin);
                            }

                            helper.setTopTitle(false);
                            helper.recomputeBarSegments(textSizes);
                        };

                        let bar = vtkScalarBarActor.newInstance();
                        bar.setScalarsToColors(mapper.getLookupTable());
                        bar.setAxisLabel(mapper.getColorByArrayName());
                        bar.setAxisTextStyle(axis_style);
                        bar.setTickTextStyle(tick_style);
                        bar.setDrawNanAnnotation(false);
                        bar.setAutoLayout(bar_layout);
                        bar.setVisibility(true);

                        visualization_preview_renderer.value.addActor(bar);

                        break;
                    }

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
        }
    };
</script>

<template>
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
</template>