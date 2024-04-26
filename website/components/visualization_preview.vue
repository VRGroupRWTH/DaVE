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
                            // we don't do a linear scale, the proportions for
                            // a 700 pixel window differ from a 1400
                            const lastSize = helper.getLastSize();
                            const yAxisAdjust = (lastSize[1] / 700) ** 0.8;
                            const tickTextStyle = helper.getTickTextStyle();

                            // rebuild the text atlas
                            const textSizes = helper.updateTextureAtlas();

                            // now compute the boxSize and pixel offsets, different algorithm
                            // for horizonal versus vertical
                            helper.setTopTitle(false);

                            const boxSize = helper.getBoxSizeByReference();

                            // if vertical
                            if (helper.getLastAspectRatio() > 1.0)
                            {
                                helper.setAxisTitlePixelOffset(0.2 * tickTextStyle.fontSize);
                                helper.setTickLabelPixelOffset(0.3 * tickTextStyle.fontSize);
                                
                                boxSize[0] = (2.0 * (textSizes.titleHeight + helper.getAxisTitlePixelOffset() + textSizes.tickWidth + helper.getTickLabelPixelOffset() + 0.8 * tickTextStyle.fontSize)) / lastSize[0];
                                helper.setBoxPosition([0.99 - boxSize[0], -0.875/*-0.92*/]);

                                boxSize[1] = 1.75;//Math.max(1.2, Math.min(1.84 / yAxisAdjust, 1.84));
                            }
                            
                            else
                            {
                                // horizontal
                                helper.setAxisTitlePixelOffset(1.2 * tickTextStyle.fontSize);
                                helper.setTickLabelPixelOffset(0.1 * tickTextStyle.fontSize);

                                // total offset from top of bar (includes ticks)
                                const titleHeight = (2.0 * (0.8 * tickTextStyle.fontSize + textSizes.titleHeight + helper.getAxisTitlePixelOffset())) / lastSize[1];
                                const tickWidth = (2.0 * textSizes.tickWidth) / lastSize[0];
                                boxSize[0] = Math.min(1.9, Math.max(1.4, 1.4 * tickWidth * (helper.getTicks().length + 3)));
                                boxSize[1] = titleHeight;
                                helper.setBoxPosition([-0.5 * boxSize[0], -0.97]);
                            }

                            // recomute bar segments based on positioning
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