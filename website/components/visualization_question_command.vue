<script>
    import { computed } from "vue";
    import VisualizationQuestion from "./visualization_question.vue";

    export default
    {
        components: 
        {
            "wizard-question": VisualizationQuestion
        },
        props: ["visualization", "config"],
        emits: ["update:config"],
        setup(props)
        {
            let wizard_question_command_options = computed(() =>
            {
                const option_local = 
                {
                    name: "local",
                    title: "Execute Local",
                    description: "The visualization technique is executed locally on a single computer, e.g. a desktop computer.",
                    settings: []
                };

                const option_mpi = 
                {
                    name: "mpi",
                    title: "Batch using MPI",
                    description: "The visualization technique should be executed using MPI. Choose this option if multiple instances of the visualization technique should be run, for example, on a cluster.",
                    settings: []
                };

                const option_slurm = 
                {
                    name: "slurm",
                    title: "Batch using Slurm",
                    description: "The visualization technique should be executed using Slurm. Choose this option if multiple instances of the visualization technique should be run, for example, on a cluster.",
                    settings: []
                };

                let options = [option_local, option_mpi, option_slurm];
                let available_options = [];

                for(const option of options)
                {
                    let found = false;

                    for(const template of props.visualization.templates)
                    {
                        if(!template.techniques.some(item => item == props.config.technique))
                        {
                            continue;
                        }

                        if(template.commands.some(item => item.type == option.name))
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
                wizard_question_command_options
            }
        }
    };
</script>

<template>
    <wizard-question name="command" :options="wizard_question_command_options" :config="config"></wizard-question>
</template>