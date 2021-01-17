<template>
  <div>
      <h4 class="text-center">{{this.data.checklist_name}}</h4>
      <br/>

<div>
    <v-expansion-panels flat>
    <v-expansion-panel

      v-for="section in sections"
      :key="section.name"
    >
      <v-expansion-panel-header >
        <p class="font-weight-bold">{{ section.name }}</p>
      </v-expansion-panel-header>

      <v-expansion-panel-content>
        <div v-for="point in section.points" :key="point.id">
              <v-row>
                <v-col cols="9">
                  <v-row class="font-weight-medium">{{point.name}}</v-row>
                  <v-row>
                    <v-text-field
                      v-model="point.comment"
                    >
          </v-text-field>
                  </v-row>
                </v-col>
                <v-col cols="3" >
                   <v-select
                        :color="getColor(point.value)"
                        v-model="point.value"
                        :items="['Не проверено', 'Не используется', 'Коментарий', 'Принято' ]"
                        :label="point.value"
                   ></v-select>
                </v-col>
              </v-row>
          <v-divider></v-divider>
        </div>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "checklist_update",
  props: ['data'],
  data: function (){
    console.log("CHECKLIST_UPDATE", this.data)
    return {
      sections: this.data.sections,
      pk: this.data.pk,
      type: this.data.type,
    }
  },
  created() {
    this.$eventHub.$on('savechecklist-button-click', this.saveChecklist)
  },
  beforeDestroy() {
    this.$eventHub.$off('savechecklist-button-click')
  },

  methods: {
    getColor: function (value) {
      if(value === 'Не проверено'){
        return 'black'
      }
      if(value === 'Не используется'){
        return 'grey'
      }
      if(value === 'Принято'){
        return 'green'
      }
      if(value === 'Коментарий'){
        return 'red'
      }
      return 'grey'
    },
    saveChecklist: function () {
      //console.log("Click")
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

        const data = this.sections

        axios({
          method: 'post',
          url: "/checklist_update/" + this.type + "/" + this.pk + "/",
          data: data,
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
          }
        })
            .catch(function (error) {
              console.log(error);
            })
            .then(response => {
              // if(response.data.status === 'ok'){
              //   const link = this.redirect_link.slice(0, -2) + response.data.id + "/"
              //   //console.log("ORDER_CREATE", link);
              //   location.replace(link);
              // }
              location.replace('/checklist_detail/' + this.type + "/" + this.pk);
              console.log(response.data)
            });
    },
  },

}
</script>

<style scoped>

</style>