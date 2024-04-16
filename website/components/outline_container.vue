<script>
    import { ref, watch } from "vue";

    export default
    {
        setup()
        {
            let outline_container = ref(null);

            function is_heading(tag)
            {
                switch(tag.toLowerCase())
                {
                case "h1":
                case "h2":
                case "h3":
                case "h4":
                case "h5":
                case "h6":
                    return true;
                default:
                    break;
                }

                return false;
            }

            function get_heading_number(tag)
            {
                switch(tag.toLowerCase())
                {
                case "h1":
                    return 1;
                case "h2":
                    return 2;
                case "h3":
                    return 3;
                case "h4":
                    return 4;
                case "h5":
                    return 5;
                case "h6":
                    return 6;
                default:
                    break;
                }

                return null;
            }

            function get_section_id(heading)
            {
                return heading.replaceAll(" ", "_").replace(/\W/g, "");
            }

            function create_sections()
            {
                if(outline_container.value == null)
                {
                    return;
                }

                let base = outline_container.value;

                while(true)
                {
                    if(base.children.length != 1)
                    {
                        break;
                    }

                    const child = base.children[0];

                    if(is_heading(child.tagName))
                    {
                        break;
                    }

                    base = child;
                }

                let child_list = base.children;

                for(let child_index = 0; child_index < child_list.length;)
                {
                    const child = child_list[child_index];

                    if(child.hasAttribute("outline_label"))
                    {
                        while(child.children.length > 0)
                        {
                            const inner = child.children[0];

                            inner.remove();
                            child.before(inner);
                        }

                        child.remove();
                    }

                    else
                    {
                        child_index++;
                    }
                }

                let section = null;
                let section_stack = [];

                for(let child_index = 0; child_index < child_list.length;)
                {
                    const child = child_list[child_index];

                    if(is_heading(child.tagName))
                    {
                        const current_number = get_heading_number(child.tagName);

                        while(section_stack.length > 0)
                        {
                            const parent_number = section_stack[section_stack.length - 1];

                            if(parent_number >= current_number)
                            {
                                section_stack.pop();
                            }

                            else
                            {
                                break;
                            }
                        }

                        section_stack.push(current_number);
                        const section_indent = section_stack.length - 1;

                        section = document.createElement("div");
                        section.id = get_section_id(child.innerHTML);
                        section.setAttribute("outline_label", child.innerHTML);
                        section.setAttribute("outline_indent", section_indent.toString());

                        child.before(section);
                        child_index++;
                    }

                    if(section != null)
                    {
                        child.remove();
                        section.append(child);
                    }

                    else
                    {
                        child_index++;
                    }
                }
            }

            const outline_mutation_options = 
            {
                subtree: true,
                childList: true
            };

            let outline_mutation_observer = new MutationObserver(records =>
            {
                create_sections();

                outline_mutation_observer.takeRecords();
            });

            watch(outline_container, (old_state, new_state) =>
            {
                outline_mutation_observer.disconnect();

                if(outline_container.value != null)
                {
                    outline_mutation_observer.observe(outline_container.value, outline_mutation_options);
                }

                create_sections();
            }, { immediate: true });

            return {
                outline_container
            };
        }  
    };
</script>

<template>
    <div ref="outline_container">
        <slot></slot>
    </div>
</template>