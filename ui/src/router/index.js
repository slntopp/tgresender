import Vue from "vue";
import Router from "vue-router";
import Login from "@/components/Login";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/login"
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
      meta: {
        guest: true
      }
    },
    {
      path: "/",
      name: "Dashboard",
      component: () =>
        import(/* webpackChunkName: "about" */ "../components/Dashboard.vue")
    }
  ]
});
