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
        props: 
        { 
            browser_filters : Object, 
            browser_filters_show : Boolean
        },
        emits: ["update:browser_filters"]
    };
</script>

<template>
    <div class="z-1">
        <button class="btn btn-toggle border-0 w-100 d-flex align-items-end browser-filter-toggle-arrow" type="button" data-bs-toggle="collapse" data-bs-target="#browser_filter_collapse" aria-expanded="true">
            <img src="../assets/icons/caret_down_fill.svg" width="20px">
            <div class="ms-1">Filters</div>
        </button>
        <div id="browser_filter_collapse" class="collapse px-4" :class="browser_filters_show ? 'show' : ''">
            <ul class="list-unstyled mt-2">
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_tag">Tags</label>
                    <BrowserFilterTag id="browser_filter_tag" :browser_filters="browser_filters"></BrowserFilterTag>
                </li>
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_author">Authors</label>
                    <BrowserFilterAuthor id="browser_filter_author" :browser_filters="browser_filters"></BrowserFilterAuthor>
                </li>
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_date">Date</label>
                    <BrowserFilterDate id="browser_filter_date" :browser_filters="browser_filters"></BrowserFilterDate>
                </li>
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_container">Container</label>
                    <div id="browser_filter_container">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="browser_filters.check_container_docker" id="browser_filter_container_docker">
                            <label class="form-check-label" for="browser_filter_container_docker">Docker</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="browser_filters.check_container_singularity" id="browser_filter_container_singularity">
                            <label class="form-check-label" for="browser_filter_container_singularity">Singularity</label>
                        </div>
                    </div>
                </li>
                <li class="mb-2">
                    <label class="form-label" for="browser_filter_container">Execution</label>
                    <div id="browser_filter_container">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="browser_filters.check_execution_local" id="browser_filter_execution_local">
                            <label class="form-check-label" for="browser_filter_execution_local">Local</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="browser_filters.check_execution_mpi" id="browser_filter_execution_mpi">
                            <label class="form-check-label" for="browser_filter_execution_mpi">MPI</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="browser_filters.check_execution_slurm" id="browser_filter_execution_slurm">
                            <label class="form-check-label" for="browser_filter_execution_slurm">Slurm</label>
                        </div>
                    </div>
                </li>
                <li>
                    <label class="form-label" for="browser_filter_other">Other</label>
                    <div id="browser_filter_other">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox"  v-model="browser_filters.check_other_preview" id="browser_filter_other_preview">
                            <label class="form-check-label" for="browser_filter_other_preview">Preview</label>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>