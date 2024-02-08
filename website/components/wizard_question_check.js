import { computed } from "vue"

export const WizardQuestionCheck =
{
    props: ["answers", "options"],
    setup(props)
    {
        let wizard_question_groups = computed(() =>
        {
            let groups = [];

            for(const option of props.options)
            {
                if(!groups.some(item => item == option.group))
                {
                    groups.push(option.group);
                }
            }

            return groups;
        });

        return {
            wizard_question_groups
        }
    },
    template:
    `
    <div class="d-flex flex-wrap p-3">
        <div v-for="group of wizard_question_groups" class="me-4 mb-4">
            <h5 >{{ group }}</h5>
            <div v-for="option of options.filter(item => item.group == group)" class="form-check ms-2">
                <input :id="'wizard_question_option_' + option.name" class="form-check-input" type="checkbox">
                <label :for="'wizard_question_option_' + option.name" class="form-check-label">{{ option.title }}</label>
            </div>
        </div>
    </div>
    `
}