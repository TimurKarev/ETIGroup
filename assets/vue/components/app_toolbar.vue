<template>
  <div>
  <el-menu
      class="el-menu-demo"
      mode="horizontal"
  >
    <el-row type="flex" justify="start">
      <el-col :span="4">
        <el-row type="flex" justify="start" gutter="30">
          <el-col :span="6">
            <el-menu-item>
            <i class="el-icon-s-unfold"></i>
          </el-menu-item>
          </el-col>
          <el-col :span="18">
            <el-menu-item>
            <i class="el-icon-s-home"></i>
          </el-menu-item>
          </el-col>
        </el-row>
      </el-col>

      <el-col :span="18">
        <el-row type="flex" justify="end" gutter="30">
          <el-col :span="19" >
            <el-menu-item index="1" style="{justify-content: end}">
              <div class="name">Ytofmd,f</div>
            </el-menu-item>
          </el-col>
          <el-col :span="5">
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