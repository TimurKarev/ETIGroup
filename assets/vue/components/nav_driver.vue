<template>
    <v-navigation-drawer
      v-model="driver"
      absolute
      temporary
    >

      <v-list
          nav
      >

        <v-subheader class="title text-center">
            {{this.data.page_title}}
        </v-subheader>

        <v-divider></v-divider>

        <v-list-item-group
          color="primary"
        >
          <v-list-item
            v-for="item in this.data.nav_list"
            :key="item.name"
            @click="listItemClick(item)"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title
                  v-text="item.name"
              >
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

     <template v-slot:append>
        <div class="pa-2">
          <v-btn
              block
              :href="login_btn_link"
          >
            {{ login_btn_title }}
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
</template>

<script>
export default {
  name: "nav_driver",
  props: ['data'],
  data: function(){
    //console.log('NAV_DRIVER - ', this.data.login.title)
    return{
      login_btn_title: this.data.login.title,
      login_btn_link: this.data.login.link,
      driver: null,
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
    },
    listItemClick(click_item){
      console.log(click_item.link)
      if(click_item.name === 'Создать заказ'){
        window.location.href = click_item.link
      }
    },
  }
}
</script>

<style scoped>

</style>