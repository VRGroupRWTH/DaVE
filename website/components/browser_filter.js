import BrowserFilterDate from "components/browser_filter_date.js"
import BrowserFilterTag from "components/browser_filter_tag.js"

export default
{
    components:
    {
        BrowserFilterDate,
        BrowserFilterTag
    },
    props: ["browser_filters"],
    emits: ["update:browser_filters"],
    template:
    `
    <div>
        <button class="btn btn-toggle border-0 w-100 d-flex align-items-end browser-filter-toggle-arrow" type="button" data-bs-toggle="collapse" data-bs-target="#browser_filter_collapse" aria-expanded="true">
            <img src="symbols/caret_down_fill.svg" width="20px">
            <div class="ms-1">Filters</div>
        </button>
        <div id="browser_filter_collapse" class="collapse show px-4">
            <ul class="list-unstyled mt-2">
                <li>
                    <label class="form-label" for="browser_filter_date">Date</label>
                    <browser-filter-date id="browser_filter_date" :browser_filters="browser_filters"></browser-filter-date>
                </li>
                <li>
                    <label class="form-label" for="browser_filter_tag">Tags</label>
                    <browser-filter-tag id="browser_filter_tag" :browser_filters="browser_filters"></browser-filter-tag>
                </li>
            </ul>
        </div>
    </div>
    `
}