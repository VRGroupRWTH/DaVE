import { ref } from "vue"

export default
{
    props: ["browser_filter_date_min", "browser_filter_date_max"],
    setup(props)
    {
        function compute_date_range(date_min, date_max)
        {
            let date_range = 0;
            date_range += (date_max.getFullYear() - date_min.getFullYear()) * 12;
            date_range -= date_min.getMonth();
            date_range += date_max.getMonth();

            return Math.max(date_range, 0);
        }

        const browser_filter_date_min = new Date(props.browser_filter_date_min);
        const browser_filter_date_max = new Date(props.browser_filter_date_max);
        const browser_filter_date_range = compute_date_range(browser_filter_date_min, browser_filter_date_max);

        let browser_filter_date_value_min = ref(0);
        let browser_filter_date_value_max = ref(browser_filter_date_range - 1);
        let browser_filter_date_value_left = ref(browser_filter_date_value_min.value);
        let browser_filter_date_value_right = ref(browser_filter_date_value_max.value);

        function on_browser_filter_date_value_left_change()
        {
            const left_value = parseInt(browser_filter_date_value_left.value);
            const right_value = parseInt(browser_filter_date_value_right.value);

            if(left_value == parseInt(browser_filter_date_value_min.value))
            {
                return;
            }

            if(left_value >= right_value)
            {
                browser_filter_date_value_left.value = right_value - 1;   
            }
        }

        function on_browser_filter_date_value_right_change()
        {
            const left_value = parseInt(browser_filter_date_value_left.value);
            const right_value = parseInt(browser_filter_date_value_right.value);

            if(right_value == browser_filter_date_value_max.value)
            {
                return;
            }

            if(right_value <= left_value)
            {
                browser_filter_date_value_right.value = left_value + 1;   
            }
        }

        function compute_date_left_percentage()
        {
            const left_value = parseInt(browser_filter_date_value_left.value);

            const range = browser_filter_date_value_max.value - browser_filter_date_value_min.value;
            const percentage = ((left_value - browser_filter_date_value_min.value) / range) * 100;
            
            return percentage.toString() + "%";
        }

        function compute_date_right_percentage()
        {
            const right_value = parseInt(browser_filter_date_value_right.value);

            const range = browser_filter_date_value_max.value - browser_filter_date_value_min.value;
            const percentage = ((right_value - browser_filter_date_value_min.value) / range) * 100;
            
            return percentage.toString() + "%";
        }

        return {
            browser_filter_date_value_min,
            browser_filter_date_value_max,
            browser_filter_date_value_left,
            browser_filter_date_value_right,
            on_browser_filter_date_value_left_change,
            on_browser_filter_date_value_right_change,
            compute_date_left_percentage,
            compute_date_right_percentage
        }
    },
    template:
    `
    <div>
        <div class="browser-filter-date-slider-container">
            <div class="browser-filter-date-slider-track-outer" :style="'left: 0%; right: calc(100% - ' + compute_date_left_percentage() + ');'"></div>
            <div class="browser-filter-date-slider-track-inner" :style="'left: ' + compute_date_left_percentage() + '; right: calc(100% - ' + compute_date_right_percentage() + ');'"></div>
            <div class="browser-filter-date-slider-track-outer" :style="'left: ' + compute_date_right_percentage() + '; right: 0%;'"></div>
            <input class="form-range browser-filter-date-slider-input" style="z-index: 1;" type="range" :min="browser_filter_date_value_min" :max="browser_filter_date_value_max" v-model="browser_filter_date_value_left" @input="on_browser_filter_date_value_left_change">
            <input class="form-range browser-filter-date-slider-input" style="z-index: 2;" type="range" :min="browser_filter_date_value_min" :max="browser_filter_date_value_max" v-model="browser_filter_date_value_right" @input="on_browser_filter_date_value_right_change">
        </div>
        <div style="display: flex">
            <div style="position: relative; width: 60px; color: white; background: rgb(33, 37, 41); border-radius: 4px; font-size: calc(1rem * 0.75); text-align: center; padding: 4px; left: calc(25% - 30px); top: calc(25% + 20px);">Jan. 2023</div>
            <div style="position: relative; width: 60px; color: white; background: rgb(33, 37, 41); border-radius: 4px; font-size: calc(1rem * 0.75); text-align: center; padding: 4px; left: calc(75% - 30px); top: calc(25% + 20px);">Dec. 2023</div>


            <!--<div class="rounded text-bg-dark p-1">Jan. 2023</div>-->
        </div>
    </div>
    `
}