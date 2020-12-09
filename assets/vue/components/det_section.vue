<template>
<dev>
  <div class="row">
    <div class="header" v-bind:class="[is_plus ? 'col-7' : 'col-8']">
      <a class="roll" href="" @click.prevent="rollUp">{{ rollSymbol}}</a>
      {{ name }}
    </div>
    <div v-if="is_plus" class="col-1" v-bind:style="{'background-color': 'red'}">
    </div>
  </div>
  <div v-if="!is_plus">
    <det_point v-for="point in section.points" :point="point"></det_point>
  </div>
</dev>
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
      'name': this.section.name,
      'is_plus': false,
    }
  },
  computed: {
    rollSymbol(){
      if (this.is_plus) return '+';
      else return '-';
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
    font-weight: bolder;
    margin-top: 10px;
  }
  .roll {
    font-size: xx-large;
    color: black
  }
</style>