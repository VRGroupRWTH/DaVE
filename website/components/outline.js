import { ref } from "vue"

export const Outline = 
{
    props: ["target"],
    setup(props)
    {
        function on_elements_intersect(entities)
        {
            
        }

        const outline_intersection_options = 
        {
            root: null,
            threshold: [0.1, 0.5, 1.0],
            rootMargin: "-80px 0px 0px 0px"
        };

        let outline_intersection_observer = new IntersectionObserver(entries => on_intersection(entries), intersection_options);

        let outline_container = ref(null);
        let outline_elements = ref([]);
        let outline_items = computed( () =>
        {
            let items = [];

            for(const element of outline_elements)
            {
                const item = 
                {
                    label: element.innerHtml,
                    link: "#" + element.id
                }

                items.push(item);
            }

            return items;
        });


        function setup_elements()
        {
            outline_elements.value = [];
            search_elements(props.target)



        }

        function search_elements(element)
        {
            if(element.id != "")
            {
                outline_elements.value.push(element);
            }

            for(const child of element.childNodes)
            {
                search_elements(child);
            }
        }

        return {
            outline_container,
            outline_items
        }
    },
    template: 
    `
    <nav ref="outline_container" class="nav flex-column align-items-stretch outline">
        <template v-for="item of outline_items">
            <a :class="" :href="item.link">{{ item.label }}</a>
        </template>
    </nav>
    `
}