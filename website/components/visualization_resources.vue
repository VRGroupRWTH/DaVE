<script>
    import { ref, computed, watch } from "vue"

    export default
    {
        props: ["visualization", "visualization_wizard"],
        setup(props)
        {
            /*let select_all_box = ref(null);
            let selected_items = ref([]);
            let selected_items_link = computed(() =>
            {
                let resource_list = "";

                for(let index = 0; index < selected_items.value.length; index++)
                {
                    const selected_item = selected_items.value[index];
                    resource_list += selected_item.toString();

                    if(index < selected_items.value.length - 1)
                    {
                        resource_list += "+"
                    }
                }

                return "/api/download_resources?visualization=" + props.visualization.name + "&resources=" + encodeURIComponent(resource_list);
            });

            function is_downloadable(resource)
            {
                return !("url" in resource); //Not optimal!!!
            }*/

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

            /*function on_item_select(event, index)
            {
                if(event.target.checked)
                {
                    selected_items.value.push(index);
                }

                else
                {
                    selected_items.value = selected_items.value.filter(item => item != index);
                }
            }

            watch([props, selected_items], (old_state, new_state) =>
            {
                const current_count = selected_items.value.length;
                let total_count = 0;

                for(const resource of props.visualization.resources)
                {
                    if(is_downloadable(resource))
                    {
                        total_count++;
                    }
                }

                if(current_count == 0)
                {
                    select_all_box.value.checked = false;
                    select_all_box.value.indeterminate = false;
                }

                else if(0 < current_count && current_count < total_count)
                {
                    select_all_box.value.checked = true;
                    select_all_box.value.indeterminate = true;
                }

                else if(current_count == total_count)
                {
                    select_all_box.value.checked = true;
                    select_all_box.value.indeterminate = false;
                }
            }, { deep: true });

            function on_item_select_all()
            {
                if(selected_items.value.length > 0)
                {
                    selected_items.value = [];
                }

                else
                {
                    for(let index = 0; index < props.visualization.resources.length; index++)
                    {
                        const resource = props.visualization.resources[index];

                        if(is_downloadable(resource))
                        {
                            selected_items.value.push(index);   
                        }
                    }
                }        
            }*/

            return {
                //select_all_box,
                //selected_items,
                //selected_items_link,
                convert_date,
                //is_downloadable,
                //on_item_select,
                //on_item_select_all
            }
        }
    };
</script>

<template>
    <div id="Resources" outline_label="Resources" outline_indent="0" style="scroll-margin-top: 80px;">
        <h3>Resources</h3>
        <div class="alert alert-success d-flex align-items-center px-4" style="padding-top: 12px; padding-bottom: 12px">
            <img class="me-2"src="/assets/icons/box_seam_fill.svg" width="24px">
            <div class="flex-fill">Container available!</div>
            <button class="btn btn-outline-success" type="button" data-bs-toggle="modal" data-bs-target="#visualization_wizard">Customize</button>
        </div>
        <div class="alert alert-light">
            <table class="table align-middle visualization-resources-table ">
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">Name</th>
                        <th scope="col" class="d-none d-sm-table-cell">Type</th>
                        <th scope="col" class="d-none d-md-table-cell">Date</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="resource of visualization.resources">
                        <td scope="row"></td>
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
    <!--<div id="Resources" outline_label="Resources" outline_indent="0" style="scroll-margin-top: 80px;">
        <h3>Resources</h3>
        <div class="alert alert-success d-flex align-items-center px-4" style="padding-top: 12px; padding-bottom: 12px">
            <img class="me-2"src="/assets/icons/box_seam_fill.svg" width="24px">
            <div class="flex-fill">Container available!</div>
            <button class="btn btn-outline-success" type="button" data-bs-toggle="modal" data-bs-target="#visualization_wizard">Customize</button>
        </div>
        <div class="alert alert-light">
            <table class="table align-middle visualization-resources-table ">
                <thead>
                    <tr>
                        <th scope="col" style="width: 0px"><input ref="select_all_box" class="form-check-input" type="checkbox" @click="on_item_select_all()"></th>
                        <th scope="col">Name</th>
                        <th scope="col" class="d-none d-sm-table-cell">Type</th>
                        <th scope="col" class="d-none d-md-table-cell">Date</th>
                        <th scope="col" style="width: 0px"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(resource, index) of visualization.resources">
                        <td scope="row"><input class="form-check-input" type="checkbox" :checked="selected_items.some(item => item == index)" @click="event => on_item_select(event, index)" :disabled="!is_downloadable(resource)"></td>
                        <td scope="row">{{ resource.name }}</td>
                        <td class="d-none d-sm-table-cell">{{ resource.type }}</td>
                        <td class="d-none d-md-table-cell">{{ convert_date(resource.date) }}</td>
                        <td v-if="'path' in resource">
                            <a class="btn btn-outline-secondary float-end" style="width: 100px" :href="resource.path" download>Download</a>
                        </td>
                        <td v-else-if="'url' in resource">
                            <a class="btn btn-outline-secondary float-end" style="width: 100px" :href="resource.url">Link</a>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="d-flex justify-content-between align-items-center pe-2 ps-2">
                <div v-if="selected_items.length == 0" class="fw-semibold text-body">No Files selected</div>
                <div v-else class="fw-semibold text-body">{{ selected_items.length }} Files selected</div>
                <a class="btn btn-primary" type="button" :class="selected_items.length == 0 ? 'disabled' : ''" download="files.zip" :href="selected_items_link">Download Selected</a>
            </div>
        </div>
    </div>-->
</template>