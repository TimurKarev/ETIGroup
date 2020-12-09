import Vue from "vue";
import det_section from "./vue/components/det_section";

const app = new Vue({
  el: "#app",
  delimiters: ['[[',']]'],
  components:{
    det_section,
      },
  data: {
    data_det: checklist_data,

  }
});