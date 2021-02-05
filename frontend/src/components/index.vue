<template>
  <div>
    <header>
      <!-- nav -->
      <el-menu
        default-active="aboutme"
        mode="horizontal"
        @select="changePage"
        background-color="#142044"
        text-color="darkgrey"
        active-text-color="beige"
      >
        <el-menu-item index="welcome" style="min-width:15vw;text-align:center">
          <i class="ezlogo"></i>
          <router-link to="/">EZ Info</router-link>
        </el-menu-item>
        <el-submenu index="aboutme">
          <template slot="title">
            <i class="el-icon-user-solid"></i>
            <a @click="changePage2('aboutme')" class="menuwords">About Me</a>
          </template>
          <el-menu-item index="aboutme-technology">
            <i class="el-icon-s-platform"></i>
            <a href="#technology">Technology</a>
          </el-menu-item>
          <el-menu-item index="aboutme-certificates">
            <i class="el-icon-medal"></i>
            <a href="#certificate">Certificates</a>
          </el-menu-item>
          <el-menu-item index="aboutme-education">
            <i class="el-icon-school"></i>
            <a href="#education">Education</a>
          </el-menu-item>
          <el-menu-item index="aboutme-projects">
            <i class="el-icon-notebook-1"></i>
            <a href="#project">Projects</a>
          </el-menu-item>
        </el-submenu>
        <el-submenu index="visual">
          <template slot="title">
            <i class="el-icon-data-line"></i>
            <span class="menuwords">Visualization</span>
          </template>
          <el-menu-item index="coding">
            <i class="el-icon-data-analysis"></i>Visual Coding
          </el-menu-item>
          <el-menu-item index="candlestick">
            <i class="el-icon-pie-chart"></i>CandleStick Chart (SSEC)
          </el-menu-item>
        </el-submenu>
        <el-submenu index="tool">
          <template slot="title"><i class="el-icon-s-tools"></i>
          <span class="menuwords">Tools</span>   
          </template>
          <el-menu-item index="translator"
            ><i class="el-icon-edit"></i>Translator</el-menu-item
          >
          <el-menu-item index="excel"
            ><i class="el-icon-s-grid"></i>Excel</el-menu-item
          >
          <el-submenu index="videochats">
            <template slot="title"
              ><i class="el-icon-phone-outline"></i>Video Chat</template
            >
            <el-menu-item index="videochat-sender">Sender</el-menu-item>
            <el-menu-item index="videochat-receiver">Receiver</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-submenu index="resources">
          <template slot="title">
            <i class="el-icon-folder-opened"></i>
            <span class="menuwords">Resources</span>
          </template>
          <el-menu-item index="link"
            ><i class="el-icon-link"></i>Links</el-menu-item
          >
        </el-submenu>
      </el-menu>
    </header>
    <main class="main">
      <Translator v-show="translatorShow"></Translator>
      <Coding v-if="codingShow"></Coding>
      <Videochat v-if="videochatShow" :room="roomtype"></Videochat>
      <Excel v-if="excelShow"></Excel>
      <Aboutme v-show="aboutmeShow"></Aboutme>
      <Candlestick v-if="candlestickShow"></Candlestick>
      <ResourceLink v-show="linkShow"></ResourceLink>
    </main>
    <el-backtop :bottom="10"></el-backtop>
  </div>
</template>

<script>
import Translator from "./translator.vue";
import Coding from "./coding.vue";
import Videochat from "./videochat.vue";
import Excel from "./excel.vue";
import Aboutme from "./aboutme.vue";
import Candlestick from "./candlestick.vue";
import ResourceLink from "./resourcelink.vue";

export default {
  name: "Index",
  components: {
    Translator,
    Coding,
    Videochat,
    Excel,
    Aboutme,
    Candlestick,
    ResourceLink
  },
  data() {
    return {
      userLocation: "",
      frameSrc: "",
      roomtype: "",
      translatorShow: false,
      codingShow: false,
      videochatShow: false,
      excelShow: false,
      aboutmeShow: true,
      candlestickShow:false,
      linkShow:false
    };
  },
  mounted() {
    this.getLocation();
  },
  methods: {
    showNotification(){
      this.$notify({
          title: 'Location Safety Notification',
          message: this.userLocation,
          type: 'success',
          duration: 5000,
        });
    },
    sendNotification(position) {
      let latitude = position.coords.latitude.toFixed(2);
      let longitude = position.coords.longitude.toFixed(2);
      latitude = latitude > 0 ? latitude + " N" : -latitude + " S";
      longitude = longitude > 0 ? longitude + " E" : -longitude + " W";
      this.userLocation = `You are now at (${latitude}, ${longitude})`;
      this.showNotification();
    },
    getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.sendNotification);
      }
    },
    changePage2(page){
      if(page=="aboutme"){
        this.translatorShow = false;
        this.codingShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.aboutmeShow = true;
        this.candlestickShow = false;
        this.linkShow = false;
      }else{
        this.aboutmeShow = false;
      }
    },
    changePage(key) {
      if (key.substr(0, 7) == "aboutme") {
        this.translatorShow = false;
        this.codingShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.aboutmeShow = true;
        this.candlestickShow = false;
        this.linkShow = false;
      } else if (key == "coding") {
        this.translatorShow = false;
        this.codingShow = true;
        this.videochatShow = false;
        this.excelShow = false;
        this.aboutmeShow = false;
        this.candlestickShow = false;
        this.linkShow = false;
      } else if(key=="candlestick"){
        this.translatorShow = false;
        this.codingShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.aboutmeShow = false;
        this.candlestickShow = true;
        this.linkShow = false;
      }else if (key == "translator") {
        this.translatorShow = true;
        this.codingShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.aboutmeShow = false;
        this.candlestickShow = false;
        this.linkShow = false;
      } else if (key == "excel") {
        this.translatorShow = false;
        this.codingShow = false;
        this.videochatShow = false;
        this.excelShow = true;
        this.aboutmeShow = false;
        this.candlestickShow = false;
        this.linkShow = false;
      } else if (key.substr(0, 9) == "videochat") {
        if (key.substr(10, 8) == "sender") {
          this.roomtype = false;
        } else {
          this.roomtype = true;
        }
        this.translatorShow = false;
        this.codingShow = false;
        this.videochatShow = true;
        this.excelShow = false;
        this.aboutmeShow = false;
        this.candlestickShow = false;
        this.linkShow = false;
      }else if(key=="link"){
        this.translatorShow = false;
        this.codingShow = false;
        this.videochatShow = false;
        this.excelShow = false;
        this.aboutmeShow = false;
        this.candlestickShow = false;
        this.linkShow = true;
      }
    },
  },
};
</script>

<style scoped>
@media (min-width: 810px){
  .menuwords{
    display: inline;
  }
}

@media (max-width: 810px){
  .menuwords{
    display: none;
  }
}

header {
  max-height: 7vh;
}

.main {
  min-height: 93vh;
}

a {
  text-decoration: none;
  color: darkgray;
}

.menu{
  display: flex;
}
</style>
