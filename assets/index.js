import Vue from "vue";

import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import checklist_header from "./vue/components/checklist_header";

new Vue({
  el: "#app",
  delimiters: ['[[',']]'],
  components: {
    checklist_header,
  },
  data: {
    data_det: checklist_data,
    header: checklist_name,
  }
});