<template>
  <div class="cell">
    <div class="row">
      <div class="col-8 cell">
        {{ name}}
      </div>
      <div class="col-4">
        {{ value }}
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        {{ comment }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "hello",
  props: ['point'],

  data: function () {
    const dict = {};
    dict['name'] = this.point.name;
    dict['value'] = this.point.value;
    if ('comment' in this.point){
      dict['comment'] = this.point.comment;
    }
    else{
      dict['comment'] = null;
    }
    return dict
  }
}
</script>

<style scoped>

.cell {
  border-style: solid;
  border-color: black;
}

</style>