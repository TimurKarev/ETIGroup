import Vue from "vue";
import vuetify from './plugins/vuetify' // path to vuetify export
import VueRouter from 'vue-router'

import app_toolbar from "./vue/components/app_toolbar";
import checklists_list from "./vue/components/checklists_list";
import action_button from "./vue/components/action_button";
import nav_driver from "./vue/components/nav_driver";
import order_config from "./vue/components/order_config";
import order_create from "./vue/components/order_create";
import checklist_config_update from "./vue/components/checklist_config_update";

Vue.use(VueRouter)
Vue.prototype.$eventHub = new Vue();

new Vue({
  vuetify,
  el: "#app",
  delimiters: ['[[',']]'],
  components: {
    app_toolbar,
    checklists_list,
    action_button,
    nav_driver,
    order_config,
    order_create,
    checklist_config_update,
  },
  data: {
    data_det: g_checklist_data,
    header: g_checklist_name,
    checklists_list: g_checklists_list,
    toolbar_data: g_toolbar_data,
    nav_driver_data: g_nav_driver_data,
    fab_data: g_fab_data,
    order_config_data: g_order_config_data,
    order_create_data: g_order_create_data,
    checklist_config_update_data: g_checklist_config_update_data
  }
});