<template>
<div>
  <h4 class="text-center">Заводской заказ №{{this.data.order_number}}</h4>

  <v-simple-table>
    <template v-slot:default>
      <tbody>
        <tr>
          <td>Тип подстанции</td>
          <td>{{ subst_type }}</td>
        </tr>
        <tr v-for="point in points" :key="point.id">
          <td>{{ point.name }}</td>
          <td>{{ point.value }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</div>
</template>

<script>
export default {
  name: "order_detail",
  props: ['data'],
  data: function (){
    console.log("ORDER_DETAIL", this.data)
    return {
      points: this.data.config.points,
      subst_type: this.data.subst_type,
      pk: this.data.order_pk,

    }
  },
  created() {
    this.$eventHub.$on('editorder-button-click', this.replace)
  },
  beforeDestroy() {
    this.$eventHub.$off('editorder-button-click')
  },
  methods: {
    replace() {
      //console.log("ORDER_DETAIL", "click")
      location.replace('http://127.0.0.1:8000/order_update_config/' + this.pk + "/");
    }
  }
}
</script>

<style scoped>

</style>