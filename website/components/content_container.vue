<script>
    import { ref, watch } from "vue";
    import * as bootstrap from "bootstrap";

    export default
    {
        setup()
        {
            let content_container = ref(null);

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

            function get_section_id(section_ids, heading)
            {
                let section_id_base = heading.replaceAll(" ", "_").replace(/\W/g, "");
                let section_id = section_id_base;

                for(let index = 1; section_ids.includes(section_id); index++)
                {
                    section_id = section_id_base + "_" + index;
                }

                return section_id;
            }

            function create_sections()
            {
                if(content_container.value == null)
                {
                    return;
                }

                let base = content_container.value;

                while(true)
                {
                    if(base.children.length != 1)
                    {
                        break;
                    }

                    const child = base.children[0];

                    if("outline_label" in child.attributes)
                    {
                        break;
                    }

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
                let section_ids = [];
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

                        let section_id = get_section_id(section_ids, child.innerHTML);
                        section_ids.push(section_id);

                        section = document.createElement("div");
                        section.id = section_id;
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

            function build_clipboard(code)
            {
                let clipboard = "";

                for(const node of code.childNodes)
                {
                    if(node.nodeType == Node.TEXT_NODE)
                    {
                        clipboard += node.nodeValue;
                    }

                    else
                    {
                        clipboard += build_clipboard(node);
                    }
                }

                return clipboard;
            }

            function on_clipboard_click(button, code)
            {
                const clipboard = build_clipboard(code);
                navigator.clipboard.writeText(clipboard);

                const tooltip = new bootstrap.Tooltip(button);
                tooltip.show();

                button.onclick = () => {};
                setTimeout(() => on_clipboard_timeout(button, tooltip, code), 2000);
            }

            function on_clipboard_timeout(button, tooltip, code)
            {
                const on_clipboard_dispose = () =>
                {
                    tooltip.dispose();
                    button.onclick = () => on_clipboard_click(button, code);
                    button.removeEventListener("hidden.bs.tooltip", on_clipboard_dispose);
                };

                button.addEventListener("hidden.bs.tooltip", on_clipboard_dispose);
                tooltip.hide();
            }

            function create_clipboard_buttons()
            {
                const elements = content_container.value.getElementsByTagName("pre");

                for(const element of elements)
                {
                    const buttons = element.getElementsByTagName("button");
                    const codes = element.getElementsByTagName("code");

                    if(codes.length <= 0)
                    {
                        continue;
                    }

                    for(const button of buttons)
                    {
                        button.remove();
                    }

                    const button = document.createElement("button");
                    button.innerHTML = "<img src='/images/copy_clipboard.svg' style='width: 18px; height: 18px'>";
                    button.setAttribute("data-bs-title", "Copied!");
                    button.setAttribute("data-bs-placement", "left");
                    button.setAttribute("data-bs-trigger", "manual");
                    button.onclick = () => on_clipboard_click(button, codes[0]);
                    
                    element.style.position = "relative";
                    element.append(button)
                }
            }

            function create_anchor_links()
            {
                const elements = content_container.value.querySelectorAll("h1, h2, h3, h4, h5, h6");

                for(const element of elements)
                {
                    const links = element.getElementsByTagName("a");
                    
                    for(const link of links)
                    {
                        link.remove();
                    }

                    const link = document.createElement("a");
                    link.innerHTML = "<img src='/images/link_45deg.svg' style='width: round(down, 1lh - 4px, 2px); position: absolute; top: 0.25lh;'>";
                    link.href = "#" + element.parentNode.id;

                    element.append(link);
                }
            }

            const content_mutation_options = 
            {
                subtree: true,
                childList: true
            };

            let content_mutation_observer = new MutationObserver(records =>
            {
                create_sections();
                create_clipboard_buttons();
                create_anchor_links();

                content_mutation_observer.takeRecords();
            });

            watch(content_container, (old_state, new_state) =>
            {
                content_mutation_observer.disconnect();

                if(content_container.value != null)
                {
                    content_mutation_observer.observe(content_container.value, content_mutation_options);
                }

                create_sections();
            }, { immediate: true });

            return {
                content_container
            };
        }  
    };
</script>

<template>
    <div ref="content_container">
        <slot></slot>
    </div>
</template>