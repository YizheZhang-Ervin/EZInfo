import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter)

import Home  from './components/home.vue';
import Main from './components/mainpart.vue';

const routes=[
    {path:'',component:Home},
    {path:'/main',component:Main},
]


const router=new VueRouter({
    routes
});

export default router;