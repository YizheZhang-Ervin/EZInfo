<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style>
::-webkit-scrollbar {
  /*滚动条整体样式*/
  height: 7px;
  width: 7px;
}
::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 10px;
  background: gold;
}
::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  border-radius: 10px;
  background: transparent;
}

* {
  margin: 0;
}

#app {
  overflow: hidden;
}

.header {
  min-height: 7vh;
}

.main {
  min-height: 86vh;
}

.footer {
  background-color: #000;
  color: gold;
  min-height: 7vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-menu-item,
.el-submenu__title,
.el-submenu__title:focus,
.el-submenu__title:hover {
  font-size: 1.1em !important;
}

.el-menu.el-menu--horizontal {
  border-bottom: none !important;
}
</style>
