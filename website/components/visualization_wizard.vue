import { ref, computed, watch } from "vue"

const WizardQuestion = 
{
    props: ["name", "options", "config"],
    emits: ["update:config"],
    setup(props, context)
    {
        function on_wizard_question_check(event, option)
        {
            if(event.target.checked)
            {
                let config = props.config;
                config[props.name] = option.name;

                context.emit("update:config", config);
            }
        }

        function on_wizard_setting_change(event, setting)
        {
            let config = props.config;
            config[setting.name] = event.target.value;

            context.emit("update:config", config);
        }

        return {
            on_wizard_question_check,
            on_wizard_setting_change
        }
    },
    template:
    `
    <div v-for="option of options">
        <div class="form-check">
            <input :id="'wizard_question_' + option.name" class="form-check-input" type="radio" :name="'wizard_question_check_' + name" :checked="config[name] == option.name" @input="on_wizard_question_check($event, option)">
            <label :for="'wizard_question_' + option.name" class="form-check-label fw-semibold">{{ option.title }}</label>
        </div>
        <div style="margin-left: 24px">
            <p>{{ option.description }}</p>
            <template v-for="setting of option.settings">
                <label :for="'wizard_question_setting_' + setting.name" class="form-label">{{ setting.title }}</label>
                <input :id="'wizard_question_setting_' + setting.name" class="form-control" type="text" :disabled="config[name] != option.name" :value="config[setting.name]" @change="on_wizard_setting_change($event, setting)">
                <div class="form-text">{{ setting.description }}</div>
            </template>
        </div>
    </div>
    `
};

const WizardQuestionDataset = 
{
    components:
    {
        "wizard-question": WizardQuestion
    },
    props: ["visualization", "config"],
    emits: ["update:config"],
    setup(props)
    {
        let wizard_question_dataset_options = computed(() =>
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
                description: "The script for the visualization technique will donwload a small dataset with which the visualization can be directly tested.",
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
            wizard_question_dataset_options
        };
    },
    template:
    `
    <wizard-question name="dataset" :options="wizard_question_dataset_options" :config="config"></wizard-question>
    `
};

const WizardQuestionTechnique = 
{
    components: 
    {
        "wizard-question": WizardQuestion
    },
    props: ["visualization", "config"],
    emits: ["update:config"],
    setup(props)
    {
        let wizard_question_technique_options = computed(() =>
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
            wizard_question_technique_options
        }
    },
    template:
    `
    <wizard-question name="technique" :options="wizard_question_technique_options" :config="config"></wizard-question>
    `
};

const WizardQuestionCommand = 
{
    components: 
    {
        "wizard-question": WizardQuestion
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
    },
    template:
    `
    <wizard-question name="command" :options="wizard_question_command_options" :config="config"></wizard-question>
    `
};

export const VisualizationWizard = 
{
    components:
    {
        "wizard-question-dataset": WizardQuestionDataset,
        "wizard-question-technique": WizardQuestionTechnique,
        "wizard-question-command": WizardQuestionCommand,
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
    },
    template:
    `
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
    `
}