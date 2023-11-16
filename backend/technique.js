const Tag = require("./tag.js");
const Example = require("./example.js");
const fs = require("fs");

class Technique
{
    #name
    #description
    #date
    #tags

    #images
    #examples

    constructor()
    {
        this.#name = "";
        this.#description = "";
        this.#date = Date.now();

        this.#tags = [];
        this.#images = [];
        this.#examples = [];
    }

    load(database_path, technique_path)
    {
        let technique = JSON.parse(fs.readFileSync(database_path + technique_path + "description.json"));

        this.#name = technique.name;
        this.#description = technique.description;
        this.#date = technique.date;
        this.#tags = Tag.load(technique.tags, "technique");

        const image_directory = fs.readdirSync(database_path + technique_path + "images");
        const example_directory = fs.readdirSync(database_path + technique_path + "examples");
        
        for(const image_path of image_directory)
        {
            this.#images.push(database_path + technique_path + "images/" + image_path);
        }

        for(const example_path of example_directory)
        {
            let example = new Example();
            example.load(database_path, technique_path + "examples/" + example_path + "/");

            this.#examples.push(example);
        }
    }

    export()
    {
        let example_names = [];

        for(const example of this.#examples)
        {
            example_names.push(example.get_name());
        }

        return {
            name : this.#name,
            description : this.#description,
            date : this.#date,
            tags : Tag.export(this.#tags),
            images : this.#images,
            examples : example_names
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

    get_date()
    {
        return this.#date;
    }

    get_tags()
    {
        return this.#tags;
    }

    get_tags_combined()
    {
        let tags = this.#tags;

        for(const example of this.#examples)
        {
            for(const tag of example.get_tags())
            {
                if(!tags.some(value => value.is_equal(tag)))
                {
                    tags.push(tag);
                }
            }
        }

        return tags;
    }

    get_images()
    {
        return this.#images;
    }

    get_examples()
    {
        return this.#examples;
    }
}

module.exports = Technique;