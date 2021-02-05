<template>
  <section>
    <!-- 小屏幕 -->
    <div id="smallscreen">
      <h3><i class="el-icon-warning"></i>Please use larger screen(>800*700) for better experience!</h3>
    </div>
    <!-- 大屏幕 -->
    <div id="bigscreen">
      <!-- toolbar -->
      <section class="toolbar">
        <el-button type="info" round plain @click="createSheet"
          >New CSV</el-button
        >
        <el-button type="info" round plain @click="importCSV"
          >Import CSV</el-button
        >
        <input id="file" type="file" accept=".csv" hidden @change="loadCSV" />
        <el-button type="info" round plain @click="exportCSV"
          >Export CSV</el-button
        >
        <el-button type="info" round plain @click="addRow">Add Row </el-button>
        <el-button type="info" round plain @click="delRow">Del Row</el-button>
        <el-input v-model="computeExp" placeholder="enter expression" clearable>
          <div slot="prepend" v-text="computeRst"></div>
          <el-button
            slot="append"
            icon="el-icon-caret-right"
            @click="computeGrid"
          ></el-button>
        </el-input>
      </section>
      <!-- sheet -->
      <section id="table">
        <section id="sheet"></section>
      </section>
    </div>
  </section>
</template>

<script>
export default {
  name: "Excel",
  data: function () {
    return {
      existRow: 0,
      existCol: 0,
      computeExp: "",
      computeRst: "",
      mouseX: 0,
      mouseY: 0,
    };
  },
  mounted() {
    this.createSheet();
    // 移动获得坐标
    window.addEventListener("mousemove", this.mouseMove);
    // 点击格子取值到计算框
    window.onclick = this.selectGrid;
    // 移动鼠标单元格出现背景
    window.addEventListener("mousemove", this.slideGrid);
  },
  destroyed () {
    window.removeEventListener("mousemove", this.slideGrid);
  },
  methods: {
    createSheet() {
      // delete old node and add new node
      let tableNode = document.getElementById("table");
      let oldSheetNode = document.getElementById("sheet");
      tableNode.removeChild(oldSheetNode);
      let sheetNode = document.createElement("section");
      sheetNode.id = "sheet";
      tableNode.appendChild(sheetNode);
      for (let r = 0; r < 51; r++) {
        // x axis
        if (r == 0) {
          let row = document.createElement("div");
          row.style.display = "flex";
          sheetNode.appendChild(row);
          let axis = document.createElement("div");
          axis.style.minWidth = "30px";
          axis.style.border = "1px gray solid";
          row.appendChild(axis);
          for (let c = 1; c < 27; c++) {
            let cellNode = document.createElement("div");
            cellNode.style.display = "inline-block";
            cellNode.style.flexDirection = "row";
            cellNode.style.border = "1px gray solid";
            cellNode.style.height = "25px";
            cellNode.style.minWidth = "60px";
            cellNode.style.textAlign = "center";
            cellNode.innerHTML = String.fromCharCode(64 + c);
            row.appendChild(cellNode);
          }
          continue;
        }
        let row = document.createElement("div");
        row.className = "row";
        row.style.display = "flex";
        sheetNode.appendChild(row);
        // y axis
        let axis = document.createElement("div");
        axis.style.minWidth = "30px";
        axis.style.border = "1px gray solid";
        axis.style.textAlign = "center";
        axis.innerHTML = r;
        row.appendChild(axis);
        for (let c = 1; c < 27; c++) {
          let cellNode = document.createElement("div");
          cellNode.style.display = "inline-block";
          cellNode.style.flexDirection = "row";
          cellNode.contentEditable = true;
          cellNode.style.border = "1px gray solid";
          cellNode.style.height = "25px";
          cellNode.style.minWidth = "60px";
          cellNode.style.textAlign = "center";
          cellNode.id = String.fromCharCode(64 + c) + r;
          row.appendChild(cellNode);
        }
      }
      this.existRow = 50;
      this.existCol = 26;
    },
    addRow() {
      let sheetNode = document.getElementById("sheet");
      let row = document.createElement("div");
      row.style.display = "flex";
      sheetNode.appendChild(row);
      // y axis
      let axis = document.createElement("div");
      let curRow = this.existRow + 1;
      this.existRow += 1;
      axis.style.minWidth = "30px";
      axis.style.border = "1px gray solid";
      axis.style.textAlign = "center";
      axis.innerHTML = curRow;
      row.appendChild(axis);
      for (let c = 1; c < 27; c++) {
        let cellNode = document.createElement("div");
        cellNode.style.display = "inline-block";
        cellNode.style.flexDirection = "row";
        cellNode.contentEditable = true;
        cellNode.style.border = "1px gray solid";
        cellNode.style.height = "25px";
        cellNode.style.minWidth = "60px";
        cellNode.style.textAlign = "center";
        cellNode.id = String.fromCharCode(64 + c) + curRow;
        row.appendChild(cellNode);
      }
    },
    delRow() {
      let sheet = document.getElementById("sheet");
      sheet.removeChild(sheet.childNodes[sheet.childNodes.length - 1]);
      this.existRow -= 1;
    },
    importCSV() {
      document.getElementById("file").click();
    },
    loadCSV() {
      this.createSheet();
      let loadfile = document.getElementById("file");
      loadfile.click();
      let csv = loadfile.files[0];
      let fr = new FileReader();
      let recover = this.createSheet;
      fr.onload = function () {
        try {
          let rIdx = 0;
          // 切成行
          for (let r of fr.result.split("\n")) {
            if (r != "") {
              rIdx += 1;
              // 行切成格子
              let grids = r.split(",");
              let cIdx = 1;
              for (let g of grids) {
                let cIdx2 = String.fromCharCode(64 + cIdx);
                let cell = document.getElementById(cIdx2 + rIdx);
                cell.innerHTML = g;
                cIdx += 1;
              }
            }
          }
        } catch (err) {
          recover();
          alert("Too many rows or cols");
        }
      };
      fr.readAsText(csv);
    },
    exportCSV() {
      let rst = "";
      for (let i = 1; i < this.existRow + 1; i++) {
        let rowData = [];
        for (let j = 1; j < this.existCol + 1; j++) {
          let idx = String.fromCharCode(64 + j) + i;
          let temp = document.getElementById(idx).innerHTML;
          if (temp.slice(-1) != "\n") {
            rowData.push(temp);
          } else {
            rowData.push(temp.slice(0, -1));
          }
        }
        let rowData2 = encodeURIComponent(rowData.join(",") + "\n");
        rst += rowData2;
      }
      let time = new Date();
      let dld = document.createElement("a");
      dld.setAttribute("href", "data:application/csv;charset=utf-8," + rst);
      dld.setAttribute(
        "download",
        `output-${time.getHours()}H${time.getMinutes()}M.csv`
      );
      dld.click();
    },
    computeGrid() {
      this.computeRst = eval(this.computeExp);
    },
    selectGrid() {
      let ele = document.elementFromPoint(this.mouseX, this.mouseY);
      // if value is null
      if (ele.innerHTML != "") {
        // if click grid
        if (ele.id.match(/^\w\d$/)) {
          if (this.computeExp == "") {
            this.computeExp = this.computeExp + ele.innerHTML;
            this.computeRst = eval(this.computeExp);
          } else {
            this.computeExp = this.computeExp + "+" + ele.innerHTML;
            this.computeRst = eval(this.computeExp);
          }
        }
      }
    },
    slideGrid() {
      let sheet = document.getElementById("sheet");
      sheet.onmouseover = (ev) => {
        if (ev.target.nodeName.toLowerCase() == "div") {
          ev.target.style.backgroundColor = "lightblue";
        }
      };
      sheet.onmouseout = (ev) => {
        if (ev.target.nodeName.toLowerCase() == "div") {
          ev.target.style.backgroundColor = "transparent";
        }
      };
    },
    mouseMove(ev) {
      ev = ev || window.event;
      //鼠标移动的位置
      if (ev.pageX || ev.pageY) {
        this.mouseX = ev.pageX;
        this.mouseY = ev.pageY;
      }
      //获取当前的x,y坐标
      this.mouseX =
        ev.clientX + document.body.scrollLeft - document.body.clientLeft;
      this.mouseY =
        ev.clientY + document.body.scrollTop - document.body.clientTop;
    },
  },
};
</script>

<style scoped>
@media (min-width: 800px) and (min-height: 600px) {
  #bigscreen {
    display: block;
  }
  #smallscreen {
    display: none;
  }
}
@media (max-width: 800px) {
  #bigscreen {
    display: block;
  }
  #smallscreen {
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
}
.toolbar {
  background-color: rgba(36, 44, 94, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 7vh;
  width:100vw;
}

#table {
  overflow: scroll;
  height: 93vh;
}

h3{
  background-image: linear-gradient(45deg,gold,white);
  display: flex;
  align-items: center;
  justify-content: center;
  width:100vw;
}
</style>