<template>
  <vs-button disabled >Disabled</vs-button>
</template>

<style lang="scss" scoped>

</style>

<script>
import Checklists_list from "./checklists_list";
export default {
  name: 'app_toolbar',
  components: {Checklists_list},
  props: [
      'title'
  ],
}
</script>