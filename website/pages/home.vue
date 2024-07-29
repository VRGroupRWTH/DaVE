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
                            <a href="https://github.com/VRGroupRWTH/DaVE" class="mb-2">
                                <img src="../assets/icons/github.svg" width="64px">
                            </a>
                            <p style="font-size: 1.125rem;">
                                Check it out on GitHub
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row g-3 g-md-5 mb-3 mb-md-5">
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
            <div class="card shadow-sm rounded-3 mb-3 mb-md-5">
                <div class="card-body card-padding">
                    <div class="row align-items-center g-1 g-sm-5">
                        <div class="col-12 col-lg-5 d-flex justify-content-center">
                            <img src="/images/home_contribution.svg" class="flex-fill p-4 p-lg-0 " style="max-width: 450px">
                        </div>
                        <div class="col-12 col-lg-7">
                            <h1 class="card-title display-5 fw-semibold mb-4">Become a Contributor</h1>
                            <p class="card-text" style="font-size: 1.125rem;">
                                Join us in growing DaVE by becoming a contributor!
                                You can contribute no matter how experienced you are in making visualizations.
                                It's as easy as adding a folder to the database to create your own example.
                            </p>
                            <a class="btn btn-primary float-end float-sm-none" href="/guide_extend_dave">Read more</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card shadow-sm rounded-3">
                <div class="card-body card-padding">
                    <div class="row row-cols-1 row-cols-lg-2 g-5 align-items-center">
                        <div class="col">
                            <h1 class="card-title mb-4 display-5 fw-semibold">Who built it?</h1>
                            <p class="card-text" style="font-size: 1.125rem;">
                                DaVE is a collaboration between the RPTU Kaiserslautern and the RWTH Aachen and was founded thorugh a NHR future project.
                            </p>
                        </div>
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