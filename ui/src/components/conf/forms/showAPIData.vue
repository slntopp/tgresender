<template>
  <div id="showAPIData">
    <a-form layout="vertical" :form="form">
      <a-form-item label="API ID">
        <a-input v-decorator="['api_id']" readonly />
      </a-form-item>
      <a-form-item label="API Hash">
        <a-input v-decorator="['api_hash']" readonly />
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
export default {
  name: "showAPIData",
  props: {
    conf: {
      required: true
    }
  },
  data() {
    return {
      form: this.$form.createForm(this, { name: "show_data" })
    };
  },
  watch: {
    conf() {
      this.form.setFieldsValue(this.conf);
    }
  },
  mounted() {
    this.form.setFieldsValue(this.conf);
  }
};
</script>
