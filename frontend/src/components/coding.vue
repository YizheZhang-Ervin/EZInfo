<template>
	<div class="whole">
		<!-- left part -->
		<section>
			<!-- top part: charts -->
			<section class="charts w50" id="charts"></section>
			<!-- bottom part: output -->
			<section class="output w50">
				<pre v-text="output" class="output-pre"></pre>
			</section>
		</section>
		<!-- right part: input -->
		<section class="rightpart">
			<section class="rightbtnArea">
				<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="post">Run Code</el-button>
				<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="clear('codes')">Clear Code</el-button>
				<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="clear('output')">Clear Output</el-button>
				<el-button class="btn" size="small" icon="el-icon-caret-right" round @click="clear('example')">Example Codes</el-button>
			</section>
			<textarea id="input" class="inputArea w50" v-model="input" @keydown="cancelTab($event)"></textarea>
		</section>
	</div>
</template>

<script>
const axios = require("axios");
const echarts = require("echarts");
export default {
	name: "Coding",
	components: {},
	data() {
		return {
			input: "class Run:\n  def run():\n    return {'x':[],'y':[],'y2':[]}",
			output: "",
			visualData: {
				x: [],
				y: [],
				y2: [],
			},
		};
	},
	mounted() {},
	methods: {
		post: function() {
			axios
				.post(`api/coding/`, {
					input: JSON.stringify(this.input),
				})
				.then(
					(response) => {
						if (response.data.error == "error") {
							console.log("backend error");
						} else {
							this.visualData = response.data.result;
							let date = new Date(Date.now());
							let time = date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
							let rst = "";
							if (this.visualData.x != undefined) {
								rst = `Output(${time})\n x:${this.visualData.x},\n y:${this.visualData.y},\n y2:${this.visualData.y2}\n\n`;
							} else {
								rst = `Output(${time})\n ${this.visualData.other}\n\n`;
							}
							this.output += rst;
							this.plot();
						}
					},
					function(err) {
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
		plot: function() {
			let myChart = echarts.init(document.getElementById("charts"));
			let option = {
				xAxis: {
					name: "Axis-X",
					type: "category",
					data: this.visualData.x,
				},
				yAxis: {
					name: "Axis-Y",
					type: "value",
				},
				series: [
					{
						data: this.visualData.y,
						type: "line",
						smooth: true,
					},
					{
						data: this.visualData.y2,
						type: "line",
						smooth: true,
					},
				],
				dataZoom: [
					{
						type: "inside",
					},
				],
				tooltip: {
					trigger: "axis",
				},
			};
			myChart.setOption(option);
		},
		clear(content) {
			if (content == "codes") {
				this.input = "class Run:\n  def run():\n    return {'x':[],'y':[],'y2':[]}";
			} else if (content == "output") {
				this.output = "";
			}else if(content=="example"){
				this.input = `class Run:\n  def run():\n    from datetime import datetime\n    from pandas_datareader import DataReader\n    stock="TGT"\n    t1=datetime(2020,1,1) \n    t2=datetime(2021,2,5)\n    data=DataReader(stock,"yahoo",t1,t2)\n    x = list(map(lambda x:str(x.date()),data.index))\n    y = list(map(float,data["Adj Close"].values))\n    y2 = list(map(float,data["Open"].values))\n    return {"x":x,"y":y,"y2":y2}`;
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
	.whole {
		display: flex;
	}
	.w50 {
		width: 50vw;
	}
}
@media (max-width: 800px) {
	.whole {
		display: flex;
		flex-direction: column-reverse;
	}
	.w50 {
		width: 100vw;
	}
}

@media (max-height: 700px) {
	.whole {
		display: flex;
		flex-direction: column-reverse;
	}
	.w50 {
		width: 100vw;
	}
}

/* 整体 */
.whole {
	align-items: center;
	background: black;
	min-height: 100vh;
	width: 100vw;
}

/* 图表 */
.charts {
	height: 46vh;
	background: beige;
	border: 2px outset black;
}

/* 输出区 */
.output {
	height: 46vh;
	background: beige;
	border: 2px outset black;
	overflow: scroll;
}
/* 输出区内部 */
.output-pre {
	margin-left: 2vw;
	font-size: 1.4em;
}
/* 输入区 */
.rightpart {
	display: flex;
	align-self: center;
	justify-content: center;
	flex-direction: column;
}
/* 右侧按钮区 */
.rightbtnArea {
	min-height: 5vh;
}
/* 输入区内部 */
.inputArea {
	min-height: 88vh;
	background: rgba(255, 255, 255, 0.12);
	color: gold;
	font-size: 1.4em;
}
/* 输入区顶部按钮 */
.btn {
	background: transparent;
	color: gold;
	min-height: 4vh;
}
</style>
