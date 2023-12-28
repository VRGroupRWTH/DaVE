import { ref, computed } from "vue"

export default
{
    props: ["browser_filters"],
    emits: ["update:browser_filters"],
    setup(props, context)
    {
        const date_month_abbreviations = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."];

        function compute_date_range(date_min, date_max)
        {
            let date_range = 0;
            date_range += (date_max.getFullYear() - date_min.getFullYear()) * 12;
            date_range -= date_min.getMonth();
            date_range += date_max.getMonth();

            return Math.max(date_range, 0);
        }

        function compute_date_offset(date, months)
        {
            let date_offset = new Date(date);
            date_offset.setMonth((date.getMonth() + months) % 12);
            date_offset.setFullYear(date.getFullYear() + months / 12);

            if(date.getMonth() + months % 12 >= 12)
            {
                date_offset.setFullYear(date_offset.getFullYear() + 1);
            }

            return date_offset;
        }

        const browser_filter_date_min = computed(() => new Date(props.browser_filters.date_min));
        const browser_filter_date_max = computed(() => new Date(props.browser_filters.date_max));
        const browser_filter_date_range = computed(() => compute_date_range(browser_filter_date_min.value, browser_filter_date_max.value));

        let browser_filter_date_value_min = ref(0);
        let browser_filter_date_value_max = computed(() => browser_filter_date_range.value);
        let browser_filter_date_value_left = computed(() => compute_date_range(browser_filter_date_min.value, new Date(props.browser_filters.date_begin)));
        let browser_filter_date_value_right = computed(() => compute_date_range(browser_filter_date_min.value, new Date(props.browser_filters.date_end)));

        let browser_filter_date_percentage_left = computed(() =>
        {
            const left_value = browser_filter_date_value_left.value;

            const range = browser_filter_date_value_max.value - browser_filter_date_value_min.value;
            const percentage = ((left_value - browser_filter_date_value_min.value) / range) * 100;
            
            return percentage.toString() + "%";
        });

        let browser_filter_date_percentage_right = computed(() =>
        {
            const right_value = browser_filter_date_value_right.value;

            const range = browser_filter_date_value_max.value - browser_filter_date_value_min.value;
            const percentage = ((right_value - browser_filter_date_value_min.value) / range) * 100;
            
            return percentage.toString() + "%";
        });

        let browser_filter_date_name_left = computed(() =>
        {
            const date_begin = new Date(props.browser_filters.date_begin);

            return date_month_abbreviations[date_begin.getMonth()] + " " + date_begin.getFullYear();
        });

        let browser_filter_date_name_right = computed(() =>
        {
            const date_begin = new Date(props.browser_filters.date_end);

            return date_month_abbreviations[date_begin.getMonth()] + " " + date_begin.getFullYear();
        });

        function on_browser_filter_date_value_left_change(event)
        {
            let left_value = parseInt(event.target.value);

            if(left_value >= browser_filter_date_value_right.value)
            {
                left_value = browser_filter_date_value_right.value - 1;
                event.target.value = left_value;
            }

            let filters = props.browser_filters;
            filters.date_begin = compute_date_offset(browser_filter_date_min.value, left_value).toString();

            context.emit("update:browser_filters", filters);
        }

        function on_browser_filter_date_value_right_change(event)
        {
            let right_value = parseInt(event.target.value);

            if(right_value <= browser_filter_date_value_left.value)
            {
                right_value = browser_filter_date_value_left.value + 1;
                event.target.value = right_value;
            }

            let filters = props.browser_filters;
            filters.date_end = compute_date_offset(browser_filter_date_min.value, right_value).toString();

            context.emit("update:browser_filters", filters);
        }

        return {
            browser_filter_date_value_min,
            browser_filter_date_value_max,
            browser_filter_date_value_left,
            browser_filter_date_value_right,
            browser_filter_date_percentage_left,
            browser_filter_date_percentage_right,
            browser_filter_date_name_left,
            browser_filter_date_name_right,
            on_browser_filter_date_value_left_change,
            on_browser_filter_date_value_right_change
        }
    },
    template:
    `
    <div>
        <div class="browser-filter-date-slider-container">
            <div class="browser-filter-date-slider-track-outer" :style="'left: 0%; right: calc(100% - ' + browser_filter_date_percentage_left + ');'"></div>
            <div class="browser-filter-date-slider-track-inner" :style="'left: ' + browser_filter_date_percentage_left + '; right: calc(100% - ' + browser_filter_date_percentage_right + ');'"></div>
            <div class="browser-filter-date-slider-track-outer" :style="'left: ' + browser_filter_date_percentage_right + '; right: 0%;'"></div>
            <input class="form-range browser-filter-date-slider-input" style="z-index: 1;" type="range" :min="browser_filter_date_value_min" :max="browser_filter_date_value_max" :value="browser_filter_date_value_left" @input="on_browser_filter_date_value_left_change($event)">
            <input class="form-range browser-filter-date-slider-input" style="z-index: 2;" type="range" :min="browser_filter_date_value_min" :max="browser_filter_date_value_max" :value="browser_filter_date_value_right" @input="on_browser_filter_date_value_right_change($event)">
        </div>
        <div class="browser-filter-date-label-container">
            <div class="rounded text-bg-dark d-flex align-items-center justify-content-center browser-filter-date-label-left" :style="'--label-left: ' + browser_filter_date_percentage_left + '; --label-right: ' + browser_filter_date_percentage_right + ';'">{{ browser_filter_date_name_left }}</div>
            <div class="rounded text-bg-dark d-flex align-items-center justify-content-center browser-filter-date-label-right" :style="'--label-left: ' + browser_filter_date_percentage_left + '; --label-right: ' + browser_filter_date_percentage_right + ';'">{{ browser_filter_date_name_right }}</div>
        </div>
    </div>
    `
}