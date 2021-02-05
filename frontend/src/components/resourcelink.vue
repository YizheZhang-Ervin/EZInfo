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
          date: "2019-09-09",
          name: "python",
          content: "python.org",
        },
        {
          date: "2020-02-02",
          name: "Angular",
          content: "angular.rog",
        },
        {
          date: "2021-01-01",
          name: "Vue",
          content: "vue.org",
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