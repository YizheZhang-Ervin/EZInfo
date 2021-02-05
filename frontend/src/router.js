import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter)

import Index  from './components/index.vue';
import Welcome from './components/welcome.vue';

const routes=[
    {path:'',component:Welcome},
    {path:'/home',component:Index},
]


const router=new VueRouter({
    routes
});

export default router;