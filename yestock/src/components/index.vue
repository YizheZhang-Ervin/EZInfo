<template>
  <div>
    <header>
      <!-- nav -->
      <el-menu
        default-active="fintech"
        class="el-menu-demo"
        mode="horizontal"
        @select="changePage"
        background-color="#000"
        text-color="gold"
        active-text-color="gold"
      >
        <el-menu-item index="fintech">
          <i class="el-icon-s-home"></i>
          YeStock
        </el-menu-item>
        <el-submenu index="alg">
          <template slot="title">
            <i class="el-icon-monitor"></i>
            Algorithms
          </template>
          <el-menu-item index="alg-1">Market Making</el-menu-item>
          <el-menu-item index="alg-2">Passive Investment</el-menu-item>
          <el-menu-item index="alg-3">Active Investment</el-menu-item>
          <el-menu-item index="alg-4">Risk Management</el-menu-item>
          <el-menu-item index="alg-5">Advanced</el-menu-item>
        </el-submenu>
        <el-submenu index="tool">
          <template slot="title"><i class="el-icon-s-tools"></i>Tools</template>
          <el-menu-item index="translator">Translator</el-menu-item>
          <el-submenu index="Games">
            <template slot="title">Games</template>
            <el-menu-item index="3-1"
              ><a href="/game1" target="iframe001"
                >Assignment 1</a
              ></el-menu-item
            >
            <el-menu-item index="3-2"
              ><a href="/game2" target="iframe001"
                >Assignment 2</a
              ></el-menu-item
            >
            <el-menu-item index="3-3">
              <a href="/game3" target="iframe001">Assignment 3</a>
            </el-menu-item>
            <el-menu-item index="3-4">
              <a href="/game4" target="iframe001">Assignment 4</a>
            </el-menu-item>
            <el-menu-item index="3-5">
              <a href="/game5" target="iframe001">Assignment 5</a>
            </el-menu-item>
            <el-menu-item index="3-6">
              <a href="/game6" target="iframe001">Project 1</a>
            </el-menu-item>
            <el-menu-item index="3-7">
              <a href="/game7" target="iframe001">Project 2</a>
            </el-menu-item>
          </el-submenu>
        </el-submenu>
      </el-menu>
      <!-- 位置提醒框 -->
      <h3 class="notify" @click="changeNotification" v-show="notificationShow">
        <i class="el-icon-caret-top"></i>
        {{ userLocation }}
      </h3>
    </header>
    <main class="main">
      <iframe id="iframe001" class="iframe" name="iframe001" v-show="iframeShow"></iframe>
      <Translator v-show="translatorShow"></Translator>
      <Fintech v-show="fintechShow"></Fintech>
    </main>
    <footer class="footer">
      <a target="_blank" rel="noopener noreferrer" 
      href="https://ervinzhang.pythonanywhere.com/">
      Design By Yizhe Zhang | ervinzhang.pythonanywhere.com
      </a>
    </footer>
  </div>
</template>

<script>
import Translator from "./translator.vue";
import Fintech from "./fintech.vue";

export default {
  name: "Index",
  components:{
    Translator,
    Fintech
  },
  data() {
    return {
      userLocation: "",
      notificationShow: true,
      translatorShow:false,
      iframeShow:false,
      fintechShow:true,
      frameSrc:""
    };
  },
  mounted() {
    this.getLocation();
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
          "YeStock - " +
          date.getHours() +
          ":" +
          date.getMinutes() +
          ":" +
          date.getSeconds();
      }
    },
    sendNotification(position) {
      let latitude =
        position.coords.latitude > 0
          ? position.coords.latitude + " N"
          : position.coords.latitude + " S";
      let longitude =
        position.coords.longitude > 0
          ? position.coords.longitude + " E"
          : position.coords.longitude + " W";
      this.userLocation = `Location Safety Notification: You are now at (${latitude}, ${longitude}), have access to Algorithms.`;
    },
    getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.sendNotification);
      }
    },
    changeNotification() {
      this.notificationShow = false;
    },
    changePage(key){
      if(key=="translator"){
        this.translatorShow = true;
        this.iframeShow = false;
        this.fintechShow = false;
      }else if(key=="fintech"){
        this.translatorShow = false;
        this.iframeShow = false;
        this.fintechShow = true;
      }else{
        this.translatorShow = false;
        this.iframeShow = true;
        this.fintechShow = false;
        document.getElementById("iframe001").src = "";
      }
    }
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: gold;
}
.notify {
  background-color: lightgreen;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
