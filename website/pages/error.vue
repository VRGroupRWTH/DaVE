<script>
    import GlobalHeader from "../components/global_header.vue"
    import GlobalFooter from "../components/global_footer.vue"

    export default
    {
        components:
        {
            GlobalHeader,
            GlobalFooter
        }
    };
</script>
<template>
    <header>
        <GlobalHeader></GlobalHeader>
    </header>
    <main class="flex-fill">
        <div class="container ps-lg-5 py-5">
            <h1 class="display-1 py-5 mb-4 fw-semibold" style="font-size: min(5rem, max(1.625rem + 4.5vw, 3.5rem));">Error</h1>
            <p class="col-lg-8" style="text-align: justify;">
                The page that you want to access ether does not exist or an error occured during the usage of the website.
            </p>
            <a href="/">Return to Homepage</a>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>