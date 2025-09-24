import {createRouter, createWebHistory} from 'vue-router'

import Home from '../views/Home.vue'
import Directors from "../views/Directors.vue";
import Actors from '../views/Actors.vue'
import Genres from "../views/Genres.vue";

const routes = [
    {path: '/', redirect: '/home'},
    {path: '/home', name: 'Home', component: Home},
    {path: '/directors', name: 'Directors', component: Directors},
    {path: '/actors', name: 'Actors', component: Actors},
    {path: '/genres', name: 'Genres', component: Genres},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router