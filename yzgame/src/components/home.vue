<template>
  <div>
    <header>
      <el-menu
        mode="horizontal"
        background-color="#000"
        text-color="gold"
        active-text-color="gold"
        default-active="A"
      >
        <el-menu-item index="A">YZGame</el-menu-item>
        <el-submenu index="B">
          <template slot="title">Games</template>
          <el-menu-item index="1">
            <a href="/game1" target="iframe001">Assignment 1</a>
          </el-menu-item>
          <el-menu-item index="2">
            <a href="/game2" target="iframe001">Assignment 2</a>
          </el-menu-item>
          <el-menu-item index="3">
            <a href="/game3" target="iframe001">Assignment 3</a>
          </el-menu-item>
          <el-menu-item index="4">
            <a href="/game4" target="iframe001">Assignment 4</a>
          </el-menu-item>
          <el-menu-item index="5">
            <a href="/game5" target="iframe001">Assignment 5</a>
          </el-menu-item>
          <el-menu-item index="6">
            <a href="/game6" target="iframe001">Project 1</a>
          </el-menu-item>
          <el-menu-item index="7">
            <a href="/game7" target="iframe001">Project 2</a>
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </header>
    <main class="main">
      <iframe id="iframe001" class="iframe" name="iframe001"></iframe>
    </main>
    <footer class="footer">Design By Yizhe Zhang</footer>
  </div>
</template>

<script>
const axios = require('axios');

export default {
  name: "Home",
  components:{
  },
  data(){
    return{
    }
  },
  mounted() {
    setInterval(() => {
      this.checkVisibility();
    }, 1000);
    document.getElementById("iframe001").src = "/game1";
  },
  methods: {
    get: function () {
      axios.get(`http://127.0.0.1:5000/api/${this.key}`).then(
        (response) => {
          if (response.data.error == "error") {
            console.log("backend error");
          } else {
            console.log(response.data.key);
          }
        },
        (err) => {
          console.log(err.data);
        }
      );
    },
    post: function () {
      axios
        .post(`http://127.0.0.1:5000/api/${this.key}`, {
          key: JSON.stringify(this.key),
        })
        .then(
          (response) => {
            if (response.data.error == "error") {
              console.log("backend error");
            } else {
              console.log(response.data.key);
            }
          },
          function (err) {
            console.log(err.data);
          }
        );
    },
    checkVisibility: function () {
      let vs = document.visibilityState;
      let date = new Date(Date.now());
      if (vs == "visible") {
        document.title =
          "YZGame - " +
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

<style scoped>
a{
  text-decoration: none;
  color: gold;
}
</style>
