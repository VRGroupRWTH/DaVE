import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { plugin as vite_plugin_markdown } from "vite-plugin-markdown";
import showdown from "showdown";
import showdown_highlight from "showdown-highlight";
import path from "path";

const syntax_highlight_config = 
{
    extensions: 
    [
        showdown_highlight(
        {
            pre: true,
            auto_detection: true
        })
    ]
};

const markdown_converter = new showdown.Converter(syntax_highlight_config);
markdown_converter.setOption("noHeaderId", "true");

const markdown_options = 
{
    mode: "vue",
    markdown: (body) => markdown_converter.makeHtml(body)
};

export default defineConfig(
{
    root: "./website/",
    build:
    {
        outDir: "../build/",
        emptyOutDir:  "../build/"
    },
    plugins: 
    [
        vue(),
        vite_plugin_markdown(markdown_options)
    ],
    resolve:
    {
        alias:
        {
            "~bootstrap": path.resolve(__dirname, "node_modules/bootstrap"),
            "~highlight.js": path.resolve(__dirname, "node_modules/highlight.js"),
            '@/': path.resolve(__dirname, './src')
        }
    },
    server: 
    {
        port: 8080,
        strictPort: true,
        proxy:
        {
            "/api": "http://localhost:8081",
            "/database": "http://localhost:8081"
        },
        watch: 
        {
            usePolling: true
        }
    },
    define:
    {
        global: {}
    },
})
