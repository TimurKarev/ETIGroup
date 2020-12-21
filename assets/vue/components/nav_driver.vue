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
     <template v-slot:append>
        <div class="pa-2">
          <v-btn block>
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
</template>

<script>
export default {
  name: "nav_driver",
  data: function(){
    return{
      driver: null
    }
  },
  created() {
    this.$eventHub.$on('nav-button-click', this.showDriver)
  },
  beforeDestroy() {
    this.$eventHub.$off('nav-button-click')
  },
  methods: {
    showDriver(){
      this.driver = true
    }
  }
}
</script>

<style scoped>

</style>