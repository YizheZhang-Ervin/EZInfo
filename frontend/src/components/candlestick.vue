<template>
  <section class="whole">
    <!-- 小屏幕 -->
    <div id="smallscreen">
      <h3><i class="el-icon-warning"></i>Please use larger screen(>600*600) for better experience!</h3>
    </div>
    <!-- 大屏幕 -->
    <el-card class="cards" shadow="hover">
        <div slot="header" class="headerArea">
            <span>Shanghai Composite Index</span>
            <section>
              <el-button class="btn"><a href="/api/ssec/web/">Refresh</a></el-button>
              <el-button class="btn"><a href="/api/ssec/csv/">Import From CSV</a></el-button>
              <el-button class="btn"><a href="/api/ssec/db/">Update From Web</a></el-button>
            </section>
        </div>
        <div id="echarts"></div>
    </el-card>
  </section>
</template>

<script>
const axios = require("axios");
const echarts = require("echarts");

export default {
  name: "Candlestick",
  data() {
    return {
        allData:""
    };
  },
  mounted() {
      this.get();
  },
  methods: {
    get() {
      axios.get(`/api/ssec/db/`).then(
        (response) => {
          if (response.data.error == "error") {
            console.log("bakend error");
          } else {
            this.allData = response.data;
            this.plot();
          }
        },
        (err) => {
          console.log("frontend error", err);
        }
      );
    },
    plot() {
      let myChart = echarts.init(document.getElementById("echarts"));
      let option = this.getOption();
      myChart.setOption(option);
    },
    getData() {
      // var all = [
      //     ['2013/1/24', 2320.26, 2320.26, 2287.3, 2362.94,86160000],
      //     ['2013/1/25', 2300, 2291.3, 2288.26, 2308.38,79330000]];
      var all = this.allData;
      var price = [];
      var date = [];
      var volume = [];
      for (var i = 0; i < all.length; i++) {
        date.push(all[i].slice(0, 1));
        price.push(all[i].slice(1, 5));
        volume.push(all[i].slice(-1)[0]);
      }
      var data = { price: price, date: date, volume: volume };
      return data;
    },
    getOption() {
      var upColor = "#ec0000";
      var upBorderColor = "#8A0000";
      var downColor = "#00da3c";
      var downBorderColor = "#008F28";
      var data = this.getData();

      function calculateMA(dayCount) {
        var result = [];
        for (var i = 0, len = data.date.length; i < len; i++) {
          if (i < dayCount) {
            result.push("-");
            continue;
          }
          var sum = 0;
          for (var j = 0; j < dayCount; j++) {
            sum += data.price[i - j][1];
          }
          result.push(sum / dayCount);
        }
        return result;
      }
      let option = {
        // title: {
        //     text: 'Shanghai Composite Index',
        //     left: 'center'
        // },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
          },
          backgroundColor: "rgba(245, 245, 245, 0.8)",
          borderWidth: 1,
          borderColor: "#ccc",
          padding: 10,
          textStyle: {
            color: "#000",
          },
          position: function (pos, params, el, elRect, size) {
            var obj = { top: 10 };
            obj[["left", "right"][+(pos[0] < size.viewSize[0] / 2)]] = 30;
            return obj;
          },
        },
        legend: {
          top: "320em",
          data: ["Day K", "MA5", "MA10", "MA20", "MA30"],
        },
        axisPointer: {
          link: { xAxisIndex: "all" },
          label: {
            backgroundColor: "#777",
          },
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: false,
            },
            brush: {
              type: ["lineX", "clear"],
            },
          },
        },
        visualMap: {
          show: false,
          seriesIndex: 5,
          dimension: 2,
          pieces: [
            {
              value: 1,
              color: downColor,
            },
            {
              value: -1,
              color: upColor,
            },
          ],
        },
        grid: [
          {
            height: "220em",
          },
          {
            top: "370em",
            height: "80em",
          },
        ],
        xAxis: [
          {
            type: "category",
            data: data.date,
            scale: true,
            boundaryGap: false,
            axisLine: { onZero: false },
            splitLine: { show: false },
            splitNumber: 20,
            min: "dataMin",
            max: "dataMax",
          },
          {
            type: "category",
            gridIndex: 1,
            data: data.date,
            scale: true,
            boundaryGap: false,
            axisLine: { onZero: false },
            axisTick: { show: false },
            splitLine: { show: false },
            axisLabel: { show: false },
            splitNumber: 20,
            min: "dataMin",
            max: "dataMax",
          },
        ],
        yAxis: [
          {
            scale: true,
            splitArea: {
              show: true,
            },
          },
          {
            scale: true,
            gridIndex: 1,
            splitNumber: 2,
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: { show: false },
          },
        ],
        dataZoom: [
          {
            type: "inside",
            xAxisIndex: [0, 1],
            start: 50,
            end: 100,
          },
          {
            show: true,
            type: "slider",
            xAxisIndex: [0, 1],
            top: "355em",
            start: 50,
            end: 100,
          },
        ],
        series: [
          {
            name: "Day K",
            type: "candlestick",
            data: data.price,
            itemStyle: {
              color: upColor,
              color0: downColor,
              borderColor: upBorderColor,
              borderColor0: downBorderColor,
            },
            markPoint: {
              label: {
                normal: {
                  formatter: function (param) {
                    return param != null ? Math.round(param.value) : "";
                  },
                },
              },
              data: [
                // {
                //     name: 'XX标点',
                //     coord: ['2013/5/31', 2300],
                //     value: 2300,
                //     itemStyle: {
                //         color: 'rgb(41,60,85)'
                //     }
                // },
                {
                  name: "highest value",
                  type: "max",
                  valueDim: "highest",
                },
                {
                  name: "lowest value",
                  type: "min",
                  valueDim: "lowest",
                },
                {
                  name: "average value on close",
                  type: "average",
                  valueDim: "close",
                },
              ],
              tooltip: {
                formatter: function (param) {
                  return param.name + "<br>" + (param.data.coord || "");
                },
              },
            },
            markLine: {
              symbol: ["none", "none"],
              data: [
                [
                  {
                    name: "from lowest to highest",
                    type: "min",
                    valueDim: "lowest",
                    symbol: "circle",
                    symbolSize: 10,
                    label: {
                      show: false,
                    },
                    emphasis: {
                      label: {
                        show: false,
                      },
                    },
                  },
                  {
                    type: "max",
                    valueDim: "highest",
                    symbol: "circle",
                    symbolSize: 10,
                    label: {
                      show: false,
                    },
                    emphasis: {
                      label: {
                        show: false,
                      },
                    },
                  },
                ],
                {
                  name: "min line on close",
                  type: "min",
                  valueDim: "close",
                },
                {
                  name: "max line on close",
                  type: "max",
                  valueDim: "close",
                },
              ],
            },
          },
          {
            name: "Volume",
            type: "bar",
            xAxisIndex: 1,
            yAxisIndex: 1,
            data: data.volume,
          },
          {
            name: "MA5",
            type: "line",
            data: calculateMA(5),
            smooth: true,
            lineStyle: {
              opacity: 0.5,
            },
          },
          {
            name: "MA10",
            type: "line",
            data: calculateMA(10),
            smooth: true,
            lineStyle: {
              opacity: 0.5,
            },
          },
          {
            name: "MA20",
            type: "line",
            data: calculateMA(20),
            smooth: true,
            lineStyle: {
              opacity: 0.5,
            },
          },
          {
            name: "MA30",
            type: "line",
            data: calculateMA(30),
            smooth: true,
            lineStyle: {
              opacity: 0.5,
            },
          },
        ],
      };
      return option;
    },
  },
};
</script>

<style scoped>
@media (min-width: 600px) and (min-height: 600px) {
  #bigscreen {
    display: block;
  }
  #smallscreen {
    display: none;
  }
  .headerArea{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}
@media (max-width: 600px) {
  #bigscreen {
    display: block;
  }
  #smallscreen {
    display: block;
  }
  .headerArea{
    display: block;
  }
}

@media (max-height: 600px) {
  #bigscreen {
    display: block;
  }
  #smallscreen {
    display: block;
  }
  .headerArea{
    display: block;
  }
}

.whole{
  height: 100vh;
  width: 100vw;
  background-color: beige;
}

#echarts{
    height:50em;
    background-color: beige;
}

.cards {
  background-color: beige;
  height:60em;
  width: 100vw;
}

.btn{
    background-color: beige;
}

a{
    text-decoration: none;
}

h3{
  background-image: linear-gradient(45deg,gold,white);
  display: flex;
  align-items: center;
  justify-content: center;
  width:100vw;
}
</style>