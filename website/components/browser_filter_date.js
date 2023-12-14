export default
{
    setup()
    {

    },
    template:
    `
    <div>
        <div style="position: relative; height: 1rem;">
            <div></div>
            <div></div>
            <div></div>
            <input class="form-range" type="range" min="1" max="100" value="25" style="position: absolute; pointer-events: none; z-index: 1">
            <input class="form-range" type="range" min="1" max="100" value="75" style="position: absolute; pointer-events: none; z-index: 2">    
        </div>
        <div style="position: relative;">
            <div style="position: absolute; width: 60px; color: white; background: rgb(33, 37, 41); border-radius: 4px; font-size: 12px; text-align: center; padding: 4px; left: calc(25% - 30px); top: calc(25% + 20px);">Jan. 2023</div>
            <div style="position: absolute; width: 60px; color: white; background: rgb(33, 37, 41); border-radius: 4px; font-size: 12px; text-align: center; padding: 4px; left: calc(75% - 30px); top: calc(25% + 20px);">Dec. 2023</div>
        </div>
    </div>
    `
}