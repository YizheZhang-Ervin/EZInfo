<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
*{
    margin: 0;
}

#app{
    overflow: hidden;
}

.header{
    min-height: 7vh;
}

.main{
    min-height:86vh;
}

.footer{
    background-color:rgb(34, 28, 28);
    color:gold;
    min-height: 7vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.iframe{
    height: 86vh;
    width: 100vw;
}

.el-menu-item,.el-submenu__title,.el-submenu__title:focus, .el-submenu__title:hover{
    font-size: 1.1em!important;
}
</style>
