import { ref } from "vue"
import BrowserFilterDate from "components/browser_filter_date.js"
import BrowserFilterTag from "components/browser_filter_tag.js"

export default
{
    components :
    {
        BrowserFilterDate,
        BrowserFilterTag
    },
    props: ["browser_filter_date_begin", "browser_filter_date_end", "browser_filter_tags"],
    emits: ["on_browser_filter_date_begin_change", "on_browser_filter_date_end_change", "on_browser_filter_tags_change"],
    template:
    `
    <div>
        <button class="btn btn-toggle border-0 w-100 d-flex align-items-end browser-filter-toggle-arrow" type="button" data-bs-toggle="collapse" data-bs-target="#browser_filter_bar_collapse">
            <img src="symbols/caret_down_fill.svg" width="20px">
            <div class="ms-1">Filters</div>
        </button>
        <div id="browser_filter_bar_collapse" class="collapse px-4 pt-2">
            <ul class="list-unstyled">
                <li>
                    <label class="form-label" for="browser_filter_date">Date</label>
                    <browser-filter-date id="browser_filter_date" :browser_filter_date_begin="browser_filter_date_begin" :browser_filter_date_end="browser_filter_date_end" @on_browser_filter_date_begin_change="on_browser_filter_date_begin_change" @on_browser_filter_date_end_change="on_browser_filter_date_end_change"></browser-filter-date>
                </li>
                <li>
                    <label class="form-label" for="browser_filter_tag">Tags</label>
                    <browser-filter-tag id="browser_filter_tag" :browser_filter_tags="browser_filter_tags" @on_browser_filter_tags_change="on_browser_filter_tags_change"></browser-filter-tag>
                </li>
            </ul>
        </div>
    </div>
    `
}