<script>
    import { computed } from "vue";
    import VisualizationQuestion from "./visualization_question.vue";

    export default
    {
        components:
        {
            VisualizationQuestion
        },
        props: ["visualization", "config"],
        emits: ["update:config"],
        setup(props)
        {
            let dataset_options = computed(() =>
            {
                let dataset_settings = [];
                let dataset_preview_availiable = true;

                for(const dataset of props.visualization.datasets)
                {
                    const dataset_identifier = "dataset_path_" + dataset.identifier.toLowerCase();

                    const dataset_setting =
                    {
                        name: dataset_identifier,
                        title: dataset.name,
                        description: dataset.description
                    };

                    dataset_settings.push(dataset_setting);

                    if(!("path" in dataset) && !("url" in dataset))
                    {
                        dataset_preview_availiable = false;
                    }
                }

                const option_dataset_preview =
                {
                    name: "preview",
                    title: "Preview Dataset",
                    description: "The script for the visualization technique will download a small dataset with which the visualization can be directly tested.",
                    settings: []
                };

                const option_dataset_custom =
                {
                    name: "custom",
                    title: "Custom Dataset",
                    description: "Only the scripts for the visualization technique will be downloaded. The datasets used by the technique are expected to be located at the given paths.",
                    settings: dataset_settings
                };

                if(dataset_preview_availiable)
                {
                    return [option_dataset_preview, option_dataset_custom];
                }

                return [option_dataset_custom];
            });

            return {
                dataset_options
            };
        }
    };
</script>

<template>
    <VisualizationQuestion name="dataset" :options="dataset_options" :config="config"></VisualizationQuestion>
</template>
