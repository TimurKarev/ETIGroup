import det_cl_section from './vue/det_cl_section.vue'

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        message: 'Hello !',
        data: json_data
    },
    components: {
        det_cl_section: det_cl_section
    }
})