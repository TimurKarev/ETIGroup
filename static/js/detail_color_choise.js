const not_checked_color =  'white';
const not_used_color = 'grey';
const apply_color =  'green';
const comment_color = 'red';

document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll('.choise_color').forEach((elem)=> {
        if (elem.innerText === 'Не проверено'){

            elem.style.backgroundColor = not_checked_color;
        }
        if (elem.innerText === 'Не используется'){

            elem.style.backgroundColor = not_used_color;
        }
        if (elem.innerText === 'Принято'){

            elem.style.backgroundColor = apply_color;
        }
        if (elem.innerText === 'Замечания'){

            elem.style.backgroundColor = comment_color;
        }
    });


});