const Tag = require("./tag.js");
const fs = require("fs");
const yaml = require("yaml");
const showdown = require("showdown");

class Technique
{
    #name
    #date

    #tags
    #images
    #resources

    #templates
    #dataset

    #description

    constructor()
    {
        this.#name = "";
        this.#date = Date.now();

        this.#tags = [];
        this.#images = [];
        this.#resources = [];

        this.#templates = [];
        this.#dataset = {};

        this.#description = "";
    }

    load(technique_path)
    {
        let technique_file = "";

        try
        {
            technique_file = fs.readFileSync(technique_path + "technique.yaml").toString();
        }

        catch(exception)
        {
            console.log("Can't load file '" + technique_path + "technique.yaml" + "'");

            return false;
        }

        let technique = yaml.parse(technique_file);

        this.#name = technique.name;
        this.#date = technique.date;

        if("technique_tags" in technique)
        {
            this.#tags = this.#tags.concat(Tag.load(technique.technique_tags, "technique"));
        }

        if("domain_tags" in technique)
        {
            this.#tags = this.#tags.concat(Tag.load(technique.domain_tags, "domain"));
        }

        if("images" in technique)
        {
            for(const image of technique.images)
            {
                this.#images.push(technique_path + image);
            }
        }

        if("resources" in technique)
        {
            for(const item of technique.resources)
            {
                let resource = item;
                
                if("path" in resource)
                {
                    resource.path = technique_path + resource.path;
                }

                this.#resources.push(resource);
            }
        }

        if("templates" in technique)
        {
            for(const item of technique.templates)
            {
                let template = item;
                template.trace = technique_path + template.trace;
                template.script = technique_path + template.script;

                if("path" in template.container)
                {
                    template.container.path = technique_path + template.container;
                }

                this.#templates.push(template);                
            }
        }

        if("dataset" in technique)
        {
            if("path" in technique.dataset)
            {
                technique.dataset.path = technique_path + technique.dataset.path;
            }
        }

        let description_file = "";

        try
        {
            description_file = fs.readFileSync(technique_path + "description.md").toString();
        }

        catch(exception)
        {
            console.log("Can't load file '" + technique_path + "description.md" + "'");

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

    get_description()
    {
        return this.#description;
    }
}

module.exports = Technique;