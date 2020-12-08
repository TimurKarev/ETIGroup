import Vue from "vue";
import hello from "/assets/vue/components/hello.vue";

const app = new Vue({
  el: "#app",
  delimiters: ['[[',']]'],
  components:{ hello
      },
  data: {
    data_det: checklist_data,

  }
});