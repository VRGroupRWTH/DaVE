Vue.createApp(
{
    setup()
    {
        let location_name = Vue.ref("");
        let location_description = Vue.ref("");

        return {
            location_name,
            location_description
        };
    },

    async mounted()
    {
        let technique_name = "";

        let arguments = window.location.search.substring(window.location.search.indexOf('?') + 1);
        arguments = arguments.replaceAll("%20", " ");

        for(const argument of arguments.split('&'))
        {
            const argument_name = argument.substring(0, argument.indexOf("="));

            if(argument_name == "technique")
            {
                technique_name = argument.substring(argument.indexOf("=") + 1);
            }
        }

        const technique_request_options =
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(
            {
                technique_name
            })
        };

        const technique = await (await fetch("api/fetch_technique", technique_request_options)).json();

        this.location_name = technique.name;
        this.location_description = technique.description;
    }
}).mount('#technique');