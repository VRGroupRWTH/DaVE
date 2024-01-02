import { ref } from "vue"

export default
{
    props: ["visualization"],
    setup(props)
    {
        let display_container = ref(null);

        return {
            display_container
        }
    },
    async mounted()
    {
        const fullScreenRenderer = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance(
        {
            container:  this.display_container
        });
        const renderer = fullScreenRenderer.getRenderer();
        const renderWindow = fullScreenRenderer.getRenderWindow();

        const sceneImporter = vtk.IO.Core.vtkHttpSceneLoader.newInstance(
        {
            renderer,
            fetchGzip: true
        });
        sceneImporter.setUrl("/database/direct_volume_rendering/scene/index.json");
        sceneImporter.onReady(() =>
        {
            renderWindow.render();
        });
    },
    template:
    `
    <div>
        <div ref="display_container" class="container my-5" style="height: 200px;"></div>
    </div>
    `
}