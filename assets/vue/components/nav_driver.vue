<template>
    <v-navigation-drawer
      v-model="driver"
      absolute
      temporary
    >
            <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Application
          </v-list-item-title>
          <v-list-item-subtitle>
            subtext
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

    </v-navigation-drawer>
</template>

<script>
export default {
  name: "nav_driver",
  data: function(){
    return{
      driver: true
    }
  }
}
</script>

<style scoped>

</style>