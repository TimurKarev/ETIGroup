<template>
  <div>
    <v-btn @click="btnClick">fk;ldaskf;s</v-btn>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'

export default {
  name: "order_config",
  props: ['token'],
  methods:{
    btnClick(){
      console.log("ORDER_CONFIG")
      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      const qs = require('qs');
      const data = qs.stringify({
                'i1sec-point_value': 11,
                'i0sec-point_value': 21,
                'i2sec-point_value': 31,
            });
      axios({
        method: 'post',
        url: "http://127.0.0.1:8000/order_update_config/6/",
        data: data,
        headers:{
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
      })
      .catch(function (error) {
         console.log(error);
      });
      location.replace('http://127.0.0.1:8000/order_detail_view/6/');
    }
  }
}
</script>

<style scoped>

</style>