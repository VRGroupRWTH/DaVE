<script>
    export default
    {
        props: ["visualization"],
        setup()
        {
            function convert_date(date_string)
            {
                const date = new Date(date_string);
                const date_options =
                {
                    year: "numeric",
                    month: "numeric",
                    day: "numeric"
                };

                return date.toLocaleDateString(undefined, date_options);
            }

            return {
                convert_date
            }
        }
    };
</script>

<template>
    <div id="Resources" outline_label="Resources" outline_indent="0" style="scroll-margin-top: 80px;">
        <h3>Resources</h3>
        <div class="alert alert-success d-flex align-items-center" style="padding-top: 10px; padding-bottom: 10px">
            <img class="me-2"src="/assets/icons/box_seam_fill.svg" width="24px">
            <div class="flex-fill">Container avaliable!</div>
            <button class="btn btn-outline-success" type="button">Customize</button>
        </div>
        <div class="alert alert-light">
            <div class="d-flex justify-content-end">
                <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#visualization_wizard">
                    <div class="d-flex align-items-center">
                        <div>Download</div>
                        
                    </div>
                </button>
            </div>
            <table class="table align-middle visualization-resources-table ">
                <thead>
                    <tr>
                        <th scope="col" style="width: 0px"><input class="form-check-input" type="checkbox" value=""></th>
                        <th scope="col">Name</th>
                        <th scope="col" class="d-none d-sm-table-cell">Type</th>
                        <th scope="col" class="d-none d-md-table-cell">Date</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="resource of visualization.resources">
                        <td scope="row"><input class="form-check-input" type="checkbox" value=""></td>
                        <td scope="row">{{ resource.name }}</td>
                        <td class="d-none d-sm-table-cell">{{ resource.type }}</td>
                        <td class="d-none d-md-table-cell">{{ convert_date(resource.date) }}</td>
                        <td v-if="'path' in resource">
                            <a class="btn btn-primary float-end me-3 p-0 d-flex align-items-center justify-content-center" style="width: 32px; height: 32px" :href="resource.path" download>
                                <img src="../assets/icons/download.svg"/>
                            </a>
                        </td>
                        <td v-else-if="'url' in resource">
                            <a class="btn btn-primary float-end me-3 p-0 d-flex align-items-center justify-content-center" style="width: 32px; height: 32px" :href="resource.url">
                                <img src="../assets/icons/link_45deg.svg"/>
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>