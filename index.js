const Backend = require("./backend/backend.js");
const express = require("express");
const fs = require("fs");

const app = express();
const port = 8080;

app.use(express.json());
app.use("/styles.css", express.static("website/styles.css"));
app.use("/favicon.png", express.static("website/favicon.png"));
app.use("/images", express.static("website/images/"));
app.use("/symbols", express.static("website/symbols/"));
app.use("/components", express.static("website/components/"));
app.use("/database", express.static("database/"));

const backend = new Backend();
backend.setup(app);

app.get("/", async (request, response) => 
{
    response.redirect("/home");
});

app.get("/:page_name", async (request, response) => 
{
    const page_directory = fs.readdirSync("./website/pages/");
    let page_content = null;
    let page_name = request.params.page_name + ".html";

    for(const page of page_directory)
    {
        if(page == page_name)
        {
            page_content = fs.readFileSync("./website/pages/" + page);

            break;
        }
    }

    if(page_content == null)
    {
        response.sendStatus(404);

        return;
    }

    let page_buffer = "<!DOCTYPE html>";
    page_buffer += "<html>";
    page_buffer += fs.readFileSync("website/head.html", "utf8");
    page_buffer += page_content;
    page_buffer += "</html>";

    response.send(page_buffer);
});

app.listen(port, () =>
{
    console.log("Listening on port " + port);
});