<template>
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
  >
    <el-menu-item index="1">Processing Center</el-menu-item>
  </el-menu>
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