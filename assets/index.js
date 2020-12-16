import Vue from "vue";

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/black-green-light.css'

Vue.use(VueMaterial)

import checklist_header from "./vue/components/checklist_header";
import app_toolbar from "./vue/components/app_toolbar";
import checklists_list from "./vue/components/checklists_list";

new Vue({
  el: "#app",
  delimiters: ['[[',']]'],
  components: {
    checklist_header,
    app_toolbar,
    checklists_list,
  },
  data: {
    data_det: g_checklist_data,
    header: g_checklist_name,
    checklists_list: g_checklists_list,
    toolbar_main_urls: g_toolbar_main_urls
  }
});