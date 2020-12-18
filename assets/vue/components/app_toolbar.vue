<template>
  <div>
  <el-menu
      class="el-menu-demo"
      mode="horizontal"
  >
    <el-row type="flex">
      <el-col :span="12">
        <el-row type="flex">
          <el-col :span="6">
            <el-menu-item>
            <i class="el-icon-s-unfold"></i>
          </el-menu-item>
          </el-col>
          <el-col :span="6">
            <el-menu-item>
            <i class="el-icon-s-home"></i>
          </el-menu-item>
          </el-col>
        </el-row>
      </el-col>

      <el-col :span="12">
        <el-row type="flex" justify="end">
          <el-col :span="18" >
            <el-menu-item index="1" style="{justify-content: end}">Незнакомец</el-menu-item>
          </el-col>
          <el-col :span="6">
           <el-menu-item>
        <i class="el-icon-s-custom"></i>
      </el-menu-item>
          </el-col>
        </el-row>
  </el-col>
    </el-row>

  </el-menu>
    </div>
</template>

<style lang="scss" scoped>
 .el-menu-demo {
   height: 10%!important;
 }
 .el-icon-s-unfold {
   height: 50%;
 }
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