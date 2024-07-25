<script>
    import { ref, computed, watch } from "vue";

    export default
    {
        props: ["name", "options", "config"],
        emits: ["update:config"],
        setup(props, context)
        {
            function on_question_check(event, option)
            {
                if(event.target.checked)
                {
                    let config = props.config;
                    config[props.name] = option.name;

                    context.emit("update:config", config);
                }
            }

            function on_setting_change(event, setting)
            {
                let config = props.config;
                config[setting.name] = event.target.value;

                context.emit("update:config", config);
            }

            return {
                on_question_check,
                on_setting_change
            }
        }
    };
</script>

<template>
    <div v-for="option of options">
        <div class="form-check">
            <input :id="'question_' + option.name" class="form-check-input" type="radio" :name="'question_check_' + name" :checked="config[name] == option.name" @input="on_wizard_question_check($event, option)">
            <label :for="'question_' + option.name" class="form-check-label fw-semibold">{{ option.title }}</label>
        </div>
        <div style="margin-left: 24px">
            <p>{{ option.description }}</p>
            <template v-for="setting of option.settings">
                <label :for="'question_setting_' + setting.name" class="form-label">{{ setting.title }}</label>
                <input :id="'question_setting_' + setting.name" class="form-control" type="text" :disabled="config[name] != option.name" :value="config[setting.name]" @change="on_wizard_setting_change($event, setting)">
                <div class="form-text">{{ setting.description }}</div>
            </template>
        </div>
    </div>
</template>