<template>
  <a-modal
    :visible="visible"
    title="Add rule"
    oktext="Create"
    @ok="submit"
    @cancel="$emit('cancel')"
  >
    <a-form :form="form">
      <a-form-item label="From">
        <a-select v-decorator="['from', {rules: [{required: true}]}]">
          <a-select-option :key="user.id" v-for="user in users">{{ user.title }}</a-select-option>
        </a-select>
      </a-form-item>
      <a-form-item label="To">
        <a-select v-decorator="['to', {rules: [{required: true}]}]">
          <a-select-option :key="user.id" v-for="user in users">{{ user.title }}</a-select-option>
        </a-select>
      </a-form-item>
      <a-form-item label="Copy">
        <a-switch v-decorator="['copy']" defaultChecked>
          <a-icon slot="checkedChildren" type="copy" />
          <a-icon slot="unCheckedChildren" type="close" />
        </a-switch>
      </a-form-item>
    </a-form>
  </a-modal>
</template>

<script>
export default {
  props: {
    visible: { required: true },
    users: { required: true },
    current: { required: false }
  },
  data() {
    return {
      form: this.$form.createForm(this, { name: "createRules" })
    };
  },
  methods: {
    submit() {
      this.form.validateFields((err, vals) => {
        if (!err) {
          this.$emit("create", vals);
        }
      });
    }
  }
};
</script>
