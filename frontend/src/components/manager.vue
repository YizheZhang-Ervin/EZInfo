<template>
	<section>
		<!-- 登录 -->
		<section v-show="loginShow" class="loginArea">
			<el-card shadow="hover">
				<div slot="header" class="center">Manager Login</div>
				<el-form label-position="right" label-width="80px" :model="loginForm">
					<el-form-item label="Username">
						<el-input v-model="loginForm.username"></el-input>
					</el-form-item>
					<el-form-item label="Password">
						<el-input v-model="loginForm.password" show-password></el-input>
					</el-form-item>
					<el-form-item>
						<el-button plain round type="primary" @click="changePart">Login</el-button>
						<el-button plain round native-type="reset">Reset</el-button>
					</el-form-item>
				</el-form>
			</el-card>
		</section>
		<!-- 控制台 -->
		<div v-if="terminalShow">
			<!-- 菜单 -->
			<el-menu default-active="python" mode="horizontal" @select="changeTerminal" background-color="#142044" text-color="darkgrey" active-text-color="beige">
				<el-submenu index="1">
					<template slot="title">
						<i class="el-icon-monitor"></i>
						<span class="menuwords">Terminal</span>
					</template>
					<el-menu-item index="python"><i class="el-icon-key"></i>Python</el-menu-item>
					<el-menu-item index="sql"><i class="el-icon-key"></i>SQL</el-menu-item>
					<el-menu-item index="js"><i class="el-icon-key"></i>JavaScript</el-menu-item>
					<el-menu-item index="html"><i class="el-icon-key"></i>HTML</el-menu-item>
					<el-menu-item index="linux"><i class="el-icon-key"></i>Linux</el-menu-item>
				</el-submenu>
				<el-menu-item index="2">
					<router-link to="/home" class="menulink">
						<i class="el-icon-s-home"></i>
						<span class="menuwords">Back To Website</span>
					</router-link>
				</el-menu-item>
			</el-menu>
			<!-- python控制台 -->
			<Coding v-if="pythonShow"></Coding>
			<!-- sql/js/html控制台 -->
			<section v-if="cmdShow" class="cmd">
				<!-- leftpart -->
				<iframe class="w50 leftpart" :srcdoc="output"></iframe>
				<!-- rightpart -->
				<section class="rightpart">
					<p v-text="cmdTitle" class="cmdTitle"></p>
					<section class="rightbtnArea">
						<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="runCode">Run Code</el-button>
						<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="clear('codes')">Clear Code</el-button>
						<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="clear('output')">Clear Output</el-button>
						<section v-show="dbBtn">
							<el-button class="btn" size="small" icon="el-icon-caret-right" round><a href="/api/ssec/web/">Update From Web</a></el-button>
							<el-button class="btn" size="small" icon="el-icon-caret-right" round><a href="/api/ssec/csv/">Import From CSV</a></el-button>
							<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="getDB">Get From DB</el-button>
						</section>
					</section>
					<textarea id="input" class="w50 inputArea" v-model="input" @keydown="cancelTab($event)"></textarea>
				</section>
			</section>
		</div>
	</section>
</template>

