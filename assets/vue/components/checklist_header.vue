<template>
  <div>
    <div class="row">
      <div class="col-8">
        <div class="str">{{ header_str }}</div>
        <a class="roll" href="" @click.prevent="rollUp">{{rollSymbol}}</a>
      </div>
    </div>
    <det_section v-for="section in this.sections"
                 :section="section"
                 :is_plus="is_plus">
    </det_section>
  </div>
</template>

<script>
import det_section from "./det_section";

export default {
  name: "checklist_header",
  components:{det_section},

  props: {
    header_props : {
      name: 'header_props',
      type: String,
    },
    sections: {
      name: 'sections',
      type: Object,
    },
  },
  data: function() {
    return {
      'header_str': this.header_props,
      'is_plus': true,
    }
  },
  computed:{
    rollSymbol() {
      if (this.is_plus) return '++';
      else return '--';
    }
  },
  methods: {
    rollUp() {
      this.is_plus = !this.is_plus;
    },
  }
}
</script>


<style scoped>

.str{
  font-weight: bold;
  font-size: x-large;
  text-align: center;
}

.roll{
  font-size: x-large;
  color: black;
}

</style>