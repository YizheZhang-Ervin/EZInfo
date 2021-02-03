<template>
<div id="groupComponent">
    <!-- 列表 -->
    <div v-show="listShow">
    <div>
        <el-card v-for="m in members" shadow="hover" :key=m.name >
            <div  @click="changeListDetailShow(m)" class="flex-row">
                <el-image style="height:100px;width:200px;" :src="m.img" fit="cover">
                </el-image>
                <div>{{m.name}}</div>
                <div>{{m.location}}</div>
                <div>{{m.pro}}</div>
            </div>
        </el-card>
    </div>
    </div>
    <!-- 单人详细 -->
    <div v-show="detailShow" style="height:86vh">
    <el-button circle icon="el-icon-arrow-left" @click="changeListDetailShow('back')"></el-button>
    <section class="outer">
        <!-- 左边 -->
        <section class="leftpart">
            <el-card :body-style="{padding:'0px'}">
                <div>
                    <el-image :src="memberDetail.img" fit="contain" style="height:40vh;">
                    </el-image>
                </div>
                <div>
                    <div  class="flex-col2">
                    <el-button type="text" icon="el-icon-message" class="email">Email: {{memberDetail.mail}}
                    </el-button>
                    <el-button type="text" icon="el-icon-user" class="contact">Contact: <span
                            v-html="memberDetail.contact"></span>
                    </el-button>
                    <el-divider></el-divider>
                    </div>
                    <div class="flex-row">
                        <a :href="memberDetail.linkedin">
                            <el-button circle>ln</el-button>
                        </a>
                        <el-divider direction="vertical"></el-divider>
                        <a href="javascript:window.print()">
                            <el-button icon="el-icon-printer" circle></el-button>
                        </a>
                    </div>
                </div>
            </el-card>
        </section>
        <!-- 右边 -->
        <section class="rightpart">
            <!-- 名字 -->
            <div class="flex-row2">
                <h1>{{memberDetail.name}}
                    <span style="font-size:medium">{{memberDetail.title}}</span>
                </h1>
                <el-image :src="logo" fit="contain">
                </el-image>
            </div>
            <!-- Role -->
            <div class="flex-col">
                <el-divider content-position="left">Role</el-divider>
                <p>{{memberDetail.exp1}}</p>
            </div>
            <!-- Projects -->
            <div class="flex-col">
                <el-divider content-position="left">Projects</el-divider>
                <div v-html="memberDetail.exp2"></div>
            </div>
            <!-- Skills -->
            <div class="flex-col">
                <el-divider content-position="left">Skills</el-divider>
                <p>{{memberDetail.exp3}}</p>
            </div>
        </section>
    </section>
    </div>
</div>
</template>

<script>
export default {
    name: "EGGroup",
    data: function () {
        return {
            listShow: true,
            detailShow: false,
            logo:require("../assets/img/favicon.svg"),
            memberDetail: {},
            members: [{
                index: '1',
                name: "Yizhe Zhang",
                location: "Boston",
                pro: "Developer",
                img: require("../assets/img/ervin.png"),
                mail: "zhang.yizhe@northeastern.edu",
                contact: "<a href='https://ervinzhang.pythonanywhere.com/' target='_new'>ervinzhang</a>",
                linkedin: "https://www.linkedin.com/in/yizhe-zhang/",
                title: "Developer",
                exp1: "FinTech",
                exp2: "<p>FISH Group\
                </p><p>YeStock</p>",
                exp3: "Python, JavaScript"
            }]
        }
    },
    methods: {
        changeListDetailShow: function (member) {
            if (member == "back") {
                this.listShow = true;
                this.detailShow = false;
            } else {
                this.listShow = false;
                this.memberDetail = member;
                this.detailShow = true;
            }
        }
    },
}
</script>

<style scoped>
h1{
    font-size: xx-large;
}
.el-divider__text{
    background-color: white!important;
    color:black!important;
    font-weight: bold!important;
    font-size: larger;
}

.flex-row{
    display: flex;
    align-items: center;
    justify-content: space-around;
}

.flex-row2{
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.flex-col{
    display: flex;
    align-items: flex-start;
    justify-content: center;
    flex-direction: column;
    width:50vw;
}

.flex-col2{
    display: flex;
    align-items: flex-start;
    justify-content: center;
    flex-direction: column;
    width:30vw;
}

.email,.contact{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: inline-block;
    text-indent: 15px;
}

.outer{
    display: flex;
    align-self: center;
    justify-content: space-around;
    width: 100vw;
    height:86vh;
}
.leftpart{
    display: flex;
    align-self: flex-start;
    justify-content: center;
    width: 30vw;
    height:66vh;
}
.rightpart{
    display: flex;
    align-self:center;
    justify-content: flex-start;
    flex-direction: column;
    width: 60vw;
    height:86vh;
}

</style>