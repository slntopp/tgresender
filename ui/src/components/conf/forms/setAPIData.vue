<template>
  <a-modal
    :visible="visible"
    :title="form_title"
    okText="Submit"
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
              required: true,
              message: 'Please enter the API Hash'
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
  props: ["visible", "form_title"],
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "configure_form" });
  },
  methods: {
    submit() {
      this.form.validateFields((err, values) => {
        if (!err) {
          let apiClientData = new FormData();
          for (let [k, v] of Object.entries(values)) {
            apiClientData.set(k, v);
          }

          axios({
            url: "/init_client",
            method: "post",
            data: apiClientData,
            params: {
              passwd: this.$store.state.password
            }
          }).then(res => {
            this.$emit("done", values);
          });
        }
      });
    }
  }
};
</script>
