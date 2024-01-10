const Tag = require("./tag.js");
const fs = require("fs");
const yaml = require("yaml");
const showdown = require("showdown");

class Visualization
{
    #name
    #date

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
        this.#date = visualization.date;

        if("technique_tags" in visualization)
        {
            this.#tags = this.#tags.concat(Tag.load(visualization.technique_tags, "technique"));
        }

        if("domain_tags" in visualization)
        {
            this.#tags = this.#tags.concat(Tag.load(visualization.domain_tags, "domain"));
        }

        if("images" in visualization)
        {
            for(const image of visualization.images)
            {
                this.#images.push(visualization_path + image);
            }
        }

        if("resources" in visualization)
        {
            for(const item of visualization.resources)
            {
                let resource = item;
                
                if("path" in resource)
                {
                    resource.path = visualization_path + resource.path;
                }

                this.#resources.push(resource);
            }
        }

        if("templates" in visualization)
        {
            this.#templates = visualization.templates;

            for(let t)

            for(const item of visualization.templates)
            {
                let template = item;
                template.trace = visualization_path + template.trace;
                template.script = visualization_path + template.script;

                if("path" in template.container)
                {
                    template.container.path = visualization_path + template.container;
                }

                this.#templates.push(template);                
            }
        }

        if("datasets" in visualization)
        {
            this.#datasets = visualization.datasets;

            for(let dataset of this.#datasets)
            {
                if("path" in dataset)
                {
                    dataset.path = visualization_path + dataset.path;
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

        const converter = new showdown.Converter();
        this.#description = converter.makeHtml(description_file);

        return true;
    }

    export()
    {
        return {
            name: this.#name,
            date: this.#date,
            tags: Tag.export(this.#tags),
            images: this.#images,
            resources: this.#resources,
            templates: this.#templates,
            dataset: this.#dataset,
            scene: this.#scene,
            description: this.#description
        }
    }

    get_name()
    {
        return this.#name;
    }

    get_date()
    {
        return this.#date;
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

    get_dataset()
    {
        return this.#dataset;
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

module.exports = Visualization;