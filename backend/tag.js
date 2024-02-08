class Tag
{
    #name
    #type
    #abbreviation

    constructor(name, type, abbreviation)
    {
        this.#name = name;
        this.#type = type;
        this.#abbreviation = abbreviation;
    }

    static import(objects)
    {
        let tags = [];

        for(const object of objects)
        {
            const name = object.name;
            const type = object.type;
            let abbreviation = "";

            if("abbreviation" in object)
            {
                abbreviation = object.abbreviation;
            }

            const tag = new Tag(name, type, abbreviation);

            if(!tags.some(item => item.is_equal(tag)))
            {
                tags.push(tag);
            }
        }

        return tags;
    }

    static export(tags)
    {
        let objects = [];

        for(const tag of tags)
        {
            objects.push(tag.export());
        }

        return objects;
    }

    export()
    {
        return {
            name: this.#name,
            type: this.#type,
            abbreviation: this.#abbreviation
        }
    }

    get_name()
    {
        return this.#name;
    }

    get_type()
    {
        return this.#type;
    }

    is_equal(tag)
    {
        return (this.#name == tag.get_name() && this.#type == tag.get_type());
    }
}

module.exports = Tag;