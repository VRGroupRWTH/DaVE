import { Backend } from "./backend.js";
import express from "express";

function parse_string(name, fallback)
{
    const index = process.argv.indexOf("--" + name);

    if(index != -1 && (index + 1) < process.argv.length)
    {
        return process.argv[index + 1];
    }

    return fallback;
}

function parse_number(name, fallback)
{
    let string = parse_string(name, null);

    if(string)
    {
        return parseInt(string);
    }

    return fallback;
}

function parse_flag(name)
{
    const index = process.argv.indexOf("--" + name);

    return (index != -1)
}

const website = parse_string("website", null);
const database = parse_string("database", "../database/");
const port = parse_number("port", "8080");

const app = express();
app.use(express.json());
app.use("/database", express.static(database));

const backend = new Backend();
backend.setup(app, database);

if(website)
{
    app.use("/", express.static(website));

    app.get("/*", (request, response) => 
    {
        response.sendFile(process.cwd() + "/" + website + "index.html");
    });
}

app.listen(port, () =>
{
    console.log("Listening on port " + port);
});