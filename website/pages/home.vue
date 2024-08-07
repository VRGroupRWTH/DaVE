<script>
    import { ref } from "vue"
    import HomeSearchBar from "../components/home_search_bar.vue"
    import GlobalFooter from "../components/global_footer.vue"

    export default
    {
        components:
        {
            HomeSearchBar,
            GlobalFooter
        },
        setup()
        {
            const video_consent = ref(false);

            function on_search_bar_search(query, tags)
            {
                let search_url = "/browser";

                if(query.length > 0 || tags.length > 0)
                {
                    search_url += "?";
                }

                if(query.length > 0)
                {
                    search_url += "query=" + encodeURIComponent(query);
                }

                if(query.length > 0 && tags.length > 0)
                {
                    search_url += "&";
                }

                if(tags.length > 0)
                {
                    let search_tag_url = tags[0].name + "+" + tags[0].type + "+" + tags[0].abbreviation;

                    for(let index = 1; index < tags.length; index++)
                    {
                        search_tag_url += "+" + tags[index].name + "+" + tags[index].type + "+" + tags[index].abbreviation;
                    }

                    search_url += "tags=" + encodeURIComponent(search_tag_url);
                }

                window.location = search_url;
            }

            function on_video_consent_accept(event)
            {
                video_consent.value = true;
            }

            return {
                video_consent,
                on_search_bar_search,
                on_video_consent_accept
            }
        }
    };
</script>

