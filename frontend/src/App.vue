<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  mounted() {
    setInterval(() => {
      this.checkVisibility();
    }, 1000);
  },
  methods: {
    checkVisibility: function () {
      let vs = document.visibilityState;
      let date = new Date(Date.now());
      if (vs == "visible") {
        document.title =
          "Ervin Zhang - " +
          date.getHours() +
          ":" +
          date.getMinutes() +
          ":" +
          date.getSeconds();
      }
    },
  },
};
</script>

<style>
::-webkit-scrollbar {
  /*滚动条整体样式*/
  height: 12px;
  width: 12px;
}
::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 10px;
  background: rgba(36, 44, 94, 0.9);
}
::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  border-radius: 10px;
  background: transparent;
}

* {
  margin: 0;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Roboto","Oxygen","Ubuntu","Cantarell","Fira Sans","Droid Sans","Helvetica Neue",sans-serif;
}

#app {
  overflow: hidden;
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


.el-collapse-item__header,.el-collapse-item__wrap{
  background-color: beige!important;
  padding: 15px;
  font-size: 1em!important;
}

.el-divider{
  background-color: lightgrey!important;
}

.el-divider__text,
.el-link {
  font-size: 1.2em!important;
  font-weight:700;
}

.el-card__header{
  font-weight: 600;
}

.el-collapse-item__content{
  font-size:medium !important;
}

.ezlogo {
  content: url("./assets/static/img/ez-light.png");
  width: 32px;
  height: 32px;
}

</style>
