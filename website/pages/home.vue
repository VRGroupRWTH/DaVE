<script>
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

            return {
                on_search_bar_search
            }
        }
    };
</script>

<template>
    <main>
        <div class="home-background-image" style="height: 80vh; min-height: 600px;">
            <div class="d-flex flex-column align-items-center justify-content-center w-100 h-100" style="padding-top: 50px; padding-bottom: 150px;">
                <div class="d-flex justify-content-center align-items-center w-100 p-3" style="min-height: 0px; padding-top: 0px !important; padding-bottom: 150px !important;">
                    <img src="/images/logo.svg" style="width: 100%; height: 100%; max-width: 750px">
                </div>
                <HomeSearchBar class="container-sm" @on_search_bar_search="on_search_bar_search"></HomeSearchBar>
            </div>
        </div>
        <div class="bg-body-tertiary card-container-padding">
            <div class="container">
                <div class="card text-bg-dark shadow-sm rounded-3 mb-3 mb-md-5">
                    <div class="card-body card-padding">
                        <h1 class="card-title display-5 fw-semibold mb-4">What is DaVE?</h1>
                        <div class="row g-5">
                            <p class="card-text col-12 col-lg-8" style="font-size: 1.125rem;">                                                                
                                DaVE serves as a centralized repository where users can find and discover visualization examples tailored to their specific needs through a simple search.
                                Our database is designed to be user-friendly, offering seamless integration into existing workflows using adaptable containers.
                                Whether you're exploring cutting-edge visualizations for data or seeking practical solutions to enhance your simulations, DaVE seeks to find helpful resources for you.
                            </p>
                            <div class="col-12 col-lg-4 d-flex align-items-center justify-content-center flex-column">
                                <a href="https://github.com/Jens-Koenen/DaVE" class="mb-2" target="_blank">
                                    <img src="../assets/icons/github.svg" width="64px">
                                </a>
                                <p style="font-size: 1.125rem;">
                                    Check it out on GitHub
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- mb-3 mb-md-5 -->
                <div class="row g-3 g-md-5">
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
                </div>
                <!--<div class="card shadow-sm rounded-3">
                    <div class="card-body card-padding">
                        <div class="row row-cols-1 row-cols-lg-2 g-5 align-items-center">
                            <div class="col">
                                <h1 class="card-title mb-4 display-5 fw-semibold">Who build it?</h1>
                                <p class="card-text" style="font-size: 1.125rem;">
                                    DaVE is a collaboration between the RPTU Kaiserslautern and the RWTH Aachen and was founded thorugh a NHR future project.
                                </p>
                            </div>
                            <div class="col">
                                <div class="row row-cols-2 g-5">
                                    <div class="col">
                                        <a class="d-flex align-items-center justify-content-center" href="https://www.nhr-verein.de/">
                                            <img  src="/images/nhr_4_cse.svg" style="width: 100%; height: 80px; max-width: 180px; object-fit: contain;">
                                        </a>
                                    </div>
                                    <div class="col">
                                        <a class="d-flex align-items-center justify-content-center" href="https://nhrsw.de/">
                                            <img src="/images/nhr_sued_west.png" style="width: 100%; height: 80px; max-width: 200px; object-fit: contain;">
                                        </a>
                                    </div>
                                    <div class="col">
                                        <a class="d-flex align-items-center justify-content-center" href="https://rptu.de/">
                                            <img src="/images/tu_kaiserslautern.svg" style="width: 100%; height: 80px; max-width: 200px; object-fit: contain;">
                                        </a>
                                    </div>
                                    <div class="col">
                                        <a class="d-flex align-items-center justify-content-center" style="height: 80px;" href="https://www.itc.rwth-aachen.de">
                                            <img src="/images/rwth_aachen.png" style="width: 100%; height: 80px; max-width: 200px; object-fit: contain;">
                                        </a>
                                    </div>  
                                </div>  
                            </div>
                        </div>
                    </div>
                </div>-->
            </div>
        </div>
    </main>
    <footer>
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>

<style scoped>
    .card-padding
    {
        padding: 2rem !important;
    }

    .card-container-padding
    {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    @media (min-width: 576px)
    {
        .card-padding
        {
            padding: 4rem !important;
        }

        .card-container-padding
        {
            padding-top: 3rem !important;
            padding-bottom: 3rem !important;
        }
    }
</style>