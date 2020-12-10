<template>
<div>
  <div class="row" v-bind:class="[is_plus ? 'close-header' : 'open-header']">
    <div v-bind:class="[is_plus ? 'col-7' : 'col-8']"
         :v-bind:class="[is_plus ? 'col-md-7' : 'col-md-8']">
      <a class="header" href="" @click.prevent="rollUp">{{ rollSymbol}} {{ name }}</a>
    </div>
    <div v-if="is_plus"
         class="col-1 col-md-1 section_box"
         v-bind:style="{'background-color': sectionColor}">
    </div>
  </div>
  <div v-if="!is_plus">
    <det_point v-for="point in section.points" :point="point" ></det_point>
  </div>

</div>
</template>

<script>
import det_point from "./det_point";

const completedColor = 'lime'
const inProgressColor = 'royalblue'

export default {
  name: "det_section",
  components: {det_point},
  props:{
    section: {
      name: 'section',
      type: Object,
    }
  },
  data: function (){
    return {
      'name': this.section.name,
      'is_plus': true,
    }
  },
  computed: {
    rollSymbol(){
      if (this.is_plus) return '+';
      else return '-';
    },
    sectionColor() {
      let retColor = inProgressColor;
      this.section.points.forEach(point =>{
        if (point.value === 'Пройдены') retColor = completedColor;
      });
      return retColor;
    }
  },
  methods: {
    rollUp(){
      this.is_plus = !this.is_plus;
    },
  }
}
</script>

<style scoped>

  .header {
    font-size: x-large;
    font-weight: 500;
    line-height: 90%;
    color: black
  }
  .open-header{
    padding-bottom: .4%;
    padding-top: 1%;
  }
  .close-header{
    padding-bottom: 0;
    padding-top: .15%;
  }
</style>