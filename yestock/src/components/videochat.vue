<template>
  <div class="whole">
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
      </section>
      <el-card class="box-card cards">
        Connection Status:
        <p v-text="connStatus" style="display: inline"></p>
        <br />
        Your Id:
        <p v-text="selfid" style="display: inline"></p>
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
      <video id="selfv" autoplay class="video"></video>
      <video id="peerv" autoplay class="video"></video>
    </section>
  </div>
</template>

<script>
import Peer from "peerjs";
export default {
  name: "Videochat",
  data() {
    return {
      peerId: null,
      peer: null,
      localStream: null,
      conn: null,
      connStatus: "Unconnected",
      msg: "",
      inputmsg: null,
      selfid: null,
    };
  },
  mounted() {
    this.initializePeer();
  },
  methods: {
    initializePeer() {
      // 初始化peer
      this.peer = new Peer();
      // 获取peer的ID
      this.peer.on("open", () => {
        this.selfid = this.peer.id;
      });
      // 接收消息
      this.peer.on("connection", (c) => {
        this.conn = c;
        this.connStatus = `Connected to ${this.conn.peer}`;
        this.conn.on("data", (data) => {
          this.msg = `${this.msg} \n ${this.conn.peer}:${data}`;
        });
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
      });
    },
    // 设置视频流
    async setLocalVideo() {
      navigator.mediaDevices.getUserMedia =
        navigator.mediaDevices.getUserMedia ||
        navigator.getUserMedia ||
        navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia;
      this.localStream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true,
      });
      let selfv = document.getElementById("selfv");
      selfv.srcObject = this.localStream;
    },
    // 发出视频
    callPeer() {
      if (this.peerId == null) {
        this.$notify({
          title: "Notification",
          message: "Please type in peer id to call!",
          duration: 5000,
          type: 'warning'
        });
      } else {
        if (this.localStream == null) {
          this.$notify({
            title: "Notification",
            message: "Please test camera first!",
            duration: 5000,
            type: 'warning'
          });
        } else {
          const sendCall = this.peer.call(this.peerId, this.localStream);
          sendCall.on("stream", (remoteStream) => {
            let peerv = document.getElementById("peerv");
            peerv.srcObject = remoteStream;
          });
          //   如果不显示对方
          this.$notify({
            title: "Notification",
            message:
              "If you can't see the other side video, please click 'call' again",
            duration: 5000,
            type: 'warning'
          });
        }
      }
    },
    // 发起连接+收消息
    connectPeer() {
      if (this.peerId == null) {
        this.$notify({
          title: "Notification",
          message: "Please type in peer id to connect!",
          duration: 5000,
          type: 'warning'
        });
      } else {
        this.conn = this.peer.connect(this.peerId, {
          reliable: true,
        });
        this.conn.on("open", () => {
          this.connStatus = `Connected to ${this.conn.peer}`;
        });
        this.conn.on("data", (data) => {
          this.msg = `${this.msg} \n ${this.conn.peer}:${data}`;
        });
      }
    },
    // 发消息
    sendMsgToPeer() {
      if (this.conn == null) {
        this.$notify({
          title: "Notification",
          message: "Please connect to peer first!",
          duration: 5000,
          type: 'warning'
        });
      } else {
        let content = this.inputmsg;
        this.conn.send(this.inputmsg);
        this.inputmsg = "";
        this.msg = `${this.msg} \n ${this.selfid}(self):${content}`;
      }
    },
  },
};
</script>

<style scoped>
/* 整体 */
.whole {
  display: flex;
  align-items: center;
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
  min-height: 86vh;
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
/* 左中上部卡片 */
.cards {
  min-width: 45vw;
  min-height: 10vh;
}
/* 左中下部消息框 */
.chattingHistory {
  min-height: 60vh;
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