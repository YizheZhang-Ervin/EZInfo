<template>
  <section class="whole">
    <header>
      <i class="ezlogo"></i>
      <p>Ervin Zhang</p>
    </header>
    <main>
        <p class="name">Hi, I am Yizhe Zhang</p>
        <p class="intro">A Front End &amp; Full Stack Developer</p>
        <router-link to="/home"><el-button plain class="btn" >Take A Look</el-button></router-link>
    </main>
    <footer>
        <p>Yizhe(Ervin) Zhang |&nbsp;
            <a target="_blank" rel="noopener noreferrer" 
            href="mailto:zhang.yizhe@northeastern.edu?subject=Please%20type%20in%20the%20subject">
            zhang.yizhe@northeastern.edu
            </a>
        </p>
    </footer>
  </section>
</template>

<script>
export default {
  name: "Welcome",
  data() {
    return {};
  },
  mounted() {},
  methods: {},
};
</script>

<style scoped>
.whole {
  height: 100vh;
  widows: 100vw;
  background-image: url("../assets/static/img/myself/self_cover.jpg");
  background-size: cover;
}

header {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  position:fixed;
  top:1%;
  padding-left:15px;
  color: beige;
  height: 5vh;
  width: 100vw;
}

@media (min-width:500px){
  header{
    font-size: 2em;
  }
  main {
    display: flex;
    align-items:flex-end;
    justify-content: center;
    flex-direction: column;
    height: 90vh;
    width: 85vw;
    color: beige;
  }
  .name{
    font-size: 2.5em;
    line-height: 50px;
  }
  .intro{
    font-size: 1.1em;
    line-height: 50px;
  }
  footer{
    font-size: 1.1em;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
@media (max-width:500px){
  header{
    font-size: 1em;
  }
  main {
    display: flex;
    align-items:center;
    justify-content: center;
    flex-direction: column;
    height: 90vh;
    width: 100vw;
    color: beige;
  }
  .name{
    font-size: 1.5em;
    line-height: 50px;
  }
  .intro{
    font-size: 0.7em;
    line-height: 50px;
  }
  footer{
    font-size: 0.7em;
    text-align: center;
  }
}

footer {
  position:fixed;
  bottom:1%;
  color: beige;
  height: 5vh;
  width: 100vw;
}

a {
  text-decoration: none;
  color: beige;
}

.btn{
    background-color: black;
    border: none;
    font-size: 1.1em;
    color: beige;
}

.el-button.is-plain:focus, .el-button.is-plain:hover{
    background-color: black;
}
</style>