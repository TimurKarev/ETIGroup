<template>
  <v-fab-transition>
      <v-btn
        elevation="2"
        fab
        bottom
        right
        fixed
        color="accent"
        @click="clickFab"
      >
        <v-icon color="black">mdi-plus</v-icon>
      </v-btn>
    </v-fab-transition>
</template>

<script>
export default {
name: "action_button",
  props: ['fab_link'],
  methods: {
    clickFab(){
      let link = this.fab_link
      if (typeof link === "undefined"){
        link="/";
      }
      location.replace(link);
    }
  }
}
</script>

<style scoped>

</style>