<script>
    export default
    {
        props: ["visualization"]
    };
</script>

<template>
    <div id="visualization_images_carousel" class="carousel carousel-dark slide" v-bind="$attrs">
        <div class="carousel-inner w-100 h-100">
            <div v-for="(image, index) of visualization.images" class="carousel-item w-100 h-100" :class="((index == 0) ? 'active' : '')">
                <img :src="image" class="w-100 h-100" style="object-fit: contain;">
            </div>
            <div class="w-100 h-100 d-flex align-items-start justify-content-end px-2 py-2" style="position: absolute;">
                <button style="border: 0; background: none; z-index: 1;" type="button" data-bs-toggle="modal" data-bs-target="#visualization_images_modal">
                    <img style="width: 20px; height: 20px;" src="../assets/icons/zoom_in.svg">
                </button>
            </div>
            <div class="w-100 h-100 d-flex align-items-center justify-content-between" style="position: absolute;">
                <button style="border: 0; background: none; z-index: 2;" type="button" data-bs-target="#visualization_images_carousel" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon"></span>
                </button>
                <button style="border: 0; background: none; z-index: 2;" type="button" data-bs-target="#visualization_images_carousel" data-bs-slide="next">
                    <span class="carousel-control-next-icon"></span>
                </button>
            </div>
        </div>
        <div class="carousel-indicators">
            <button v-for="(image, index) of visualization.images" :class="((index == 0) ? 'active' : '')" type="button" data-bs-target="#visualization_images_carousel" :data-bs-slide-to="index"></button>
        </div>
    </div>
    <div id="visualization_images_modal" class="modal fade" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered modal-xl">
            <div class="modal-content">
                <div class="modal-body" style="height: 75vh">
                    <button class="btn-close" style="position: absolute; top: 1.5rem; right: 1.5rem; z-index: 1;" type="button" data-bs-dismiss="modal"></button>
                    <div id="visualization_images_modal_carousel" class="carousel carousel-dark slide w-100 h-100">
                        <div class="carousel-inner w-100 h-100">
                            <div v-for="(image, index) of visualization.images" class="carousel-item w-100 h-100" :class="((index == 0) ? 'active' : '')">
                                <img :src="image" class="w-100 h-100" style="object-fit: contain;">
                            </div>
                            <div class="w-100 h-100 d-flex align-items-center justify-content-between" style="position: absolute;">
                                <button style="border: 0; background: none; z-index: 2;" type="button" data-bs-target="#visualization_images_modal_carousel" data-bs-slide="prev">
                                    <span class="carousel-control-prev-icon"></span>
                                </button>
                                <button style="border: 0; background: none; z-index: 2;" type="button" data-bs-target="#visualization_images_modal_carousel" data-bs-slide="next">
                                    <span class="carousel-control-next-icon"></span>
                                </button>
                            </div>
                        </div>
                        <div class="carousel-indicators">
                            <button v-for="(image, index) of visualization.images" :class="((index == 0) ? 'active' : '')" type="button" data-bs-target="#visualization_images_modal_carousel" :data-bs-slide-to="index"></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>