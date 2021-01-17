<script src="../../index.js"></script>
<template>
  <div>
    <h4 class="text-center">Создать новый заказ</h4>
    <br/>

    <v-alert
        dense
        :value="alert_order_num"
        color="red"
        dark
    >
      Номер заказа существует в базе
    </v-alert>

    <v-alert
        dense
        :value="alert_order_type"
        color="red"
        dark
    >
      Тип подстанции не поддерживается
    </v-alert>
    <v-text-field
        :rules="[rules.loanMin, rules.required]"
        v-model="order_num"
        type="number"
    >
      <template v-slot:label>
        Номер заводского заказа
      </template>
    </v-text-field>

    <v-select
        v-model="selected_type"
        :items="this.data.tp_type_list"
        label="Тип подстанции"
    ></v-select>

    <v-btn
        absolute
        block
        @click="btnClick"
    >
      Создать
    </v-btn>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "order_create",
  props: ['data'],
  data: function () {
    console.log("ORDER_CREATE", this.data)

    return {
      man_number_list: this.data.man_number_list,
      redirect_link: this.data.redirect_link,
      order_num: Math.max(... this.data.man_number_list) + 1,
      selected_type: this.data.tp_type_list[0],
      alert_order_num: false,
      alert_order_type: false,
      rules: {
         required: value => !!value || 'Обязательное поле',
         loanMin: value => value >= 0 || 'Значение не может быть отрицательным',
      },
    }
  },
  created() {
    this.$eventHub.$on('createorder-button-click', this.btnClick)
  },
  beforeDestroy() {
    this.$eventHub.$off('createorder-button-click')
  },
  methods:{
    btnClick() {
      //console.log("ORDER_CREATE", this.man_number_list.indexOf(parseInt(this.order_num)))
      if (this.man_number_list.indexOf(parseInt(this.order_num)) >= 0) {
        this.alert_order_num = true
      }else if (this.data.tp_type_list.indexOf(this.selected_type) < 0) {
        this.alert_order_type = true
      }
      else {
        this.alert_order_num = false
        this.alert_order_type = false

        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
        const data = {
          "order_num": this.order_num,
          "order_type": this.selected_type,
        }
        axios({
          method: 'post',
          url: "/order_create/",
          data: data,
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
          }
        })
            .catch(function (error) {
              console.log(error);
            })
            .then(response => {
              if(response.data.status === 'ok'){
                const link = this.redirect_link.slice(0, -2) + response.data.id + "/"
                //console.log("ORDER_CREATE", link);
                location.replace(link);
              }
              //location.replace('http://127.0.0.1:8000/order_detail_view/' + this.pk + "/");
            });
      }
    }
  }
}
</script>

<style scoped>

</style>