<template>
  <div class="whole">
    <!-- video -->
    <section class="videoArea">
      <section class="videoBtn">
        <el-input
          placeholder="Type in peer id to call"
          v-model="peerId"
          clearable
        ></el-input>
        <el-button
          type="primary"
          plain
          round
          id="callpeer"
          @click="callPeer"
          icon="el-icon-phone"
          >Call</el-button
        >
        <el-button
          type="primary"
          plain
          round
          id="openVideo"
          @click="setLocalVideo"
          icon="el-icon-video-camera"
          >Test Camera</el-button
        >
      </section>
      <video
        id="selfv"
        autoplay
        class="video"
        @drop="drop($event)"
        @dragover="allowDrop($event)"
      ></video>
      <video id="peerv" autoplay class="video"></video>
    </section>
    <!-- chatting -->
    <section class="chattingArea">
      <section class="chatBtn">
        <el-input
          placeholder="Type in peer id to call"
          v-model="peerId"
          clearable
        ></el-input>
        <el-button
          type="primary"
          plain
          round
          id="connect"
          @click="connectPeer"
          icon="el-icon-connection"
          >Connect</el-button
        >
        <el-button
          @click="drawer = true"
          type="primary"
          plain
          round
          icon="el-icon-s-operation"
          >Browse Status</el-button
        >
      </section>
      <el-card class="box-card cards">
        <el-switch
          v-model="chatrole"
          active-color="lightgreen"
          inactive-color="lightblue"
          active-text="Receiver"
          inactive-text="Sender"
        >
        </el-switch>
        <br />
        Connection Status:
        <p v-text="connStatus" style="display: inline"></p>
        <br />
        Your Id:
        <p v-text="selfid" style="display: inline"></p>
        <br />
        Video Url(click to drag to Video Area):
        <p
          @dragstart="drag($event)"
          draggable="true"
          v-text="url001"
          class="urls"
        ></p>
      </el-card>

      <pre v-text="msg" class="chattingHistory"></pre>
      <section class="inputArea">
        <el-input
          id="inputmsg"
          placeholder="msg"
          v-model="inputmsg"
          type="textarea"
        ></el-input>
        <el-button
          type="primary"
          plain
          round
          id="sendmsg"
          @click="sendMsgToPeer"
          icon="el-icon-s-promotion"
          >Send</el-button
        >
      </section>
    </section>
    <!-- parameters -->
    <el-drawer title="Connection Status" :visible.sync="drawer" direction="ltr">
      <el-card shadow="hover">
        <div v-for="k in dataURL" :key="k">
          {{ k }}
        </div>
        <div v-for="k in dataHardware" :key="k">
          {{ k }}
        </div>
        <div v-for="k in dataConnection" :key="k">
          {{ k }}
        </div>
      </el-card>
    </el-drawer>
  </div>
</template>

