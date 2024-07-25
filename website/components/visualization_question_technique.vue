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
            let technique_options = computed(() =>
            {
                const option_docker = 
                {
                    name: "docker",
                    title: "Docker",
                    description: "The visualization technique should be encapsulated in a docker container. Docker is the most common container technique.",
                    settings: []
                };

                const option_singularity = 
                {
                    name: "singularity",
                    title: "Singularity",
                    description: "The visualization technique should be encapsulated in a singularity container. Singularity is generally better suited for the deployment on a cluster, as it does not require root privileges.",
                    settings: []
                };

                let options = [option_docker, option_singularity];
                let available_options = [];

                for(const option of options)
                {
                    let found = false;

                    for(const template of props.visualization.templates)
                    {
                        if(template.techniques.some(item => item == option.name))
                        {
                            found = true;

                            break;
                        }
                    }

                    if(found)
                    {
                        available_options.push(option);
                    }
                }

                return available_options;
            });

            return {
                technique_options
            }
        }
    };
</script>

<template>
    <VisualizationQuestion name="technique" :options="technique_options" :config="config"></VisualizationQuestion>
</template>