<template>
  <div id="dashboard">
    <a-layout>
      <a-layout-header>
        <h2 style="color: white;">Dashboard</h2>
      </a-layout-header>
      <a-layout-content>
        <a-row type="flex" justify="space-between" id="conf_container">
          <a-col :span="7">
            <a-card title="Telegram API Conf">
              <APIConf
                :conf="api_conf"
                form_title="Configure Telegram API keys"
              />
            </a-card>
          </a-col>
          <a-col :span="7">
            <a-card title="Set up user/bot" :loading="api_conf.unset">
              <APIConf
                :conf="user_conf"
                form_title="Login to Telegram as user or bot"
              />
            </a-card>
          </a-col>
          <a-col :span="7">
            <a-card
              title="Configure TgResender"
              :loading="api_conf.unset || user_conf.unset"
            >
              <APIConf :conf="resender_conf" form_title="Configure Resender" />
            </a-card>
          </a-col>
        </a-row>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script>
import APIConf from "@/components/conf/APIConf";

export default {
  name: "Dashboard",
  components: {
    APIConf,
  },
  data() {
    return {
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
a-card {
  min-height: 300px;
}
</style>
