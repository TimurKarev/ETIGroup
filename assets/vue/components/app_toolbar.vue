<template>
  <div>
  <v-app-bar
      app
      fixed
      color="primary"
      max-height="50"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-4"
  >
    <v-app-bar-nav-icon @click="navButtonClicked"></v-app-bar-nav-icon>

    <v-btn
      icon
      :href="this.main_urls.checklist_list"
    >
        <v-icon>mdi-home</v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    <v-toolbar-title>Незнакомец</v-toolbar-title>

   <v-btn icon>
      <v-icon>mdi-account-circle</v-icon>
  </v-btn>
  </v-app-bar>
</div>
</template>

<style lang="scss" scoped>

</style>

<script>
import nav_driver from "./nav_driver";

export default {
  name: 'app_toolbar',
  components: {nav_driver},
  props: {
    main_urls: {
      type: Object,
    }
  },
  data: function(){
     return {
      active: 'guide',
      collapseOnScroll: true,
    }
  },
  methods: {
    navButtonClicked(){
       this.$eventHub.$emit('nav-button-click');
    }
  },
}

</script>