<template>
  <div>
    <h4 class="text-center">Конфигурация строительной части заказа №{{this.data.order_number}}</h4>
    <br/>
   <div v-for="c_data in config_list" :key="c_data.id">
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
        Создать Чеклист
      </v-btn>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "checklist_config_update",
  props: ['data'],
  data: function (){
    console.log("CHL_CONFIG_UPDT", this.data)
    return {
      config_list: this.data.config,
      pk: this.data.pk,
      rules: {
         required: value => !!value || 'Обязательное поле',
         loanMin: value => value >= 0 || 'Значение не может быть отрицательным',
      },
    }
  },
  created() {
    this.$eventHub.$on('createchecklist-button-click', this.btnClick)
  },
  beforeDestroy() {
    this.$eventHub.$off('createchecklist-button-click')
  },
  methods: {
    btnClick() {
      console.log("CHL_CONFIG_UPDT", this.config_list)

      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      const data = {
        "points": this.config_list,
        //"pk": this.data.pk,
        }
      axios({
        method: 'post',
        url: "/checklist_config_update/bm_checklist/"+ this.pk,
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
        location.replace(response.data.message);
      });
    }
  },
}
</script>


<style scoped>

</style>