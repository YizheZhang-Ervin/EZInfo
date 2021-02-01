import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter)

import Index  from './components/index.vue';

const routes=[
    {path:'',component:Index},
]


const router=new VueRouter({
    routes
});

export default router;