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
          name: "Free Images 1",
          content: "https://stockup.sitebuilderreport.com/",
        },
        {
          date: "2021-02-05",
          name: "Free Images 2",
          content: "https://unsplash.com",
        },
        {
          date: "2021-02-05",
          name: "Free Images 3",
          content: "https://pixabay.com",
        },
        {
          date: "2021-02-05",
          name: "Free Images 4",
          content: "https://stocksnap.io",
        },
        {
          date: "2021-02-05",
          name: "Free Images 5",
          content: "https://visualhunt.com",
        },
        {
          date: "2021-02-05",
          name: "Free SVG 1",
          content: "https://icon-icons.com/zh/",
        },
        {
          date: "2021-02-05",
          name: "Free SVG 2",
          content: "https://www.flaticon.com/",
        },
        {
          date: "2021-02-05",
          name: "Free SVG 3",
          content: "https://www.freepik.com",
        },
        {
          date: "2021-02-05",
          name: "Free SVG 4",
          content: "https://www.iconfinder.com",
        },
        {
          date: "2021-02-05",
          name: "Free SVG 5",
          content: "https://www.iconfont.cn",
        },
        {
          date: "2021-02-05",
          name: "Free E-books",
          content: "https://b-ok.cc/",
        },
        {
          date: "2021-02-05",
          name: "Free Fonts",
          content: "https://fontawesome.com",
        },
        {
          date: "2021-02-05",
          name: "Free Palette 1",
          content: "https://flatuicolors.com/palette/cn",
        },
        {
          date: "2021-02-05",
          name: "Free Palette 2",
          content: "https://www.divcss5.com/peise/",
        },
        {
          date: "2021-02-05",
          name: "Free HTML Templates 1",
          content: "https://templated.co/",
        },
        {
          date: "2021-02-05",
          name: "Free HTML Templates 2",
          content: "https://www.free-css.com/free-css-templates?start=48",
        },
        {
          date: "2021-02-05",
          name: "Free HTML Templates 3",
          content: "https://www.os-templates.com",
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