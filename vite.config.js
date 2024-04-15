import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { plugin as vite_plugin_markdown } from "vite-plugin-markdown";
import showdown from "showdown";
import path from "path";

const markdown_converter = new showdown.Converter();
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
