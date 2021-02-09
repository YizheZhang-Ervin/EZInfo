<template>
	<div class="whole mh93">
		<!-- video -->
		<section class="videoArea mw50 mh93">
			<section class="videoBtn mw45 mh6">
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
					@click="setLocalVideo"
					icon="el-icon-video-camera"
					>Use Camera</el-button
				>
				<el-button
					type="primary"
					plain
					round
					@click="setScreenShotVideo"
					icon="el-icon-monitor"
					>Use Screenshot</el-button
				>
			</section>
			<video
				id="selfv"
				autoplay
				class="video w50 mh43"
				@drop="drop($event)"
				@dragover="allowDrop($event)"
			></video>
			<video id="peerv" autoplay class="video w50 mh43"></video>
		</section>
		<!-- chatting -->
		<section class="chattingArea mw50 mh93">
			<section class="chatBtn mw45 mh6">
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
			<el-card class="box-card cards mw50 mh10">
				<section class="flexIdArea">
					<el-input v-model="definedId" placeholder="use custom id">
						<el-switch
							slot="prepend"
							v-model="chatrole"
							active-color="lightgreen"
							inactive-color="lightblue"
							active-text="Receiver"
							inactive-text="Sender"
						>
						</el-switch>
						<el-button
							icon="el-icon-check"
							slot="append"
							circle
							@click="refresh"
						></el-button>
					</el-input>
				</section>

				<br />
				Connection Status:
				<p v-text="connStatus" style="display: inline"></p>
				<br />
				Your Id:
				<p v-text="selfid" style="display: inline"></p>
				<br />
				* Video Player:
				<p
					@dragstart="drag($event)"
					draggable="true"
					v-text="url001"
					class="urls w-url"
				></p>
			</el-card>

			<pre v-text="msg" class="mw45 mh54"></pre>
			<section class="inputArea mw50 mh10">
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
		<el-drawer
			title="Connection Status"
			:visible.sync="drawer"
			direction="ltr"
			size="50%"
		>
			<el-card shadow="hover" class="card">
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
			serverConfig: {
				debug: 2,
				config: {
					iceServers: [
						// { url: "stun:stun1.l.google.com:19302" },
						{ url: "stun:0.peerjs.com:443" },
						{
							url: "turn:numb.viagenie.ca:3478",
							username: "553887054@qq.com",
							credential: "87654321",
						},
					],
				},
			},
			definedId: "",
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
				"You can play video via dragging URL/mp4 and dropping to video area",
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
			this.definedId = "";
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
		refresh() {
			if (this.chatrole == true) {
				this.receiver();
			} else {
				this.sender();
			}
		},
		receiver() {
			// 初始化peer
			if (this.definedId != "") {
				this.peer = new Peer(this.definedId, this.serverConfig);
			} else {
				this.peer = new Peer(this.serverConfig);
			}
			// 获取peer的ID
			this.peer.on("open", () => {
				this.selfid = this.peer.id;
			});
			// 接收消息
			this.peer.on("connection", (c) => {
				// 连接打开: 已连接，不用手动连
				if (this.conn && this.conn.open) {
					c.on("open", function() {
						c.send("Already connected to another client");
						setTimeout(function() {
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
			if (this.definedId != "") {
				this.peer = new Peer(this.definedId, this.serverConfig);
			} else {
				this.peer = new Peer(this.serverConfig);
			}
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
		// 设置桌面流
		async setScreenShotVideo() {
			this.localStream = await navigator.mediaDevices.getDisplayMedia({
				video: {
					cursor: "always",
				},
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
							message: "Please click use camera/screenshot first!",
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
@media (max-width: 1000px) {
	/* 整体 */
	.whole {
		display: flex;
		align-items: flex-start;
		justify-content: center;
		flex-direction: column;
		width: 100vw;
	}
	/* 总宽度 */
	.mw50 {
		min-width: 100vw;
	}

	.w50 {
		width: 100vw;
	}

	.mw45 {
		min-width: 90vw;
	}

	.w-url {
		width: 90vw;
	}
	.videoBtn {
		display: block;
	}
	.chatBtn {
		display: block;
	}
}

@media (max-height: 700px) {
	/* 整体 */
	.whole {
		display: flex;
		align-items: flex-start;
		justify-content: center;
		flex-direction: column;
		width: 100vw;
	}
	/* 总宽度 */
	.mw50 {
		min-width: 100vw;
	}

	.w50 {
		width: 100vw;
	}

	.mw45 {
		min-width: 90vw;
	}

	.w-url {
		width: 90vw;
	}
	.videoBtn {
		display: block;
	}
	.chatBtn {
		display: block;
	}
}
@media (min-width: 1000px) and (min-height: 700px) {
	/* 整体 */
	.whole {
		display: flex;
		align-items: flex-start;
		justify-content: center;
		width: 100vw;
	}

	/* 总宽度 */
	.mw50 {
		min-width: 50vw;
	}

	.w50 {
		width: 50vw;
	}

	.mw45 {
		min-width: 45vw;
	}

	.w-url {
		width: 45vw;
	}
	.videoBtn {
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.chatBtn {
		display: flex;
		align-items: center;
		justify-content: center;
	}
}
/* 总高度 */
.mh93 {
	min-height: 100vh;
}
.mh6 {
	min-height: 6vh;
}
.mh10 {
	min-height: 10vh;
}
.mh54 {
	min-height: 61vh;
}
.mh43 {
	max-height: 46vh;
	height: 46vh;
}

/* video部分 */
.videoArea {
	display: flex;
	align-items: center;
	justify-content: flex-start;
	flex-direction: column;
	border: 1px dashed lightgray;
}

/* 下部视频 */
.video {
	border: 1px dashed lightgray;
}

/* ------------------------------------------------ */
/* chatting部分 */
.chattingArea {
	display: flex;
	align-items: center;
	justify-content: flex-start;
	flex-direction: column;
	border: 1px dashed lightgray;
}

/* 自定义id */
.flexIdArea {
	display: flex;
	align-items: center;
	justify-content: space-around;
}
/* url框 */
.urls {
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	display: inline-block;
}

/* 参数抽屉 */
.card {
	overflow: scroll;
	height: 70vh;
}

/* 下部输入框 */
.inputArea {
	display: flex;
	align-items: center;
	justify-content: center;
	border: 1px dashed lightgray;
}
</style>
