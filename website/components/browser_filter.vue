<script>
    import BrowserFilterDate from './browser_filter_date.vue';
    import BrowserFilterTag from './browser_filter_tag.vue';
    import BrowserFilterAuthor from './browser_filter_author.vue';

    export default
    {
        components:
        {
            BrowserFilterDate,
            BrowserFilterTag,
            BrowserFilterAuthor
        },
        props: ["browser_filters"],
        emits: ["update:browser_filters"]
    };
</script>

<template>
    <div>
        <button class="btn btn-toggle border-0 w-100 d-flex align-items-end browser-filter-toggle-arrow" type="button" data-bs-toggle="collapse" data-bs-target="#browser_filter_collapse" aria-expanded="true">
            <img src="../assets/icons/caret_down_fill.svg" width="20px">
            <div class="ms-1">Filters</div>
        </button>
        <div id="browser_filter_collapse" class="collapse show px-4">
            <ul class="list-unstyled mt-2">
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_tag">Tags</label>
                    <browser-filter-tag id="browser_filter_tag" :browser_filters="browser_filters"></browser-filter-tag>
                </li>
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_author">Authors</label>
                    <browser-filter-author id="browser_filter_author" :browser_filters="browser_filters"></browser-filter-author>
                </li>
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_date">Date</label>
                    <browser-filter-date id="browser_filter_date" :browser_filters="browser_filters"></browser-filter-date>
                </li>
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_container">Container</label>
                    <div id="browser_filter_container">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                            <label class="form-check-label" for="defaultCheck1">Docker</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                            <label class="form-check-label" for="defaultCheck1">Singularity</label>
                        </div>
                    </div>
                </li>
                <li>
                    <label class="form-label" for="browser_filter_container">Container</label>
                    <div id="browser_filter_container">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                            <label class="form-check-label" for="defaultCheck1">Docker</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                            <label class="form-check-label" for="defaultCheck1">Singularity</label>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>