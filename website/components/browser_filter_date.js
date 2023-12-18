import { ref, computed } from "vue"

export default
{
    props: ["browser_filters"],
    emits: ["update:browser_filters"],
    setup(props, context)
    {
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

        const browser_filter_date_min = new Date(props.browser_filters.date_begin);
        const browser_filter_date_max = new Date(props.browser_filters.date_end);
        const browser_filter_date_range = compute_date_range(browser_filter_date_min, browser_filter_date_max);

        let browser_filter_date_value_min = ref(0);
        let browser_filter_date_value_max = ref(browser_filter_date_range);
        let browser_filter_date_value_left = computed(() => compute_date_range(browser_filter_date_min, new Date(props.browser_filters.date_begin)));
        let browser_filter_date_value_right = computed(() => compute_date_range(browser_filter_date_min, new Date(props.browser_filters.date_end)));

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

        function on_browser_filter_date_value_left_change(event)
        {
            let left_value = parseInt(event.target.value);

            if(left_value >= browser_filter_date_value_right.value)
            {
                event.target.value = browser_filter_date_value_right.value - 1;

                return;
            }

            let filters = props.browser_filters;
            filters.date_begin = compute_date_offset(browser_filter_date_min, left_value).toString();

            context.emit("update:browser_filters", filters);
        }

        function on_browser_filter_date_value_right_change(event)
        {
            let right_value = parseInt(event.target.value);

            if(right_value <= browser_filter_date_value_left.value)
            {
                event.target.value = browser_filter_date_value_left.value + 1;

                return;
            }

            let filters = props.browser_filters;
            filters.date_end = compute_date_offset(browser_filter_date_min, right_value).toString();

            context.emit("update:browser_filters", filters);
        }

        return {
            browser_filter_date_value_min,
            browser_filter_date_value_max,
            browser_filter_date_value_left,
            browser_filter_date_value_right,
            browser_filter_date_percentage_left,
            browser_filter_date_percentage_right,
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
        <div style="display: flex">
            <div style="position: relative; width: 60px; color: white; background: rgb(33, 37, 41); border-radius: 4px; font-size: calc(1rem * 0.75); text-align: center; padding: 4px; left: calc(25% - 30px); top: calc(25% + 20px);">Jan. 2023</div>
            <div style="position: relative; width: 60px; color: white; background: rgb(33, 37, 41); border-radius: 4px; font-size: calc(1rem * 0.75); text-align: center; padding: 4px; left: calc(75% - 30px); top: calc(25% + 20px);">Dec. 2023</div>
        </div>
    </div>
    `
}