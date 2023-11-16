const fs = require("fs");

class ServerPageBuilder
{
    #home_buffer
    #wizzard_buffer
    #browser_buffer
    #technique_buffer
    #about_buffer

    constructor()
    {
        this.#home_buffer = "";
        this.#wizzard_buffer = "";
        this.#browser_buffer = "";
        this.#technique_buffer = "";
        this.#about_buffer = "";
    }

    setup(app)
    {
        //For deployment
        //this.#home_buffer = this.#load_page("home", false, true);
        //this.#wizzard_buffer = this.#load_page("wizzard", true, true);
        //this.#browser_buffer = this.#load_page("browser", false, true);
        //this.#technique_buffer = this.#load_page("technique", true, true);
        //this.#about_buffer = this.#load_page("about", true, true);

        app.get("/", async (request, response) => this.#on_home_request(request, response));
        app.get("/wizzard", async (request, response) => this.#on_wizzard_request(request, response));
        app.get("/browser", async (request, response) => this.#on_browser_request(request, response));
        app.get("/technique", async (request, response) => this.#on_technique_request(request, response));
        app.get("/about", async (request, response) => this.#on_about_request(request, response));
    }

    #load_page(page, use_header, use_footer)
    {
        let page_buffer = "<!DOCTYPE html>";
        page_buffer += "<html>";
        page_buffer += fs.readFileSync("website/head.html", "utf8");
        page_buffer += "<body>";

        if(use_header)
        {
            page_buffer += fs.readFileSync("website/modules/header.html", "utf8");
            page_buffer += "<script>";
            page_buffer += fs.readFileSync("website/modules/header.js", "utf8");
            page_buffer += "</script>";
        }

        page_buffer += fs.readFileSync("website/pages/" + page + ".html", "utf8");
        page_buffer += "<script>";
        page_buffer += fs.readFileSync("website/pages/" + page + ".js", "utf8");
        page_buffer += "</script>";

        if(use_footer)
        {
            page_buffer += fs.readFileSync("website/modules/footer.html", "utf8");
            page_buffer += "<script>";
            page_buffer += fs.readFileSync("website/modules/footer.js", "utf8");
            page_buffer += "</script>";
        }

        page_buffer += "</body>";
        page_buffer += "</html>";

        return page_buffer;
    }

    async #on_home_request(request, response)
    {
        //For debug only
        this.#home_buffer = this.#load_page("home", false, true);

        response.send(this.#home_buffer);
    }

    async #on_wizzard_request(request, response)
    {
        //For debug only
        this.#wizzard_buffer = this.#load_page("wizzard", true, true);

        response.send(this.#wizzard_buffer);
    }

    async #on_browser_request(request, response)
    {
        //For debug only
        this.#browser_buffer = this.#load_page("browser", false, true);

        response.send(this.#browser_buffer);
    }

    async #on_technique_request(request, response)
    {
        //For debug only
        this.#technique_buffer = this.#load_page("technique", true, true);

        response.send(this.#technique_buffer);
    }

    async #on_about_request(request, response)
    {
        //For debug only
        this.#about_buffer = this.#load_page("about", true, true);

        response.send(this.#about_buffer);
    }
}

module.exports = ServerPageBuilder;