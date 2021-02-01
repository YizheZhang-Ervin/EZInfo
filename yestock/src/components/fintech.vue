<template>
  <div class="whole">
    <!-- left part -->
    <section>
      <!-- top part: charts -->
      <section class="charts" id="charts"></section>
      <!-- bottom part: output -->
      <section class="output">
        <pre v-text="output" class="output-pre"></pre>
      </section>
    </section>
    <!-- right part: input -->
    <section>
      <el-button
        class="btn"
        size="small"
        icon="el-icon-caret-right"
        round
        @click="post"
        >Run Code</el-button
      >
      <el-button
        class="btn"
        size="small"
        icon="el-icon-caret-right"
        round
        @click="clear('codes')"
        >Clear Code</el-button
      >
      <el-button
        class="btn"
        size="small"
        icon="el-icon-caret-right"
        round
        @click="clear('output')"
        >Clear Output</el-button
      >
      <textarea id="input" class="input" v-model="input" @keydown="cancelTab($event)"></textarea>
    </section>
  </div>
</template>

<script>
const axios = require("axios");
const echarts = require("echarts");
export default {
  name: "Fintech",
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
    get: function () {
      axios.get(`api/fintech/`).then(
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
        .post(`api/fintech/`, {
          input: JSON.stringify(this.input),
        })
        .then(
          (response) => {
            if (response.data.error == "error") {
              console.log("backend error");
            } else {
              this.visualData = response.data.result;
              let date = new Date(Date.now());
              let time = date.getHours() + ":" +date.getMinutes() +":" +date.getSeconds();
              let rst = ""
              if(this.visualData.x!=undefined){
                rst = `Output(${time})\n x:${this.visualData.x},\n y:${this.visualData.y},\n y2:${this.visualData.y2}\n\n`;
              }else{
                rst = `Output(${time})\n ${this.visualData.other}\n\n`
              }
              this.output += rst;
              this.plot();
            }
          },
          function (err) {
            console.log(err.data);
          }
        );
    },
    plot: function () {
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
        if(content=="codes"){
            this.input = "class Run:\n  def run():\n    return {'x':[],'y':[],'y2':[]}";
        }else if(content=="output"){
            this.output = "";
        }
    },
    cancelTab(e){
        if(e.keyCode==9){
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
    }
  },
};
</script>

<style scoped>
.whole {
  display: flex;
  align-items: center;
  background: black;
}

.charts {
  height: 43vh;
  width: 50vw;
  background: beige;
  border: 2px outset black;
}

.output {
  height: 43vh;
  width: 50vw;
  background: beige;
  border: 2px outset black;
  overflow: scroll;
}

.output-pre{
    margin-left: 2vw;
    font-size: 1.4em;
}

.input {
  height: 82vh;
  width: 50vw;
  background: rgba(255, 255, 255, 0.12);
  color: gold;
  font-size: 1.4em;
}

.btn {
  background: transparent;
  color: gold;
  min-height: 4vh;
}
</style>