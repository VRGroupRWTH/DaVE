const Tag = require("./tag.js")
const fs = require("fs");

class Example
{
    #name
    #description
    #author
    #date
    #tags

    #images
    #resources

    constructor()
    {
        this.#name = "";
        this.#description = "";
        this.#author = "";
        this.#date = Date.now();

        this.#tags = [];
        this.#images = [];
        this.#resources = [];
    }

    load(database_path, example_path)
    {
        const example = JSON.parse(fs.readFileSync(database_path + example_path + "description.json"));

        this.#name = example.name;
        this.#description = example.description;
        this.#author = example.author;
        this.#date = example.date;
        this.#tags = Tag.load(example.tags, "example");

        const image_directory = fs.readdirSync(database_path + example_path + "images");
        const resource_directory = fs.readdirSync(database_path + example_path + "resources");
        
        for(const image_path of image_directory)
        {
            this.#images.push(database_path + example_path + "images/" + image_path);
        }

        for(const resource_path of resource_directory)
        {
            this.#resources.push(database_path + example_path + "resources/" + resource_path);
        }
    }

    export()
    {
        return {
            name : this.#name,
            description : this.#description,
            author : this.#author,
            date : this.#date,
            tags : Tag.export(this.#tags),
            images : this.#images,
            resources : this.#resources
        }
    }

    get_name()
    {
        return this.#name;
    }

    get_description()
    {
        return this.#description;
    }

    get_author()
    {
        return this.#author;
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
}

module.exports = Example;