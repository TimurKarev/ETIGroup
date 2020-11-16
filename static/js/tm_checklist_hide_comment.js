document.addEventListener('DOMContentLoaded', () =>{
    const one = document.querySelector('.sktm_table')
        console.log(one);
        one.onchange = () => {
            console.log(this);
        }
});