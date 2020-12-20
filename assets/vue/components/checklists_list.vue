<template>
  <v-btn @click="btnClick"> hdjskahk</v-btn>
</template>

<script>
export default {
  name: "checklists_list",
  props: ['list_data'],
  data: function() {
    console.log(this.list_data)
    return {
      n: 'none'
    }
  },
  methods: {
    btnClick(){
      this.$eventHub.$emit('button_click',
          {
                list: [1,1,3,4],
                text: 'bambarbia'
          })
    }
  }
}

</script>

<style scoped>

</style>