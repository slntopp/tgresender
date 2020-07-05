<template>
  <div id="api_conf">
    <a-button
      v-if="conf.unset"
      type="dashed"
      icon="plus"
      style="font-size: 150px; min-height: 250px; min-width: 100%;"
      @click="configure"
    />
    <configureForm
      :visible="editing"
      :form_title="form_title"
      @cancel="editing = false"
      @done="done"
    />
  </div>
</template>

<script>
import "axios";

import { default as configureForm } from "./forms/setAPIData";

export default {
  name: "APIConf",
  components: {
    configureForm,
  },
  props: {
    conf: {
      required: true,
    },
    form_title: {
      required: true,
    },
  },
  data() {
    return {
      editing: false,
    };
  },
  methods: {
    configure() {
      this.editing = true;
    },
    done(values) {
      this.conf = { unset: false, ...values };
      this.editing = false;
    },
  },
};
</script>
