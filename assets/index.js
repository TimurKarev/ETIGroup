import Vue from "vue";
import checklist_header from "./vue/components/checklist_header";

const app = new Vue({
  el: "#app",
  delimiters: ['[[',']]'],
  components: {
    checklist_header
  },
  data: {
    data_det: checklist_data,
    header: checklist_name,
  }
});