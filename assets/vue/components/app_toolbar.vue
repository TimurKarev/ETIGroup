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

    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-app-bar-nav-icon
            @click="navButtonClicked"
            v-on="on"
            v-bind="attrs"
        >
        </v-app-bar-nav-icon>
      </template>
      <span>{{this.data.menu_btn.tooltip}}</span>
    </v-tooltip>


    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn
            @click="homeButtonClicked"
            icon
            v-on="on">
          <v-icon>{{home_icon}}</v-icon>
        </v-btn>
      </template>
      <span>{{this.data.home_btn.tooltip}}</span>
    </v-tooltip>

    <v-spacer></v-spacer>

    <v-toolbar-title>{{ this.data.login.app_title }}</v-toolbar-title>

    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn
            icon
            v-on="on"
            :href="log_link"
        >
          <v-icon>{{log_icon}}</v-icon>
        </v-btn>
      </template>
      <span>{{this.data.login.tooltip}}</span>
    </v-tooltip>

  </v-app-bar>
</div>
</template>

<style lang="scss" scoped>

</style>

<script>
import nav_driver from "./nav_driver";

export default {
  name: 'app_toolbar',
  props: {
    data: {
      type: Object,
    },
    header: {
      type: String,
    }
  },
  data: function(){
     //console.log("APP_TOOLBAR - ", this.data.login.menu[0].link)
     return {
      active: 'guide',
       home_icon: this.data.home_btn.icon,
       log_icon: this.data.login.icon,
       log_link: this.data.login.menu[0].link,
    }
  },
  methods: {
    navButtonClicked(){
      this.$eventHub.$emit('nav-button-click');
    },
    homeButtonClicked(){
      window.location.href = '/'
    }
  },
}

</script>