<template>
<div class="row">
  <div class="col-7 col-md-7">
    <div class="header">{{ name }}</div>
  </div>
  <div class="col-1 col-md-1">
    <p>dasjdkjskldjalskdjal</p>
  </div>
</div>
<det_point v-for="point in section.points" :point="point"></det_point>
</template>

<script>
import det_point from "./det_point";

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
      'name': this.section.name
    }
  },
  computed: {

  }
}
</script>

<style scoped>
  .header {
    font-size: larger;
    font-weight: bolder;
    margin-top: 10px;
  }
</style>