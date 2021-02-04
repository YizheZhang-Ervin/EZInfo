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
          <el-menu-item index="translator"><i class="el-icon-edit"></i>Translator</el-menu-item>
          <el-menu-item index="excel"><i class="el-icon-s-grid"></i>Excel</el-menu-item>
          <el-submenu index="videochats">
            <template slot="title"><i class="el-icon-phone-outline"></i>Video Chat</template>
            <el-menu-item index="videochat-sender">Sender</el-menu-item>
            <el-menu-item index="videochat-receiver">Receiver</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="group">
          <i class="el-icon-user"></i>
          Group
        </el-menu-item>
      </el-menu>
      <!-- 位置提醒框 -->
      <h3 class="notify" @click="changeNotification" v-show="notificationShow">
        <i class="el-icon-caret-top"></i>
        {{ userLocation }}
      </h3>
    </header>
    <main class="main">
      <Translator v-show="translatorShow"></Translator>
      <Fintech v-show="fintechShow"></Fintech>
      <Videochat v-if="videochatShow" :room="roomtype"></Videochat>
      <Excel v-show="excelShow"></Excel>
      <Group v-show="groupShow"></Group>
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
import Videochat from "./videochat.vue";
import Excel from './excel.vue';
import Group from "./group.vue";

export default {
  name: "Index",
  components:{
    Translator,
    Fintech,
    Videochat,
    Excel,
    Group
  },
  data() {
    return {
      userLocation: "",
      notificationShow: true,
      translatorShow:false,
      fintechShow:true,
      videochatShow:false,
      excelShow:false,
      groupShow:false,
      frameSrc:"",
      roomtype:""
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
      let latitude = position.coords.latitude.toFixed(2);
      let longitude = position.coords.longitude.toFixed(2);
      latitude =
        latitude > 0
          ? latitude + " N"
          : -latitude + " S";
      longitude =
        longitude > 0
          ? longitude + " E"
          : -longitude + " W";
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
        this.fintechShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.groupShow = false;
      }else if(key=="fintech"){
        this.translatorShow = false;
        this.fintechShow = true;
        this.videochatShow = false;
        this.excelShow = false;
        this.groupShow = false;
      }else if(key.substr(0,9)=="videochat"){
        if(key.substr(10,8)=="sender"){
          this.roomtype = false;
        }else{
          this.roomtype = true;
        }
        this.translatorShow = false;
        this.fintechShow = false;
        this.videochatShow = true;
        this.excelShow = false;
        this.groupShow = false;
      }else if(key=="excel"){
        this.translatorShow = false;
        this.fintechShow = false;
        this.videochatShow = false;
        this.excelShow = true;
        this.groupShow = false;
      }else if(key=="group"){
        this.translatorShow = false;
        this.fintechShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.groupShow = true;
      }else{
        this.translatorShow = false;
        this.fintechShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.groupShow = false;
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
  background-image: linear-gradient(45deg,lightgreen,white);
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
