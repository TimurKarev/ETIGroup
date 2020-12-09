<template>
  <div class="cell">
    <div class="row">
      <div class="col-5 col-md-7 name">
        {{ name}}
      </div>
      <div class="col-3 col-md-3 value" v-bind:style="{'background-color': valueColor}">
        {{ value }}
      </div>
    </div>
    <div class="row">
      <div class="col-8 col-md-10 comment">
        {{ comment }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "det-point",
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
  },
  computed: {
    valueColor() {
      if (this.value === 'Не используется') return 'cadetblue';
      if (this.value === 'Принято') return 'limegreen';
      if (this.value === 'Комментарий') return 'lightcoral';
      if (this.value === 'Не проверено') return 'palegoldenrod';
      if (this.value === 'Пройдены') return 'forestgreen'
      if (this.value === 'Не Пройдены') return 'navajowhite'
    }
  },
}
</script>

<style scoped>

.name, .value, .comment {
    word-break:break-all;
}

.cell {
  margin-left: 1%;
}

.name {
    font-weight: 450;
    font-size: large;
}

.value {
  display: table-cell;
  float: right;
  text-align: right;
  vertical-align: middle;
}

.comment {
  font-size: small;
  padding-left: 5%;
  border-width: thin;
  border-bottom-style: solid;
  border-color: darkgrey;
}

</style>
