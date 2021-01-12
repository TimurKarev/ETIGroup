<template>
  <v-tooltip top>
    <template v-slot:activator="{ on }">
      <v-fab-transition>
          <v-btn
            elevation="2"
            fab
            bottom
            right
            fixed
            color="accent"
            @click="clickFab"
            v-on="on"
          >
            <v-icon color="black">{{ icon }}</v-icon>
          </v-btn>
        </v-fab-transition>
    </template>
    <span>{{ this.data.tooltip }}</span>
  </v-tooltip>
</template>

<script>
export default {
name: "action_button",
  props: ['data'],
  data: function (){
    console.log
    return {
      icon: this.data.icon,
    }
  },
  methods: {
    clickFab(){
      let link = this.data.link
      if (this.data.event === 'Link' && typeof link !== "undefined"){
        location.replace(link);
      }
      else if(this.data.event !== 'None'){
          const event = this.data.event
          this.$eventHub.$emit(event);
      } else {
        location.replace("/");
      }
    }
  }
}
</script>

<style scoped>

</style>