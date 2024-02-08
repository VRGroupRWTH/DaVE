export const VisualizationContent =
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
    },
    template:
    `
    <div class="card card-body shadow-sm">
        <table class="table align-middle">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col" class="d-none d-sm-table-cell">Type</th>
                    <th scope="col" class="d-none d-md-table-cell">Date</th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="resource of visualization.resources">
                    <td scope="row">{{ resource.name }}</td>
                    <td class="d-none d-sm-table-cell">{{ resource.type }}</td>
                    <td class="d-none d-md-table-cell">{{ convert_date(resource.date) }}</td>
                    <td v-if="'path' in resource">
                        <a class="btn btn-primary float-end me-3 p-0 d-flex align-items-center justify-content-center" style="width: 32px; height: 32px" :href="resource.path" download>
                            <img src="symbols/download.svg"/>
                        </a>
                    </td>
                    <td v-else-if="'url' in resource">
                        <a class="btn btn-primary float-end me-3 p-0 d-flex align-items-center justify-content-center" style="width: 32px; height: 32px" :href="resource.url">
                            <img src="symbols/link_45deg.svg"/>
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    `
}