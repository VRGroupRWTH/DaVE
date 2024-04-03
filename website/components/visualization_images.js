export const VisualizationImages = 
{
    props: ["visualization"],
    setup()
    {
        return {
        }
    },
    template: 
    `
    <div class="carousel carousel-dark slide" v-bind="$attrs">
        <div class="carousel-inner w-100 h-100">
            <div v-for="(image, index) of visualization.images" class="carousel-item w-100 h-100" :class="((index == 0) ? 'active' : '')">
                <img :src="image" class="w-100 h-100" style="object-fit: contain;">
            </div>
            <button class="w-100 h-100 p-0" style="position: absolute; z-index: 1; border: 0; background: none; cursor: zoom-in;" type="button" data-bs-toggle="modal" data-bs-target="#visualization_images_modal"></button>
            <div class="w-100 h-100 d-flex align-items-center justify-content-between" style="position: absolute;">
                <button style="border: 0; background: none; z-index: 2;" type="button" data-bs-target="#visualization_preview_carousel" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon"></span>
                </button>
                <button style="border: 0; background: none; z-index: 2;" type="button" data-bs-target="#visualization_preview_carousel" data-bs-slide="next">
                    <span class="carousel-control-next-icon"></span>
                </button>
            </div>
        </div>
        <div class="carousel-indicators">
            <button v-for="(image, index) of visualization.images" :class="((index == 0) ? 'active' : '')" type="button" data-bs-target="#visualization_preview_carousel" :data-bs-slide-to="index"></button>
        </div>
    </div>
    <div id="visualization_images_modal" class="modal fade" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered modal-xl">
            <div class="modal-content">
                <div class="modal-body">
                    <button type="button" class="btn-close" data-bs-dismiss="visualization_images_modal"></button>
                    <div id="visualization_image_carousel" class="carousel carousel-dark slide w-100 h-100">
                        <div class="carousel-inner w-100 h-100">
                            <div v-for="(image, index) of visualization.images" class="carousel-item w-100 h-100" :class="((index == 0) ? 'active' : '')">
                                <img :src="image" class="w-100 h-100" style="object-fit: contain;">
                            </div>
                            <div class="w-100 h-100 d-flex align-items-center justify-content-between" style="position: absolute; z-index: 2002;">
                                <button style="border: 0; background: none; z-index: 2002;" type="button" data-bs-target="#visualization_image_carousel" data-bs-slide="prev">
                                    <span class="carousel-control-prev-icon"></span>
                                </button>
                                <button style="border: 0; background: none; z-index: 2002;" type="button" data-bs-target="#visualization_image_carousel" data-bs-slide="next">
                                    <span class="carousel-control-next-icon"></span>
                                </button>
                            </div>
                        </div>
                        <div class="carousel-indicators">
                            <button v-for="(image, index) of visualization.images" :class="((index == 0) ? 'active' : '')" type="button" data-bs-target="#visualization_image_carousel" :data-bs-slide-to="index"></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `
};