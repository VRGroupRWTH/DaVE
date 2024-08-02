<script>
    import { ref, computed, watch } from "vue";

    export default
    {
        props: ["target", "depth_max"],
        setup(props)
        {
            const outline_mutation_options = 
            {
                subtree: true,
                childList: true
            };

            const outline_intersection_options = 
            {
                root: null,
                threshold: [0.1, 0.5, 1.0],
                rootMargin: "-80px 0px 0px 0px"
            };

            let outline_mutation_observer = null;
            let outline_intersection_observer = null;

            let outline_elements = ref([]);
            let outline_elements_visible = {};
            let outline_element_active = ref("");
            let outline_items = computed(() =>
            {
                let items = [];

                for(const element of outline_elements.value)
                {
                    if(is_hidden(element))
                    {
                        continue;
                    }

                    const item = 
                    {
                        label: element.attributes.outline_label.value,
                        link: "#" + element.id,
                        active: is_child_of(outline_element_active.value, element),
                        indent: element.attributes.outline_indent.value
                    }

                    items.push(item);
                }

                return items;
            });

            function setup_elements()
            {
                if(outline_intersection_observer != null)
                {
                    outline_intersection_observer.disconnect();
                }

                outline_elements.value = [];

                if(props.target != null)
                {
                    search_elements(props.target);
                }

                if(outline_intersection_observer != null)
                {
                    for(const element of outline_elements.value)
                    {
                        outline_intersection_observer.observe(element);
                    }
                }
            }

            function is_outline_element(element)
            {
                if("id" in element && element.id != "" && "outline_label" in element.attributes && "outline_indent" in element.attributes)
                {
                    return true;
                }

                return false;
            }

            function is_hidden(element)
            {
                const depth_max = props.depth_max || 1;
                const depth = parseInt(element.attributes.outline_indent.value);

                return (depth > depth_max);
            }

            function is_child_of(child_id, parent)
            {
                const parent_depth = parseInt(parent.attributes.outline_indent.value);

                const parent_index = outline_elements.value.findIndex((element) =>
                {
                    return element.id == parent.id;
                });

                const child_index = outline_elements.value.findIndex((element) =>
                {
                    return element.id == child_id;
                });

                if(child_index < parent_index)
                {
                    return false;
                }

                for(let index = parent_index + 1; index <= child_index; index++)
                {
                    const element = outline_elements.value[index];
                    const element_depth = parseInt(element.attributes.outline_indent.value)

                    if(!is_hidden(element) || element_depth <= parent_depth)
                    {
                        return false;   
                    }
                }

                return true;
            }

            function search_elements(element)
            {
                if(is_outline_element(element))
                {
                    outline_elements.value.push(element);
                }

                for(const child of element.childNodes)
                {
                    search_elements(child);
                }
            }

            function on_elements_intersect(entities)
            {
                for(const entity of entities)
                {
                    if(!entity.isIntersecting)
                    {
                        delete outline_elements_visible[entity.target.id];
                    }

                    else
                    {
                        outline_elements_visible[entity.target.id] = entity;
                    }
                }

                let top_element = null;
                let top_offset = 0.0;

                for(const [key, entity] of Object.entries(outline_elements_visible))
                {
                    if(top_element == null)
                    {
                        top_element = entity.target;
                        top_offset = entity.target.offsetTop;
                    }

                    else
                    {
                        if(entity.target.offsetTop < top_offset)
                        {
                            top_element = entity.target;
                            top_offset = entity.target.offsetTop;
                        }
                    }
                }

                if(top_element != null)
                {
                    outline_element_active.value = top_element.id;
                }
            }

            outline_mutation_observer = new MutationObserver(records => setup_elements())
            outline_intersection_observer = new IntersectionObserver(entries => on_elements_intersect(entries), outline_intersection_options);

            watch(props, (old_state, new_state) =>
            {
                outline_mutation_observer.disconnect();

                if(props.target != null)
                {
                    outline_mutation_observer.observe(props.target, outline_mutation_options);
                }

                setup_elements();
            }, { immediate: true });

            return {
                outline_items
            }
        }
    };
</script>

<template>
    <nav ref="outline_container" class="nav flex-column align-items-stretch outline">
        <template v-for="item of outline_items">
            <a class="nav-link rounded-end" :class="item.active ? 'active' : ''" :outline_indent="item.indent" :style="'--outline_indent: ' + item.indent + 'px'" :href="item.link">{{ item.label }}</a>
        </template>
    </nav>
</template>