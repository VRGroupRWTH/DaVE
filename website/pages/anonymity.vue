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
            <h1 class="display-1 py-5 mb-4 fw-semibold" style="font-size: min(5rem, max(1.625rem + 4.5vw, 3.5rem));">Link not avaliable</h1>
            <p class="col-lg-8" style="text-align: justify;">
                The link you clicked was removed for anonymity.
                Since this website is part of a scientific publication, every information that could reveal the identity of the authors has been removed from this website.
                After the anonymous reviewing process of the publication, the information that this link leads to will be made available.
            </p>
            <a href="/">Return to Homepage</a>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>