<script>
import Coding from "./coding.vue";
const axios = require("axios");
export default {
	name: "Manager",
	components: {
		Coding,
	},
	data() {
		return {
			loginShow: true,
			terminalShow: false,
			pythonShow: true,
			cmdShow: false,
			dbBtn: false,
			loginForm: {
				username: "",
				password: "",
			},
			cmdTitle: "Super SQL v1.0",
			input: ">>",
			output: "",
		};
	},
	methods: {
		runCode() {
			try {
				let sentence = this.input.substr(2);
				if (this.cmdTitle == "Super SQL v1.0") {
					this.get();
				} else if (this.cmdTitle == "Super JavaScript v1.0") {
					this.output = eval(sentence);
				} else if (this.cmdTitle == "Super HTML v1.0") {
					this.output = sentence;
				} else if (this.cmdTitle == "Super Linux v1.0") {
					this.getOS();
				}
			} catch (err) {
				this.$notify({
					title: "Notification",
					message: "Wrong Codes",
					type: "warning",
					duration: 5000,
				});
			}
		},
		get: function() {
			axios.get(`api/coding/?pkg=${this.input.substr(2)}`).then(
				(response) => {
					if (response.data.error == "error") {
						console.log("backend error");
						this.$notify({
							title: "Notification",
							message: "Wrong Codes",
							type: "warning",
							duration: 5000,
						});
					} else {
						this.output = `<pre>${response.data.result}</pre>`;
					}
				},
				(err) => {
					console.log(err.data);
					this.$notify({
						title: "Notification",
						message: "Wrong Codes",
						type: "warning",
						duration: 5000,
					});
				}
			);
		},
		getOS: function() {
			axios.post(`api/coding2/`, {input: JSON.stringify(this.input.substr(2)),})
			.then((response) => {
					if (response.data.error == "error") {
						console.log("backend error");
						this.$notify({
							title: "Notification",
							message: "Wrong Codes",
							type: "warning",
							duration: 5000,
						});
					} else {
						this.output = `<pre>${response.data.result}</pre>`;
					}
				},
				(err) => {
					console.log(err.data);
					this.$notify({
						title: "Notification",
						message: "Wrong Codes",
						type: "warning",
						duration: 5000,
					});
				}
			);
		},
        getDB: function() {
			let sql = "SELECT date,open,close,low,high,volume FROM shindex order by date ASC";
            axios.get(`api/coding/?pkg=${sql}`).then(
				(response) => {
					if (response.data.error == "error") {
						console.log("backend error");
						this.$notify({
							title: "Notification",
							message: "Wrong Codes",
							type: "warning",
							duration: 5000,
						});
					} else {
						this.output = `<pre>${response.data.result}</pre>`;
					}
				},
				(err) => {
					console.log(err.data);
					this.$notify({
						title: "Notification",
						message: "Wrong Codes",
						type: "warning",
						duration: 5000,
					});
				}
			);
		},
		changePart() {
			if ((this.loginForm.username == "ez") & (this.loginForm.password == "ez")) {
				this.loginShow = false;
				this.terminalShow = true;
			} else {
				this.$notify({
					title: "Notification",
					message: "Wrong username or password",
					type: "warning",
					duration: 5000,
				});
			}
		},
		changeTerminal(key) {
			if (key == "python") {
				this.pythonShow = true;
				this.cmdShow = false;
				this.dbBtn = false;
			} else {
				this.pythonShow = false;
				this.cmdShow = true;
				if (key == "sql") {
					this.cmdTitle = "Super SQL v1.0";
					this.dbBtn = true;
                    this.input = ">>";
					this.output="";
				} else if (key == "js") {
					this.cmdTitle = "Super JavaScript v1.0";
					this.dbBtn = false;
                    this.input = ">>";
					this.output="";
				} else if (key == "html") {
					this.cmdTitle = "Super HTML v1.0";
					this.dbBtn = false;
                    this.input = ">>";
					this.output="";
				} else if (key == "linux") {
					this.cmdTitle = "Super Linux v1.0";
					this.dbBtn = false;
                    this.input = ">>";
					this.output="";
				}
			}
		},
		clear(content) {
			if (content == "codes") {
				this.input = ">>";
			} else if (content == "output") {
				this.output = "";
			}
		},
		cancelTab(e) {
			if (e.keyCode == 9) {
				e.preventDefault();
				// 任意位置tab键插入四个空格
				let ip = document.getElementById("input");
				let value = "    ";
				var startPos = ip.selectionStart;
				var endPos = ip.selectionEnd;
				var scrollTop = ip.scrollTop;
				ip.value = ip.value.substring(0, startPos) + value + ip.value.substring(endPos, ip.value.length);
				ip.focus();
				ip.selectionStart = startPos + value.length;
				ip.selectionEnd = startPos + value.length;
				ip.scrollTop = scrollTop;
			}
		},
	},
};
</script>

<style scoped>
@media (min-width: 800px) and (min-height: 700px) {
	.cmd {
		display: flex;
	}
	.w50 {
		width: 50vw;
	}
	.menuwords {
		display: inline;
	}
}
@media (max-width: 800px) {
	.cmd {
		display: flex;
		flex-direction: column-reverse;
	}
	.w50 {
		width: 100vw;
	}
	.menuwords {
		display: none;
	}
}

@media (max-height: 700px) {
	.cmd {
		display: flex;
		flex-direction: column-reverse;
	}
	.w50 {
		width: 100vw;
	}
	.menuwords {
		display: none;
	}
}

.menulink {
	display: inline-block;
	width: 100%;
}

a {
	text-decoration: none;
	color: darkgray;
}

.btn a {
	color: gold;
}

.loginArea {
	display: flex;
	align-items: center;
	justify-content: center;
	width: 100vw;
	height: 100vh;
	background-image: linear-gradient(45deg, #142044, white);
}

.center {
	text-align: center;
}

/* termainal */
/* 整体 */
.cmd {
	align-items: center;
	justify-content: center;
	width: 100vw;
	background: black;
	min-height: 100vh;
}

/* 右部 */
.rightpart {
	display: flex;
	align-self: center;
	justify-content: center;
	flex-direction: column;
}

/* 右上标题 */
.cmdTitle {
	color: gold;
	font-size: 1.5em;
	min-height: 5vh;
	text-indent: 10px;
}

/* 右上部按钮区 */
.rightbtnArea {
	min-height: 5vh;
}

/* 右上部按钮区按钮 */
.btn {
	background: transparent;
	color: gold;
	min-height: 4vh;
}

/* 右下部输入区 */
.inputArea {
	min-height: 90vh;
	background: rgba(255, 255, 255, 0.12);
	color: gold;
	font-size: 1.4em;
}

/* 左部 */
.leftpart {
	height: 100vh;
	border: none;
	background-color: beige;
}
</style>
