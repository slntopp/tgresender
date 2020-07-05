<template>
  <div id="dashboard">
    <a-layout>
      <a-layout-header>
        <h2 style="color: white;">Telegram Resender Dashboard</h2>
      </a-layout-header>
      <a-layout-content>
        <div class="spin-container" v-if="loading">
          <a-spin :spinning="loading" size="large" />
        </div>
        <a-row type="flex" justify="space-between" id="conf_container" v-else>
          <a-col :span="7">
            <APIConf
              :conf="api_conf"
              form_title="Configure Telegram API keys"
              :disabled="false"
            />
          </a-col>
          <a-col :span="7">
            <UserConf
              :conf="user_conf"
              form_title="Login to Telegram"
              :disabled="api_conf.unset"
            />
          </a-col>
          <a-col :span="7">
            <APIConf
              :conf="resender_conf"
              form_title="Configure Resender"
              :disabled="api_conf.unset || user_conf.unset"
            />
          </a-col>
        </a-row>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
import APIConf from "@/components/conf/APIConf";
import UserConf from "@/components/conf/UserConf";

import axios from "axios";

export default {
  name: "Dashboard",
  components: {
    APIConf,
    UserConf,
  },
  data() {
    return {
      loading: true,
      api_conf: {
        unset: true,
      },
      user_conf: {
        unset: true,
      },
      resender_conf: {
        unset: true,
      },
    };
  },
  mounted() {
    let vm = this;
    console.log("mounted, getting conf");
    axios({
      method: "get",
      url: "/get_conf",
      params: {
        passwd: vm.$store.state.password,
      },
    })
      .then((res) => {
        let conf = res.data;
        console.log(conf);
        if (conf.api_id && conf.api_hash) {
          vm.api_conf = {
            unset: false,
            api_id: conf.api_id,
            api_hash: conf.api_hash,
          };
        }
      })
      .catch(() => {})
      .then(() => {
        vm.loading = false;
      });
  },
};
</script>

<style>
#dashboard {
  width: 100%;
  height: 100%;
}
#conf_container {
  padding: 20px 10%;
}
.spin-container {
  text-align: center;
  min-width: 600px;
  min-height: 600px;
  max-height: 300px;
  width: 60%;
  height: 20%;
  padding: 50px 30px;
}
</style>