<template>
    <header>
        <div class="home-background-image" style="height: 80vh; min-height: 600px;">
            <div class="d-flex flex-column align-items-center justify-content-center w-100 h-100" style="padding-top: 50px; padding-bottom: 120px;">
                <div class="d-flex justify-content-center align-items-center w-100 p-3" style="min-height: 0px; padding-top: 0px !important; padding-bottom: 150px !important;">
                    <img src="/images/home_logo.svg" class="d-none d-sm-block" style="width: 100%; max-width: 750px">
                    <img src="/images/home_logo_small.svg" class="d-sm-none" style="width: 100%; max-width: 300px">
                </div>
                <HomeSearchBar class="container-sm" @on_search_bar_search="on_search_bar_search" style="padding-bottom: 30px;"></HomeSearchBar>
                <a class="btn btn-primary shadow" href="/browser">
                    Explore all Visualizations
                </a>
            </div>
        </div>
    </header>
    <main class="bg-body-tertiary card-container-padding flex-fill">
        <div class="container">
            <div class="card text-bg-dark shadow-sm rounded-3 card-margin">
                <div class="card-body card-padding">
                    <div class="row card-gutter">
                        <div class="col-12 col-lg-8">
                            <h1 class="card-title display-5 fw-semibold mb-4">What is DaVE?</h1>
                            <p class="card-text" style="font-size: 1.125rem;">                                                                
                                DaVE serves as a centralized repository where users can find and discover visualization examples tailored to their specific needs through a simple search.
                                Our database is designed to be user-friendly, offering seamless integration into existing workflows using adaptable containers.
                                Whether you're exploring cutting-edge visualizations for data or seeking practical solutions to enhance your simulations, DaVE seeks to find helpful resources for you.
                            </p>
                        </div>
                        <div class="col-12 col-lg-4 d-flex align-items-center justify-content-center flex-column">
                            <a href="https://github.com/VRGroupRWTH/DaVE" class="mb-2 pt-lg-4">
                                <img src="../assets/icons/github.svg" width="72px">
                            </a>
                            <h5>Check it out on GitHub</h5>
                            <!--<p style="font-size: 1.125rem;">
                                Check it out on GitHub
                            </p>-->
                        </div>
                    </div>
                </div>
            </div>
            <!--<div class="row g-3 g-md-5 mb-3 mb-md-5">
                <div class="col-12 col-xl-4">
                    <div class="card shadow-sm rounded-3 h-100">
                        <div class="card-body" style="padding: 2rem;">
                            <h2 class="card-title fw-semibold">Browser</h2>
                            <p class="card-text">
                                Use the browser to freely explore what DaVE has to offer.
                                Just scroll thorugh the library of visualization examples and use filters to find a technique specific to your use case.
                            </p>
                        </div>
                        <div class="p-3">
                            <a class="btn btn-primary float-end" href="/browser">Show</a>
                        </div>
                    </div>
                </div>
                <div class="col-12 col-md-6 col-xl-4">
                    <div class="card shadow-sm rounded-3 h-100">
                        <div class="card-body" style="padding: 2rem;">
                            <h2 class="card-title fw-semibold">Guide</h2>
                            <p class="card-text">
                                Get more information on how to use DaVE in the Guide. 
                                Learn how DaVE is build up and how you can contribute to DaVE by creating your own examples.
                                It's easy, give it a try.
                            </p>
                        </div>
                        <div class="p-3">
                            <a class="btn btn-primary float-end" href="/guide">Show</a>
                        </div>
                    </div>
                </div>
                <div class="col-12 col-md-6 col-xl-4">
                    <div class="card shadow-sm rounded-3 h-100">
                        <div class="card-body" style="padding: 2rem;">
                            <h2 class="card-title fw-semibold">About</h2>
                            <p class="card-text">
                                Learn more about the project or get in touch with the creators if you have a question, don't know how to contribute or simply found a bug.
                            </p>
                        </div>
                        <div class="p-3">
                            <a class="btn btn-primary float-end" href="/about">Show</a>
                        </div>
                    </div>
                </div>
            </div>-->
            <div class="card shadow-sm rounded-3 card-margin">
                <div class="card-body card-padding">
                    <div class="row align-items-center card-gutter">
                        <div class="card-40 col-12 d-flex justify-content-center">
                            <div class="card-video flex-fill shadow" style="position: relative;"> 
                                <template v-if="video_consent">
                                    <iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/T0VihZcaOxo?si=XvXOCvNjMIVsImpo&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                                </template>
                                <template v-else>
                                    <img src="/images/home_how_to_use_dave_thumbnail.png" class="w-100 h-100">
                                    <div class="d-flex align-items-center justify-content-center card-video-play">
                                        <img src="/assets/icons/play.svg" width="48px" data-bs-toggle="modal" data-bs-target="#home_video_consent">
                                    </div>
                                </template>
                            </div>
                            <!--<div class="shadow d-flex d-none d-sm-block d-md-none">
                                <iframe width="432" height="243" src="https://www.youtube-nocookie.com/embed/rNVD_P3OUAE?si=kCOC0gW8Ub-BPamf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                            </div>
                            <div class="shadow d-flex d-sm-none">
                                <iframe width="336" height="189" src="https://www.youtube-nocookie.com/embed/rNVD_P3OUAE?si=kCOC0gW8Ub-BPamf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                            </div>-->
                        </div>
                        <div class="card-60 col-12">
                            <h1 class="card-title mb-4 display-5 fw-semibold">How to use DaVE?</h1>
                            <p class="card-text mb-4" style="font-size: 1.125rem;">
                                Get more information on how to use DaVE in the Guide. 
                                Learn how DaVE is build up and how you can contribute to DaVE by creating your own examples.
                                It's easy, give it a try.
                            </p>
                            <a class="btn btn-primary float-end float-sm-start" href="/guide_use_dave">Read more</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card shadow-sm rounded-3 card-margin">
                <div class="card-body card-padding">
                    <div class="row align-items-center card-gutter">
                        <div class="col-12 card-60 order-1 order-lg-1">
                            <h1 class="card-title mb-4 display-5 fw-semibold">Become a Contributor</h1>
                            <p class="card-text mb-4" style="font-size: 1.125rem;">
                                Join us in growing DaVE by becoming a contributor!
                                You can contribute no matter how experienced you are in making visualizations.
                                It's as easy as adding a folder to the database to create your own example.
                            </p>
                            <a class="btn btn-primary float-end float-sm-none" href="/guide_extend_dave">Read more</a>
                        </div>
                        <div class="col-12 card-40 d-flex justify-content-center order-0 order-lg-1">
                            <img src="/images/home_contribution.svg" class="flex-fill p-4 p-lg-0" style="aspect-ratio: 16 / 9;">
                        </div>
                    </div>
                </div>
            </div>
            <div class="card shadow-sm rounded-3">
                <div class="card-body card-padding">
                    <div class="row row-cols-1 row-cols-lg-2 card-gutter align-items-center">
                        <div class="col">
                            <div class="row row-cols-2 g-5">
                                <div class="col">
                                    <a class="d-flex align-items-center justify-content-center" href="https://www.nhr4ces.de/">
                                        <img  src="/images/home_nhr_4_cse.svg" style="width: 100%; height: 80px; max-width: 180px; object-fit: contain;">
                                    </a>
                                </div>
                                <div class="col">
                                    <a class="d-flex align-items-center justify-content-center" href="https://nhrsw.de/">
                                        <img src="/images/home_nhr_sued_west.png" style="width: 100%; height: 80px; max-width: 200px; object-fit: contain;">
                                    </a>
                                </div>
                                <div class="col">
                                    <a class="d-flex align-items-center justify-content-center" href="https://rptu.de/">
                                        <img src="/images/home_tu_kaiserslautern.svg" style="width: 100%; height: 80px; max-width: 200px; object-fit: contain;">
                                    </a>
                                </div>
                                <div class="col">
                                    <a class="d-flex align-items-center justify-content-center" style="height: 80px;" href="https://www.itc.rwth-aachen.de">
                                        <img src="/images/home_rwth_aachen.png" style="width: 100%; height: 80px; max-width: 200px; object-fit: contain;">
                                    </a>
                                </div>  
                            </div>  
                        </div>
                        <div class="col">
                            <h1 class="card-title mb-4 display-5 fw-semibold">Who built it?</h1>
                            <p class="card-text mb-4" style="font-size: 1.125rem;">
                                DaVE is a collaboration between the RPTU Kaiserslautern and the RWTH Aachen and was founded thorugh a NHR future project.
                            </p>
                            <a class="btn btn-primary float-end float-sm-start" href="/about">Read more</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div id="home_video_consent" class="modal fade" tabindex="-1">
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header text-bg-dark" data-bs-theme="dark">
                        <h5>Youtube Video Consent</h5>
                    </div>
                    <div class="modal-body">
                        <p>The content embedded in this web page will take you to web pages provided by the Google-operated video sharing platform YouTube - YouTube, LLC, 901 Cherry Ave., San Bruno, CA 94066, USA. Invoking this content makes it possible for YouTube to determine your IP address, the language setting of your system, and a number of browser-specific details.</p>
                        <p>If you are logged in to your YouTube account, you make it possible for YouTube to tie your web browsing behavior directly to your personal profile. You can prevent this by logging out of your YouTube account.</p>
                        <p>YouTube uses cookies and tracking tools. Information on YouTube's data processing activities and the purpose of these activities is available and can be viewed at <a href="https://policies.google.com/privacy">YouTube</a>.</p>
                        <p>By clicking the "accept" button, you agree to use the content provided by the platform under the conditions outlined above.</p>
                        <p>Please note that you give your consent for a one-time use of the web page only. When you visit the page again, you will again be asked for your consent.</p>
                    </div>
                    <div class="modal-footer border-0">
                        <button class="btn btn-primary" type="button" data-bs-dismiss="modal">Decline</button>
                        <button class="btn btn-primary ms-auto" type="button" data-bs-dismiss="modal" @click="on_video_consent_accept">Accept</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
    <footer>
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>

