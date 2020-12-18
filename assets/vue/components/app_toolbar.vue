<template>
  <el-button type="primary">Primary</el-button>
</template>

<style lang="scss" scoped>

</style>

<script>

export default {
  name: 'app_toolbar',

  props: [
      'title'
  ],

  data:() => ({
      active: 'guide'
    })
}

</script>