<template>
  <div>
    <h4 class="text-center">Конфигурация заводского заказа №{{man_number}}</h4>
    <br/>
    <div v-for="c_data in config_data" :key="c_data.id">
          <v-text-field
            v-model="c_data.value"
            type="number"
            :rules="[rules.loanMin, rules.required]"
          >
           <template v-slot:label>
             {{c_data.name}}
           </template>
          </v-text-field>
    </div>
      <v-btn
          absolute
          block
          @click="btnClick"
      >
        Сохранить
      </v-btn>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "order_config",
  props: ['data'],
  data: function (){
    console.log("ORDER_CONFIG", this.data)
    return {
      config_data: this.data.points,
      pk: this.data.pk,
      man_number: this.data.man_number,
      rules: {
         required: value => !!value || 'Обязательное поле',
         loanMin: value => value >= 0 || 'Значение не может быть отрицательным',
      },
    }
  },
  created() {
    this.$eventHub.$on('save-button-click', this.btnClick)
  },
  beforeDestroy() {
    this.$eventHub.$off('save-button-click')
  },
  methods:{
    btnClick(){
      console.log("ORDER_CONFIG", this.config_data)
      //console.log("ORDER_CONFIG")
      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      const data = {
        "points": this.config_data,
        "pk": this.data.pk,
        }
      axios({
        method: 'post',
        url: "http://127.0.0.1:8000/order_update_config/"+ this.pk + "/",
        data: data,
        headers:{
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
      })
      .catch(function (error) {
         console.log(error);
      })
      .then(response => {
        console.log(response.data);
        location.replace('http://127.0.0.1:8000/checklist_update/bm_/<int:pk>/' + this.pk + "/");
      });

      },
  }
}
</script>

<style scoped>

</style>