<template>
  <a-modal
    :visible="visible"
    :title="form_title"
    okText="Submit"
    :ok-button-props="{ props: { loading: loading } }"
    @cancel="
      () => {
        $emit('cancel');
      }
    "
    @ok="submit"
  >
    <a-form layout="vertical" :form="form">
      <a-form-item label="API ID">
        <a-input
          v-decorator="[
            'api_id',
            {
              rules: [
                {
                  required: true,
                  message: 'Please enter the API ID'
                }
              ]
            }
          ]"
        />
      </a-form-item>
      <a-form-item label="API Hash">
        <a-input
          v-decorator="[
            'api_hash',
            {
              rules: [{ required: true, message: 'Please enter the API Hash' }]
            }
          ]"
        />
      </a-form-item>
    </a-form>
  </a-modal>
</template>

<script>
import axios from "axios";

export default {
  props: ["visible", "form_title", "conf"],
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "configure_form" });
  },
  data() {
    return {
      loading: false
    };
  },
  mounted() {
    this.checkConf();
  },
  methods: {
    checkConf() {
      this.form.setFieldsValue(this.conf);
      if (this.conf.api_id && this.conf.api_hash) {
        this.$emit("done", this.conf);
      }
    },
    submit() {
      let vm = this;
      vm.form.validateFields((err, values) => {
        if (!err) {
          vm.loading = true;
          let apiClientData = new FormData();
          for (let [k, v] of Object.entries(values)) {
            apiClientData.set(k, v);
          }

          axios({
            url: "/init_client",
            method: "post",
            data: apiClientData,
            params: {
              passwd: vm.$store.state.password
            }
          })
            .then(res => {
              console.log("init_client", res);
              vm.$emit("done", values);
              vm.$message.success("API conf is all set");
            })
            .catch(() => {})
            .then(() => {
              vm.loading = false;
            });
        }
      });
    }
  }
};
</script>
