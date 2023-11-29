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

    #commands
    #container
    #dataset

    #description

    constructor()
    {
        this.#name = "";
        this.#date = Date.now();

        this.#tags = [];
        this.#images = [];
        this.#resources = [];

        this.#commands = [];
        this.#container = {};
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
            for(const resource of technique.resources)
            {
                this.#resources.push(technique_path + resource);
            }
        }

        this.#commands = technique.commands;
        this.#container = technique.container;
        this.#dataset = technique.datset;

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
            name : this.#name,
            date : this.#date,
            tags : Tag.export(this.#tags),
            images : this.#images,
            resources : this.#resources,
            description : this.#description
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

    get_description()
    {
        return this.#description;
    }
}

module.exports = Technique;