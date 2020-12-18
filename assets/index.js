import Vue from "vue";

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

import app_toolbar from "./vue/components/app_toolbar";


new Vue({
  el: "#app",
  delimiters: ['[[',']]'],
  components: {
    app_toolbar,
  },
  data: {
    data_det: g_checklist_data,
    header: g_checklist_name,
    checklists_list: g_checklists_list,
    toolbar_main_urls: g_toolbar_main_urls
  }
});