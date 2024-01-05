function analyse_image(file)
{
    return { 
        ok: true,
        metadata: 
        {
            type: "image"
        }
    }
}

const file_types = 
[
    { analyse: analyse_image, extensions: ["bmp", "dib"], magic_numbers: [[0x42, 0x4D]] },
    { analyse: analyse_image, extensions: ["png"], magic_numbers: [[0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]] },
    { analyse: analyse_image, extensions: ["jpg", "jpeg", "jpe", "jif", "jfif", "jfi"] , magic_numbers: [[0xFF, 0xD8, 0xFF]] },
    { analyse: analyse_image, extensions: ["tiff", "tif"], magic_numbers: [[0x49, 0x49, 0x2A, 0x00], [0x4D, 0x4D, 0x00, 0x2A]] },
    { analyse: analyse_image, extensions: ["gif"], magic_numbers: [[0x47, 0x49, 0x46, 0x38, 0x37, 0x61], [0x47, 0x49, 0x46, 0x38, 0x39, 0x61]]},
    { analyse: analyse_image, extensions: ["tga", "icb", "vda", "vst"]},
    { analyse: analyse_image, extensions: ["webp"]},
    { analyse: analyse_image, extensions: ["pbm"], magic_numbers: [[0x50, 0x31], [0x50, 0x34]]},
    { analyse: analyse_image, extensions: ["pgm"], magic_numbers: [[0x50, 0x32], [0x50, 0x35]]},
    { analyse: analyse_image, extensions: ["ppm"], magic_numbers: [[0x50, 0x33], [0x50, 0x36]]},
    { analyse: analyse_image, extensions: ["exr"], magic_numbers: [[0x76, 0x2F, 0x31, 0x01]]},
    { analyse: analyse_image, extensions: ["exr"], magic_numbers: [[0x76, 0x2F, 0x31, 0x01]]},
    { analyse: analyse_image, extensions: ["dds"], magic_numbers: [[0x44, 0x44, 0x53, 0x20]]},
    { analyse: analyse_image, extensions: ["vti"] }
];

async function analyse_file(file)
{
    let metadata = 
    {
        type: "unkown",
        size: file.size
    }

    const file_extension_offset = file.name.lastIndexOf(".");

    if(file_extension_offset == -1)
    {
        return metadata;
    }

    const file_extension = file.name.substr(file_extension_offset + 1);

    for(const file_type of file_types)
    {
        let match_extension = true;
        let match_magic_number = true;

        if("extensions" in file_type)
        {
            match_extension = false;

            for(const extension of file_type.extensions)
            {
                if(extension == file_extension)
                {
                    match_extension = true;

                    break;
                }
            }
        }

        if("magic_numbers" in file_type)
        {
            match_magic_number = false;

            for(const magic_number of file_type.magic_numbers)
            {
                if(file.size < magic_number.length)
                {
                    continue;
                }

                const file_head = await file.slice(0, magic_number.length).arrayBuffer();
                const file_head_array = new Uint8Array(file_head);
                match_magic_number = true;

                for(let index = 0; index < file_head_array.length; index++)
                {
                    if(magic_number[index] != file_head_array[index])
                    {
                        match_magic_number = false;
    
                        break;
                    }
                }

                if(match_magic_number)
                {
                    break;
                }
            }
        }

        if(match_extension && match_magic_number)
        {
            const result = file_type.analyse(file);

            if(result.ok)
            {
                metadata = {...metadata, ...result.metadata};

                break;
            }
        }
    }

    return metadata;
}

export
{
    analyse_file
}