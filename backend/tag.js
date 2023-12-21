class Tag
{
    #name
    #type

    constructor(name, type)
    {
        this.#name = name;
        this.#type = type;
    }

    static load(names, type)
    {
        let tags = [];

        for(const name of names)
        {
            if(!tags.some(value => value == name))
            {
                const tag = new Tag(name, type);

                tags.push(tag);
            }
        }

        return tags;
    }

    static import(objects)
    {
        let tags = [];

        for(const object of objects)
        {
            const tag = new Tag(object.name, object.type);

            tags.push(tag);
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
            type: this.#type
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