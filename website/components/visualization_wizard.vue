<script>
    import { ref, computed, watch } from "vue";
    import VisualizationQuestionDataset from "./visualization_question_dataset.vue";
    import VisualizationQuestionTechnique from "./visualization_question_technique.vue";
    import VisualizationQuestionCommand from "./visualization_question_command.vue";

    export default
    {
        components:
        {
            "wizard-question-dataset": VisualizationQuestionDataset,
            "wizard-question-technique": VisualizationQuestionTechnique,
            "wizard-question-command": VisualizationQuestionCommand,
        },
        props: ["visualization"],
        setup(props)
        {
            let visualization_wizard_question_index = ref(0);
            let visualization_wizard_question_titles = ref(
            [
                "Dataset",
                "Container",
                "Execution"
            ]);
            let visualization_wizard_questions = ref(
            [
                "wizard-question-dataset",
                "wizard-question-technique",
                "wizard-question-command"
            ]);

            let visualization_wizard_config = ref(
            {
                dataset: "preview",
                technique: "",
                command: ""
            });

            function setup_visualization_wizard()
            {
                let config = 
                {
                    dataset: "",
                    technique: "",
                    command: ""
                };

                if(props.visualization.templates.length > 0)
                {
                    const template = props.visualization.templates[0];
        
                    config.technique = template.techniques[0];
                    config.command = template.commands[0].type;
                }

                let dataset_preview_availiable = true;

                for(const dataset of props.visualization.datasets)
                {
                    const dataset_identifier = "dataset_path_" + dataset.identifier.toLowerCase();

                    config[dataset_identifier] = "./data/"

                    if(!("path" in dataset) && !("url" in dataset))
                    {
                        dataset_preview_availiable = false;
                    }
                }

                if(dataset_preview_availiable)
                {
                    config.dataset = "preview";
                }

                else
                {
                    config.dataset = "custom";
                }

                visualization_wizard_config.value = config;
            }

            watch([props], (old_state, new_state) =>
            {
                setup_visualization_wizard();
            });

            let visualization_wizard_link = computed(() =>
            {
                let link = "/api/create_script?";
                link += "visualization=" + props.visualization.name + "&";
                link += "technique=" + visualization_wizard_config.value.technique + "&";
                link += "command=" + visualization_wizard_config.value.command;

                if(visualization_wizard_config.value.dataset != "preview")
                {
                    let dataset_link = "";

                    for(const dataset of props.visualization.datasets)
                    {
                        const dataset_identifier = "dataset_path_" + dataset.identifier.toLowerCase();

                        if(dataset_identifier in visualization_wizard_config.value)
                        {
                            dataset_link += dataset.identifier + "+" + visualization_wizard_config.value[dataset_identifier];
                        }
                    }

                    link += "&datasets=" + encodeURIComponent(dataset_link)
                }
                
                return link;
            });

            function on_visualization_wizard_open()
            {
                setup_visualization_wizard();

                visualization_wizard_question_index.value = 0;
            }

            function on_visualization_wizard_question_back()
            {
                if(visualization_wizard_question_index.value > 0)
                {
                    visualization_wizard_question_index.value = visualization_wizard_question_index.value - 1;
                }
            }

            function on_visualization_wizard_question_next()
            {
                if(visualization_wizard_question_index.value < visualization_wizard_questions.value.length - 1)
                {
                    visualization_wizard_question_index.value = visualization_wizard_question_index.value + 1;
                }
            }

            return {
                visualization_wizard_question_index,
                visualization_wizard_question_titles,
                visualization_wizard_questions,
                visualization_wizard_config,
                visualization_wizard_link,
                on_visualization_wizard_open,
                on_visualization_wizard_question_back,
                on_visualization_wizard_question_next
            }
        }
    };
</script>

<template>
    <div class="modal fade" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header text-bg-dark" data-bs-theme="dark">
                    <h5 class="modal-title text-bg-dark">{{ visualization_wizard_question_titles[visualization_wizard_question_index] }}</h5>
                    <button class="btn-close" type="button" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <component :is="visualization_wizard_questions[visualization_wizard_question_index]" :visualization="visualization" v-model:config="visualization_wizard_config"></component>
                </div>
                <div class="modal-footer border-0">
                    <button v-if="visualization_wizard_question_index > 0" class="btn btn-primary" type="button" @click="on_visualization_wizard_question_back">Back</button>
                    <button v-if="visualization_wizard_question_index < visualization_wizard_questions.length - 1" class="btn btn-primary ms-auto" type="button" @click="on_visualization_wizard_question_next">Next</button>
                    <a v-else class="btn btn-primary ms-auto" :href="visualization_wizard_link" download="render_script.zip">Download</a>
                </div>
            </div>
        </div>
    </div>
</template>