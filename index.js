const ServerPageBuilder = require("./backend/builder.js");
const ServerAPI = require("./backend/api.js");
const express = require("express");

const app = express();
const port = 8080;

const builder = new ServerPageBuilder();
const api = new ServerAPI();

app.use(express.json());
app.use("/styles.css", express.static("website/styles.css"));
app.use("/images", express.static("website/images/"));
app.use("/symbols", express.static("website/symbols/"));
app.use("/database", express.static("database/"));

builder.setup(app);
api.setup(app);

app.listen(port, () =>
{
    console.log("Listening on port " + port);
});