<style scoped>
    .card-video
    {
        position: relative;
        aspect-ratio: 16 / 9;
    }

    .card-video iframe
    {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    .card-margin
    {
        margin-bottom: 1rem !important;
    }

    .card-container-padding
    {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    .card-padding
    {
        padding: 2rem !important;
    }

    .card-gutter
    {
        --bs-gutter-x: 2rem !important;
        --bs-gutter-y: 2rem !important;
    }

    .card-video-play
    {
        position: absolute; 
        z-index: 1; 
        top: 0px; 
        left: 0px; 
        width: 100%; 
        height: 100%; 
    }

    .card-video-play img
    {
        opacity: 0.8;
    }

    .card-video-play img:hover
    {
        opacity: 1.0;
        cursor: pointer;
    }

    @media (min-width: 576px)
    {
        .card-margin
        {
            margin-bottom: 2rem !important;
        }

        .card-container-padding
        {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }

        .card-padding
        {
            padding: 3rem !important;
        }

        .card-gutter
        {
            --bs-gutter-x: 3rem !important;
            --bs-gutter-y: 3rem !important;
        }
    }

    @media (min-width: 992px)
    {
        .card-margin
        {
            margin-bottom: 3rem !important;
        }

        .card-container-padding
        {
            padding-top: 3rem !important;
            padding-bottom: 3rem !important;
        }

        .card-padding
        {
            padding: 4rem !important;
        }

        .card-gutter
        {
            --bs-gutter-x: 4rem !important;
            --bs-gutter-y: 4rem !important;
        }

        .card-40
        {
            flex: 0 0 auto;
            width: 40%;
        }

        .card-60
        {
            flex: 0 0 auto;
            width: 60%;
        }
    }
</style>