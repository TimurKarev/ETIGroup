<template>
<div>
      <h3 class="text-center">{{this.data.checklist_name}}</h3>

  <div>
    <v-expansion-panels flat>
    <v-expansion-panel
      v-for="section in sections"
      :key="section.name"
    >
      <v-expansion-panel-header>
        <v-list-item>

          <v-list-item-content>
            <v-list-item-title class="font-weight-medium">{{ section.name }}</v-list-item-title>
          </v-list-item-content>

          <v-list-item-icon>
            <v-icon
                :color="headerColor(section)"
            >
              {{ headerIcon(section) }}
            </v-icon>
          </v-list-item-icon>
        </v-list-item>
      </v-expansion-panel-header>
      <v-expansion-panel-content>

        <div v-for="point in section.points" :key="point.id">
          <v-list-item>

        <v-list-item-content>
          <v-list-item-title>{{point.name}}</v-list-item-title>
          <v-list-item-subtitle>{{point.comment}}</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-icon>
          <v-icon :color="pointColor(point)">{{ pointIcon(point) }}</v-icon>
        </v-list-item-icon>
      </v-list-item>
        </div>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
  </div>

</div>
</template>

<script>
export default {
  name: "checklist_detail",
  props: ['data'],
  data: function (){
    console.log('CHECKLIST DETAIL', this.data)
    return {
      sections: this.data.data,
      pk: this.data.pk,
      type: this.data.checklist_type,
    }
  },
  created() {
    this.$eventHub.$on('editchecklist-button-click', this.replace)
  },
  beforeDestroy() {
    this.$eventHub.$off('editchecklist-button-click')
  },
  methods: {
    replace: function (){
      location.replace('/checklist_update/' + this.type + "/" + this.pk + "/");
    },
    headerColor: function(section) {
      //console.log(section.points.slice(-1)[0].value)
      //const value = section.points.slice(-1)[0].value
      if (section.points.slice(-1)[0].value === 'Пройдены') {
        return 'green'
      }
        return 'grey'
    },
    headerIcon: function(section) {
      if (section.points.slice(-1)[0].value === 'Пройдены') {
        return 'mdi-check-bold'
      }
        return 'mdi-close-box'
    },
    pointIcon: function (point){
      let icon
      if(point.value === "Не проверено"){
        icon =  'mdi-message-text-clock-outline'
      }
      if(point.value === "Принято"){
        icon =  'mdi-check'
      }
      if(point.value === "Не используется"){
        icon =  'mdi-block-helper'
      }
      if(point.value === "Коментарий"){
        icon =  'mdi-exclamation-thick'
      }
      if(point.value === "Не Пройдены"){
        icon =  'mdi-close'
      }
      if(point.value === "Пройдены"){
        icon =  'mdi-check-bold'
      }
      return icon
    },
    pointColor: function (point){
      let color
      if(point.value === "Не проверено"){
        color =  'grey'
      }
      if(point.value === "Принято"){
        color =  'green'
      }
      if(point.value === "Не используется"){
        color =  'black'
      }
      if(point.value === "Коментарий"){
        color =  'red'
      }
      if(point.value === "Не Пройдены"){
        color =  'red'
      }
      if(point.value === "Пройдены"){
        color =  'green'
      }
      return color
    },
  }
}
</script>

<style scoped>

</style>