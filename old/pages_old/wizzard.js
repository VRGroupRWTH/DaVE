questions =
[
    {
        question : "What data formats are you using?",
        options : ["Images", "Volumetric", "Networks", "Tables"]
    },
    {
        question : "How many dimensions do you use?",
        options : ["1D", "2D", "3D", "nD"]
    },
    {
        question : "Does your data change over time?",
        options : ["Yes", "No"]
    },
    {
        question : "Is there a physical unit that could be assigned to your data?",
        options : ["Distance", "Time", "Speed", "Acceleration", "Density", "Temperature", "Color"]
    },
    {
        question : "What devies do you want to use for the visualisation of the data?",
        options : ["Desktop Computer", "Virtual Reality Headset", "Cave", "Mobile"]
    },
]

Vue.createApp(
{
    setup()
    {
        location_question = Vue.ref("");
        location_options = Vue.ref([]);
        location_question_start = Vue.ref(false);
        location_question_end = Vue.ref(false);
        location_question_index = Vue.ref(0);
        location_selection = Vue.ref([]);

        for(let question_index = 0; question_index < questions.length; question_index++)
        {
            location_selection.value[question_index] = [];

            for(let option_index = 0; option_index < questions[question_index].options.length; option_index++)
            {
                location_selection.value[question_index][option_index] = false;
            }
        }

        function show_question(question_index)
        {
            location_question_index.value = Math.max(Math.min(question_index, questions.length - 1), 0);

            location_question.value = questions[location_question_index.value].question;
            location_options.value = questions[location_question_index.value].options;

            location_question_start.value = (location_question_index.value == 0);
            location_question_end.value = (location_question_index.value == questions.length - 1);
        }

        function on_next_question(event)
        {
            show_question(location_question_index.value + 1);
        }

        function on_previous_question(event)
        {
            show_question(location_question_index.value - 1);
        }

        function on_submit(event)
        {
            window.location = "/browser";
        }

        return {
            location_question,
            location_options,
            location_question_start,
            location_question_end,
            location_question_index,
            location_selection,
            show_question,
            on_next_question,
            on_previous_question,
            on_submit
        }
    },

    mounted()
    {
        this.show_question(0);
    }
}).mount("#wizzard");