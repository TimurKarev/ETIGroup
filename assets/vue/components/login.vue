<template>
<div>
    <v-text-field
      v-model="login"
    >
     <template v-slot:label>
       Имя пользоватля
     </template>
    </v-text-field>

    <v-text-field
      v-model="password"
      type="password"
    >
     <template v-slot:label>
       Пароль
     </template>
    </v-text-field>

    <v-btn
        absolute
        block
        @click="enter"
    >
      Войти
    </v-btn>

</div>
</template>

<script>
import axios from "axios";

export default {
name: "login",
  data: function () {
    return {
      login: null,
      password: null
    }
  },
  methods: {
    enter: function (){
      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      const data = {
        login: this.login,
        password: this.password,

        }
      axios({
        method: 'post',
        url: "/custom_login/",
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
        if(response.data.message === 'ok'){
          location.replace("/");
        }
        //location.replace("http://127.0.0.1:8000" + response.data.message);
      });
    }
  },
}
</script>

<style scoped>

</style>