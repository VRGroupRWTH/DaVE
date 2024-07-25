<script>
    import { VueComponent as ImprintContent } from "../content/imprint_content.md";
    import GlobalHeader from "../components/global_header.vue"
    import GlobalFooter from "../components/global_footer.vue"

    export default
    {
        components:
        {
            GlobalHeader,
            GlobalFooter,
            ImprintContent
        }
    };
</script>
<template>
    <header>
        <GlobalHeader></GlobalHeader>
    </header>
    <main class="flex-fill">
        <div class="container">
            <div class="col-12 col-lg-10">
                <h1 class="display-1 fw-semibold ps-2 py-5 mb-4" style="font-size: min(5rem, max(1.625rem + 4.5vw, 3.5rem));">Site Credits</h1>
                <div class="imprint-content">
                    <ImprintContent></ImprintContent>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary mt-4">
        <GlobalFooter class="container"></GlobalFooter>
    </footer>
</template>