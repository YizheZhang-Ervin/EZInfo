import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter)

import Index  from './components/index.vue';
import Welcome from './components/welcome.vue';
import Manager from './components/manager.vue';

const routes=[
    
    {path:'/home',component:Index},
    {path:"/manager",component:Manager},
    {path:'*',component:Welcome},
]


const router=new VueRouter({
    mode: 'history',
    routes
});

export default router;