<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="ch_list"
      hide-default-footer
      class="elevation-1"
      fixed-header
    >
      <template v-slot:item.order_num="{value}">
        <a
            :href="value.link"
        >
          {{value.name}}
        </a>
      </template>

      <template v-slot:item.build="{value}">
        <a :href="value.link">{{value.name}}</a>
      </template>

    </v-data-table>
  </div>
</template>

<script>
export default {
  name: "checklists_list",
  props: ['list_data'],
  data: function() {
    return {
      headers: [
          {text: 'Заказ', value: 'order_num'},
          {text: 'Стройка', value: 'build'},
          // {text: 'Электрика', value: 'el'},
          // {text: 'Телемеханика', value: 'tm'},
          // {text: 'Зип', value: 'zip'},
          // {text: 'Документы', value: 'doc'},
          // {text: 'Заказчик', value: 'sal'},
      ],
      ch_list: this.list_data,
    }
  },
  created() {
    this.$eventHub.$on('oredercreate-button-click', this.createOrder)
  },
  beforeDestroy() {
    this.$eventHub.$off('oredercreate-button-click')
  },
  methods: {
    createOrder: function (){
      console.log("Click")
      location.replace('/order_create/')
    }
  },
}

</script>

<style scoped>
 a {
   color: black!important;
 }
</style>