import { Tag } from "./tag.js";
import fs from "fs";
import yaml from "yaml";
import showdown from "showdown";
import showdown_highlight from "showdown-highlight";

export class Visualization
{
    #name
    #date
    #authors

    #tags
    #images
    #resources

    #templates
    #datasets

    #scene
    #description

    constructor()
    {
        this.#name = "";
        this.#date = Date.now();
        this.#authors = [];

        this.#tags = [];
        this.#images = [];
        this.#resources = [];

        this.#templates = [];
        this.#datasets = [];

        this.#scene = "";
        this.#description = "";
    }

    load(visualization_path)
    {
        if(!this.#load_visualization(visualization_path))
        {
            return false;
        }

        if(!this.#load_description(visualization_path))
        {
            return false;
        }

        fs.watchFile(visualization_path + "visualization.yaml", (old_state, new_state) =>
        {
            console.log("Reloaded: " + visualization_path + "visualization.yaml");

            this.#load_visualization(visualization_path);
        });

        fs.watchFile(visualization_path + "description.md", (old_state, new_state) =>
        {
            console.log("Reloaded: " + visualization_path + "description.md");

            this.#load_description(visualization_path);
        });

        return true;
    }

    #load_visualization(visualization_path)
    {
        let visualization_file = "";

        try
        {
            visualization_file = fs.readFileSync(visualization_path + "visualization.yaml").toString();
        }

        catch(exception)
        {
            console.log("Can't load file '" + visualization_path + "visualization.yaml" + "'");

            return false;
        }

        let visualization = yaml.parse(visualization_file);

        this.#name = visualization.name;
        this.#date = new Date(visualization.date);
        this.#authors = [];
        this.#tags = [];
        this.#images = [];
        this.#resources = [];
        this.#templates = [];
        this.#datasets = [];
        this.#scene = "";

        if("authors" in visualization && visualization.authors != null)
        {
            this.#authors = visualization.authors;
        }

        if("tags" in visualization && visualization.tags != null)
        {
            this.#tags = Tag.import(visualization.tags);
        }

        if("images" in visualization && visualization.images != null)
        {
            this.#images = visualization.images;

            for(let index = 0; index < this.#images.length; index++)
            {
                this.#images[index] = visualization_path + this.#images[index];
            }
        }

        if("resources" in visualization && visualization.resources != null)
        {
            this.#resources = visualization.resources;

            for(let index = 0; index < this.#resources.length; index++)
            {
                if("path" in this.#resources[index])
                {
                    this.#resources[index].path = visualization_path + this.#resources[index].path;
                }
            }
        }

        if("templates" in visualization && visualization.templates != null)
        {
            this.#templates = visualization.templates;

            for(let index = 0; index < this.#templates.length; index++)
            {
                this.#templates[index].trace = visualization_path + this.#templates[index].trace;
                this.#templates[index].script = visualization_path + this.#templates[index].script;

                if("path" in this.#templates[index].container)
                {
                    this.#templates[index].container.path = visualization_path + this.#templates[index].container;
                }
            }
        }

        if("datasets" in visualization && visualization.datasets != null)
        {
            this.#datasets = visualization.datasets;

            for(let index = 0; index < this.#datasets.length; index++)
            {
                if("path" in this.#datasets[index])
                {
                    this.#datasets[index].path = visualization_path + this.#datasets[index].path;
                }
            }
        }

        if("scene" in visualization)
        {
            this.#scene = visualization_path + visualization.scene;
        }

        return true;
    }

    #load_description(visualization_path)
    {
        let description_file = "";

        try
        {
            description_file = fs.readFileSync(visualization_path + "description.md").toString();
        }

        catch(exception)
        {
            console.log("Can't load file '" + visualization_path + "description.md" + "'");

            return false;
        }

        const syntax_highlight_config = 
        {
            extensions: 
            [
                showdown_highlight(
                {
                    pre: true,
                    auto_detection: true
                })
            ]
        };

        let converter = new showdown.Converter(syntax_highlight_config);
        converter.setOption("noHeaderId", "true");

        this.#description = converter.makeHtml(description_file);

        return true;
    }

    export()
    {
        return {
            name: this.#name,
            date: this.#date.toString(),
            authors: this.#authors,
            tags: Tag.export(this.#tags),
            images: this.#images,
            resources: this.#resources,
            templates: this.#templates,
            datasets: this.#datasets,
            scene: this.#scene,
            description: this.#description
        }
    }

    supports_docker()
    {
        for(const template of this.#templates)
        {
            if(template.techniques.some(technique => technique == "docker"))
            {
                return true;
            }
        }

        return false;
    }

    supports_singularity()
    {
        for(const template of this.#templates)
        {
            if(template.techniques.some(technique => technique == "singularity"))
            {
                return true;
            }
        }

        return false;
    }

    supports_local()
    {
        for(const template of this.#templates)
        {
            if(template.commands.some(command => command.type == "local"))
            {
                return true;
            }
        }

        return false;
    }

    supports_mpi()
    {
        for(const template of this.#templates)
        {
            if(template.commands.some(command => command.type == "mpi"))
            {
                return true;
            }
        }

        return false;
    }

    supports_slurm()
    {
        for(const template of this.#templates)
        {
            if(template.commands.some(command => command.type == "slurm"))
            {
                return true;
            }
        }

        return false;
    }

    get_name()
    {
        return this.#name;
    }

    get_date()
    {
        return this.#date;
    }

    get_authors()
    {
        return this.#authors;
    }

    get_tags()
    {
        return this.#tags;
    }

    get_images()
    {
        return this.#images;
    }

    get_resources()
    {
        return this.#resources;
    }

    get_templates()
    {
        return this.#templates;
    }

    get_datasets()
    {
        return this.#datasets;
    }

    get_scene()
    {
        return this.#scene;
    }

    get_description()
    {
        return this.#description;
    }
}