<script>
import Peer from "peerjs";
export default {
  name: "Videochat",
  data() {
    return {
      chatrole: "",
      drawer: false,
      peerId: null,
      peer: null,
      selfid: null,
      localStream: null,
      conn: null,
      connStatus: "Unconnected",
      msg: "",
      inputmsg: null,
      url001:
        "https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/89/78/6797889/6797889_da3-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1612286863&gen=playurl&os=kodobv&oi=978800370&trid=e879e59beb8a47a19728b10316f3f0e5h&platform=html5&upsig=d7a302c76c539ae1b6748312a3683704&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=524602686&logo=80000000",
      dataURL: {
        protocol: "协议: " + window.location.protocol,
        hostname: "主机地址名: " + window.location.hostname,
        port: "端口号: " + window.location.port,
        pathname: "路径名: " + window.location.pathname,
      },
      dataHardware: {
        cpu: "CPU个数: " + window.navigator.hardwareConcurrency,
        storage: "设备存储: " + window.navigator.deviceMemory,
        touch: "最大触点数: " + window.navigator.maxTouchPoints,
      },
      dataConnection: {
        na: "用户代理: " + window.navigator.userAgent,
        vendor: "开发商: " + window.navigator.vendor,
        platform: "操作系统: " + window.navigator.platform,
        ol: "联网状态: " + (window.navigator.onLine ? "在线" : "离线"),
        condl: "网络下行速度: " + window.navigator.connection.downlink,
        conet: "网络类型: " + window.navigator.connection.effectiveType,
        conrtt: "估算往返时间: " + window.navigator.connection.rtt,
      },
    };
  },
  props: {
    room: Boolean,
  },
  watch: {
    chatrole() {
      if (this.chatrole == true) {
        this.receiver();
      } else {
        this.sender();
      }
    },
  },
  mounted() {
    this.chatrole = this.room;
    if (this.room) {
      this.receiver();
    } else {
      this.sender();
    }
  },
  methods: {
    receiver() {
      // 初始化peer
      this.peer = new Peer({ 
        debug: 2,
        config: {
          'iceServers': [
            { url: 'stun:stun1.l.google.com:19302' },
            { 
              url: 'turn:numb.viagenie.ca:3478',username: '807850644@qq.com',credential:"ZXCVBNM" 
            }
          ]
        } 
      });
      // 获取peer的ID
      this.peer.on("open", () => {
        this.selfid = this.peer.id;
      });
      // 接收消息
      this.peer.on("connection", (c) => {
        // 连接打开: 已连接，不用手动连
        if (this.conn && this.conn.open) {
          c.on("open", function () {
            c.send("Already connected to another client");
            setTimeout(function () {
              c.close();
            }, 500);
          });
          return;
        }
        this.conn = c;
        this.connStatus = `Connected to ${this.conn.peer}`;
        // 收到数据
        this.conn.on("data", (data) => {
          this.msg = `${this.msg} \n ${this.conn.peer}:${data}`;
        });
        // 连接关闭
        this.conn.on("close", () => {});
      });
      // 接收视频
      this.peer.on("call", (receiveCall) => {
        if (this.localStream == null) {
          this.setLocalVideo();
        }
        receiveCall.answer(this.localStream);
        receiveCall.on("stream", (remoteStream) => {
          let peerv = document.getElementById("peerv");
          peerv.srcObject = remoteStream;
        });
        receiveCall.on("error", (err) => {
          console.log(err);
        });
      });
      // 失联重连
      this.peer.on("disconnected", () => {
        this.connStatus = `Disconnected to ${this.peerId}, reconnecting...`;
        this.peer.id = this.selfid;
        this.peer.reconnect();
      });
      // 关闭
      this.peer.on("close", () => {
        this.connStatus = `Connection close`;
      });
      // 报错
      this.peer.on("error", (err) => {
        console.log(err);
      });
    },
    sender() {
      // 初始化peer
      this.peer = new Peer({ 
        debug: 2,
        config: {
          'iceServers': [
            { url: 'stun:stun1.l.google.com:19302' },
            { 
              url: 'turn:numb.viagenie.ca:3478',username: '807850644@qq.com',credential:"ZXCVBNM" 
            }
          ]
        }
      });
      // 获取peer的ID
      this.peer.on("open", () => {
        this.selfid = this.peer.id;
      });
      // 接收消息
      // this.peer.on("connection", (c) => {
      //   // 连接打开: 不能被动连接，只能主动发出连接
      //   c.on("open", () => {});
      //   // 连接关闭
      //   c.on("close", () => {});
      // });
      // 接收视频: 不能被动连接，只能主动发出连接
      // this.peer.on("call", (receiveCall) => {
      // });
      // 失联重连
      this.peer.on("disconnected", () => {
        this.connStatus = `Disconnected to ${this.peerId}, reconnecting...`;
        this.peer.id = this.selfid;
        this.peer.reconnect();
      });
      // 关闭
      this.peer.on("close", () => {});
      // 报错
      this.peer.on("error", (err) => {
        console.log(err);
      });
    },
    // 设置视频流
    async setLocalVideo() {
      navigator.mediaDevices.getUserMedia =
        navigator.mediaDevices.getUserMedia ||
        navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia ||
        navigator.getUserMedia;
      this.localStream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true,
      });
      let selfv = document.getElementById("selfv");
      selfv.srcObject = this.localStream;
    },
    // 发出视频
    callPeer() {
      if (this.chatrole == true) {
        this.$notify({
          title: "Notification",
          message: "Please adjust to sender first!",
          duration: 5000,
          type: "warning",
        });
      } else {
        if (this.peerId == null) {
          this.$notify({
            title: "Notification",
            message: "Please type in peer id to call!",
            duration: 5000,
            type: "warning",
          });
        } else {
          if (this.localStream == null) {
            this.$notify({
              title: "Notification",
              message: "Please test camera first!",
              duration: 5000,
              type: "warning",
            });
          } else {
            this.peerId = this.peerId.replace(/\s+/g, "");
            const sendCall = this.peer.call(this.peerId, this.localStream);
            sendCall.on("stream", (remoteStream) => {
              let peerv = document.getElementById("peerv");
              peerv.srcObject = remoteStream;
            });
            sendCall.on("error", (err) => {
              console.log(err);
            });
            // 如果不显示对方
            this.$notify({
              title: "Notification",
              message:
                "If you can't see the other side video, please click 'call' again",
              duration: 5000,
              type: "warning",
            });
          }
        }
      }
    },
    // 发起连接+收消息
    connectPeer() {
      if (this.chatrole == true) {
        this.$notify({
          title: "Notification",
          message: "Please adjust to sender first!",
          duration: 5000,
          type: "warning",
        });
      } else {
        if (this.peerId == null) {
          this.$notify({
            title: "Notification",
            message: "Please type in peer id to connect!",
            duration: 5000,
            type: "warning",
          });
        } else {
          // 旧连接关闭
          if (this.conn) {
            this.conn.close();
          }
          this.peerId = this.peerId.replace(/\s+/g, "");
          this.conn = this.peer.connect(this.peerId);
          // 打开连接
          this.conn.on("open", () => {
            this.connStatus = `Connected to ${this.conn.peer}`;
          });
          // 接收数据
          this.conn.on("data", (data) => {
            this.msg = `${this.msg} \n ${this.conn.peer}:${data}`;
          });
          // 关闭连接
          this.conn.on("close", () => {
            this.connStatus = `Connection close`;
          });
          // 连接报错
          this.conn.on("error", (err) => {
            console.log(err);
          });
        }
      }
    },
    // 发消息
    sendMsgToPeer() {
      if (this.conn == null) {
        this.$notify({
          title: "Notification",
          message: "Please connect to peer first!",
          duration: 5000,
          type: "warning",
        });
      } else {
        let content = this.inputmsg;
        if (this.conn && this.conn.open) {
          this.conn.send(this.inputmsg);
          this.inputmsg = "";
          this.msg = `${this.msg} \n ${this.selfid}(self):${content}`;
        } else {
          this.connStatus = `Disconnected to ${this.peerId}, reconnecting...`;
        }
      }
    },
    allowDrop(ev) {
      ev.preventDefault();
    },
    drag(ev) {
      ev.dataTransfer.setData("Text", ev.target.innerText);
    },
    drop(ev) {
      ev.preventDefault();
      var data = ev.dataTransfer.getData("Text");
      ev.target.src = data;
    },
  },
};
</script>

<style scoped>
/* 总宽度 */
.fullwidth {
  width: 45vw;
}

/* 整体 */
.whole {
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

/* 右部 */
.videoArea {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  min-height: 80vh;
  min-width: 50vw;
  border: 1px dashed lightgray;
}
/* 右顶部按钮 */
.videoBtn {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 6vh;
  min-width: 45vw;
}
/* 右下部视频 */
.video {
  border: 1px dashed lightgray;
}

#selfv,
#peerv {
  width: 50vw;
  height: 40vh;
}

/* ------------------------------------------------ */
/* 左部 */
.chattingArea {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  min-width: 50vw;
  min-height: 80vh;
  border: 1px dashed lightgray;
}
/* 左顶部按钮 */
.chatBtn {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 6vh;
  min-width: 45vw;
}
/* url框 */
.urls {
  width: 45vw;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  display: inline-block;
}
/* 左中上部卡片 */
.cards {
  min-width: 45vw;
  min-height: 10vh;
}
/* 左中下部消息框 */
.chattingHistory {
  min-height: 54vh;
  min-width: 45vw;
}
/* 左下部输入框 */
.inputArea {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 10vh;
  border: 1px dashed lightgray;
  min-width: 50vw;
}
</style>