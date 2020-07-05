import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    password: "",
    validated: false
  },
  mutations: {
    validate_password(state, pass) {
      state.password = pass;
      state.validated = true;
    }
  },
  actions: {},
  modules: {}
});
