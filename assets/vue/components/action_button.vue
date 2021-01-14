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
      const event = this.data.event
      this.$eventHub.$emit(event);
    }
  }
}
</script>

<style scoped>

</style>