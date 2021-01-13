import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import Register from "../components/Register";
import Index from "../components/Index"
import AddEmp from "../components/AddEmp";
import UpdateEmp from "../components/UpdateEmp";
Vue.use(Router)

export default new Router({
  routes: [
    {path: "/login", component: Login},
    {path: "/register", component: Register},
    {path: "/index", component: Index},
    {path: "/add", component: AddEmp},
    {path: "/update", component: UpdateEmp},
    {path: "/update/:id", component: UpdateEmp},
    {path: "/", redirect: "/login"},
    {path: "/*", redirect: "/login"},
  ]
})
