<template>
  <div id="panel">
    <a-layout>
      <a-layout-header>
        <h2 style="color: white;">Telegram Resender Panel</h2>
      </a-layout-header>
      <a-layout-content>
        <a-row type="flex" justify="space-between" id="conf_container">
          <a-col :span="7">
            <APIConf
              :conf="api_conf"
              form_title="Configure Telegram API keys"
              :disabled="false"
              @updated="
                (conf) => {
                  api_conf = conf;
                }
              "
            />
          </a-col>
          <a-col :span="7">
            <UserConf
              :conf="user_conf"
              form_title="Login to Telegram"
              :disabled="api_conf.unset"
              @updated="
                (conf) => {
                  user_conf = conf;
                }
              "
            />
          </a-col>
          <a-col :span="7">
            <ResenderConf
              :conf="resender_conf"
              form_title="Configure Resender"
              :disabled="false && (api_conf.unset || user_conf.unset)"
              @updated="
                (conf) => {
                  resender_conf = conf;
                }
              "
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
import ResenderConf from "@/components/conf/ResenderConf";

export default {
  name: "Panel",
  components: {
    APIConf,
    UserConf,
    ResenderConf
  },
  data() {
    return {
      api_conf: {
        unset: true
      },
      user_conf: {
        unset: true
      },
      resender_conf: {
        unset: true,
        data: []
      }
    };
  }
};
</script>

<style>
#panel {
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
