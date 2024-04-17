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
        <div class="home-background-image" style="height: 92vh;">
            <div class="d-flex flex-column align-items-center justify-content-center w-100 h-100" style="padding-bottom: 200px !important">
                <div class="d-flex justify-content-center align-items-center w-100 p-3" style="padding-bottom: 100px !important">
                    <img src="/public/images/logo.svg" width="100%" style="max-width: 750px">
                </div>
                <HomeSearchBar class="container-sm" @on_search_bar_search="on_search_bar_search"></HomeSearchBar>
            </div>
        </div>
        <div class="py-4 bg-body-tertiary" style="padding-top: 80px !important;padding-bottom: 80px !important;">
            <div class="container">
                <div class="mb-5">
                    <div class="card shadow-sm h-100 rounded-3 text-bg-dark">
                        <div style="padding: 4rem;" class="card-body">
                            <h1 class="card-title display-5 fw-semibold mb-4">What is DaVE?</h1>
                            <p class="card-text col-md-8" style="font-size: 1.125rem;">                                                                
                                DaVE serves as a centralized repository where users can find and discover visualization examples tailored to their specific needs through a simple search.
                                Our database is designed to be user-friendly, offering seamless integration into existing workflows using adaptable containers.
                                Whether you're exploring cutting-edge visualizations for data or seeking practical solutions to enhance your simulations, DaVE seeks to find helpful resources for you.
                            </p>
                        </div>
                        <!--<div class="p-3">
                            <a href="/guide" class="btn btn-outline-light float-end">Show</a>
                        </div>-->
                    </div>
                </div>
                <div class="row row-cols-1 row-cols-lg-3 g-5">
                    <div class="clo">
                        <div class="card shadow-sm h-100 rounded-3">
                            <div style="padding: 2rem;" class="card-body">
                                <h2 class="card-title fw-semibold">Browser</h2>
                                <p class="card-text">
                                    Use the browser to freely explore what DaVE has to offer.
                                    Just scroll thorugh the library of visualization examples and use filters to find a technique specific to your use case.
                                </p>
                            </div>
                            <div class="p-3">
                                <a href="/browser" class="btn btn-primary float-end">Show</a>
                            </div>
                        </div>
                    </div>
                    <div class="clo">
                        <div class="card shadow-sm h-100 rounded-3">
                            <div style="padding: 2rem;" class="card-body">
                                <h2 class="card-title fw-semibold">Guide</h2>
                                <p class="card-text">
                                    Get more information on how to use DaVE in the Guide. 
                                    Learn how DaVE is build up and how you can contribute to DaVE by creating your own examples.
                                    It's easy, give it a try.
                                </p>
                            </div>
                            <div class="p-3">
                                <a href="/guide" class="btn btn-primary float-end">Show</a>
                            </div>
                        </div>
                    </div>
                    <div class="clo">
                        <div class="card shadow-sm h-100 rounded-3">
                            <div style="padding: 2rem;" class="card-body">
                                <h2 class="card-title fw-semibold">About</h2>
                                <p class="card-text">
                                    Learn more about the project or get in touch with the creators if you have a question, don't know how to contribute or simply found a bug.
                                </p>
                            </div>
                            <div class="p-3">
                                <a href="/about" class="btn btn-primary float-end">Show</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="mt-5">
                    <div class="card shadow-sm h-100 rounded-3">
                        <div style="padding: 2rem;" class="card-body">
                            <div class="row align-items-center">
                                <div class="col-6 p-5">
                                    <h1 class="card-title mb-4 display-5 fw-semibold">Who build it?</h1>
                                    <p class="card-text" style="font-size: 1.125rem;">
                                        DaVE is a collaboration between the RPTU Kaiserslautern and the RWTH Aachen and was founded thorugh a NHR future project.
                                    </p>
                                </div>
                                <div class="col-6">
                                    <div class="row row-cols-2 g-5">
                                        <div class="col">
                                            <a href="https://www.nhr-verein.de/">
                                                <img class="p-4" src="/public/images/nhr_4_cse.svg" width="100%" height="100%" style="object-fit: contain;">
                                            </a>
                                        </div>
                                        <div class="col">
                                            <a href="https://rptu.de/">
                                                <img class="p-4"src="/public/images/tu_kaiserslautern.svg" width="100%" height="100%" style="object-fit: contain;">
                                            </a>
                                        </div>
                                        <div class="col">
                                            <a href="https://nhrsw.de/">
                                                <img class="p-4"src="/public/images/nhr_sued_west.png" width="100%" height="100%" style="object-fit: contain;">
                                            </a>
                                        </div>
                                        <div class="col">
                                            <a href="https://www.itc.rwth-aachen.de">
                                                <img class="p-4"src="/public/images/rwth_aachen.png" width="100%" height="100%" style="object-fit: contain;">
                                            </a>
                                        </div>  
                                    </div>  
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

<!--<template>
    <main>
        <div class="home-background-image">
            <div class="container py-5">
                <div class="d-flex justify-content-center align-items-center">
                    <div class="px-2 home-logo-large home-logo-blue">DaVE</div>
                    <div class="px-2 border-start home-logo-small">
                        A curated 
                        <span class="home-logo-blue">Da</span>tabase of <br class="d-none d-md-inline d-lg-none">
                        <span class="home-logo-blue">V</span>isualization <br class="d-none d-lg-inline d-xl-none">
                        <span class="home-logo-blue">E</span>xamples
                    </div>
                </div>
            </div>
            <HomeSearchBar class="container-sm pt-5" style="padding-bottom: 200px;" @on_search_bar_search="on_search_bar_search"></HomeSearchBar>
        </div>
    <div class="py-4 bg-body-tertiary">
        <div class="container">
            <div class="row row-cols-1 row-cols-lg-2 g-4">
                <div class="col">
                    <div class="card shadow-sm h-100">
                        <div class="card-body">
                            <h5 class="card-title">Wizard</h5>
                            <p class="card-text">Use the wizard to get a siutable visualization technique for your use case by answering some questions. You can also use the wizard to explore new visualization techniques that you might not have known before.</p>
                        </div>
                        <div class="p-3">
                            <a href="/wizard" class="btn btn-primary float-end">Show</a>
                        </div>
                    </div>
                </div>
                <div class="clo">
                    <div class="card shadow-sm h-100">
                        <div class="card-body">
                            <h5 class="card-title">Guide</h5>
                            <p class="card-text">Work in progress.</p>
                        </div>
                        <div class="p-3">
                            <a href="/guide" class="btn btn-primary float-end">Show</a>
                        </div>
                    </div>
                </div>
                <div class="clo">
                    <div class="card shadow-sm h-100">
                        <div class="card-body">
                            <h5 class="card-title">About</h5>
                            <p class="card-text">Get more information about the project.</p>
                        </div>
                        <div class="p-3">
                            <a href="/about" class="btn btn-primary float-end">Show</a>
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
</template>-->