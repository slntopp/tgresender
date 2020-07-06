<template>
  <a-row type="flex" justify="center" align="middle" id="login">
    <a-col :span="12">
      <a-row type="flex" justify="start">
        <h1>Login to TelegramResender Panel</h1>
      </a-row>
      <a-row type="flex" justify="space-around" :gutter="5">
        <a-col :span="16">
          <a-input-password
            v-model="password"
            :disabled="validating"
            @pressEnter="submit"
          />
        </a-col>
        <a-col :span="8">
          <a-button
            type="primary"
            :disabled="password.length == 0"
            @click="submit"
            :loading="validating"
            >Submit</a-button
          >
        </a-col>
      </a-row>
    </a-col>
  </a-row>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      password: "",
      validating: false,
    };
  },
  methods: {
    submit() {
      let vm = this;
      vm.validating = true;
      axios({
        url: "/login/",
        method: "post",
        params: {
          passwd: vm.password,
        },
      })
        .then((res) => {
          console.log("Logged in", res.data);
          if (res.data.result) {
            vm.$store.commit("validate_password", vm.password);
            vm.$router.push({ path: "/panel" });
          } else {
            vm.$notification.error({
              message: "Password wan't validated",
              description: "Check your password and try again.",
            });
          }
        })
        .catch(() => {})
        .then(() => {
          vm.validating = false;
        });
    },
  },
};
</script>

<style>
#login {
  width: 80%;
  min-height: 50%;
  padding: 20% 10%;
}
</style>
