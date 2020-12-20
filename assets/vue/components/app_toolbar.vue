<template>
  <v-app-bar
    color="primary"
    dense
    max-height="50"
  >
    <v-app-bar-nav-icon></v-app-bar-nav-icon>

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
</template>

<style lang="scss" scoped>

</style>

<script>
export default {
  name: 'app_toolbar',

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
  created() {
    this.$eventHub.$on('button_click', this.someButtonClicked)
  },
  methods: {
    someButtonClicked(data){
      console.log(data)
    }
  }
}

</script>