<template>
  <section>
    <el-table :data="linkData" stripe height="93vh">
      <el-table-column prop="date" label="Date" width="180"> </el-table-column>
      <el-table-column prop="name" label="Name" width="180"> </el-table-column>
      <el-table-column prop="content" label="Content"> </el-table-column>
    </el-table>
  </section>
</template>

<script>
export default {
  name: "ResourceLink",
  data() {
    return {
      linkData: [
        {
          date: "2021-02-05",
          name: "Free Images",
          content: "https://stockup.sitebuilderreport.com/",
        },
        {
          date: "2021-02-05",
          name: "Free SVG",
          content: "https://www.flaticon.com/",
        },
        {
          date: "2021-02-05",
          name: "Free E-books",
          content: "https://b-ok.cc/",
        },
        {
          date: "2021-02-05",
          name: "Palette",
          content: "https://flatuicolors.com/palette/cn",
        },
        {
          date: "2021-02-05",
          name: "Free Icons",
          content: "https://www.iconfont.cn/search/index?searchType=icon&q=school",
        },
        {
          date: "2021-02-05",
          name: "Free HTML Templates",
          content: "https://templated.co/",
        },
        {
          date: "2021-02-05",
          name: "Transform Icons",
          content: "http://www.bitbug.net/",
        },
      ],
    };
  },
  mounted() {},
  methods: {},
};
</script>

<style scoped>
</style>