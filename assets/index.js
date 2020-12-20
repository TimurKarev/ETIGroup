import Vue from "vue";
import vuetify from './plugins/vuetify' // path to vuetify export
import VueRouter from 'vue-router'

import app_toolbar from "./vue/components/app_toolbar";
import checklists_list from "./vue/components/checklists_list";

Vue.use(VueRouter)
Vue.prototype.$eventHub = new Vue();

new Vue({
  vuetify,
  el: "#app",
  delimiters: ['[[',']]'],
  components: {
    app_toolbar,
    checklists_list
  },
  data: {
    data_det: g_checklist_data,
    header: g_checklist_name,
    checklists_list: g_checklists_list,
    toolbar_main_urls: g_toolbar_main_urls
  }
});