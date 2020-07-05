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
    @ok="ok"
  >
    <a-form layout="vertical" :form="form">
      <a-form-item label="Phone number">
        <a-input
          v-decorator="[
            'phone_number',
            {
              rules: [
                {
                  required: true,
                  message: 'Please enter the phone number with country code'
                }
              ]
            }
          ]"
        />
      </a-form-item>
      <transition name="slide">
        <a-form-item label="Code" v-if="stage > 0">
          <a-input-number
            v-decorator="[
              'code',
              {
                rules: [
                  {
                    required: true,
                    message: 'You must enter a valid auth code'
                  }
                ]
              }
            ]"
          >
          </a-input-number>
        </a-form-item>
      </transition>
      <transition name="slide">
        <a-form-item label="Code" v-if="stage > 1">
          <a-input-password
            v-decorator="[
              'passwd',
              {
                rules: [
                  {
                    required: true,
                    message: 'You must enter a valid password'
                  }
                ]
              }
            ]"
          >
          </a-input-password>
        </a-form-item>
      </transition>
    </a-form>
  </a-modal>
</template>

<script>
import axios from "axios";

export default {
  props: ["visible", "form_title", "conf"],
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "login_form" });
  },
  data() {
    return {
      stage: 0 // ['send_code', 'enter_code', 'enter_password', 'login']
    };
  },
  computed: {
    ok() {
      return this[["sendCode", "enterCode", "enterPass"][this.stage]];
    }
  },
  watch: {
    conf() {
      this.form.setFieldsValue(this.conf);
    },
    stage() {
      if (this.stage === 3) {
        this.$emit("done", {});
      }
    }
  },
  methods: {
    enterPass() {
      let vm = this;
      vm.form.validateFields((err, values) => {
        if (!err) {
          let payload = new FormData();
          payload.set("passwd", values.passwd);
          axios({
            url: "/enter_pass",
            method: "post",
            data: payload,
            params: {
              passwd: vm.$store.state.password
            }
          }).then(res => {
            vm.stage++;
          });
        }
      });
    },
    enterCode() {
      let vm = this;
      vm.form.validateFields((err, values) => {
        if (!err) {
          let payload = new FormData();
          payload.set("code", values.code);
          axios({
            url: "/enter_code",
            method: "post",
            data: payload,
            params: {
              passwd: vm.$store.state.password
            }
          }).then(res => {
            if (res.data.success) {
              vm.stage += 2;
            } else {
              vm.stage++;
            }
          });
        }
      });
    },
    sendCode() {
      let vm = this;
      vm.form.validateFields((err, values) => {
        if (!err) {
          let payload = new FormData();
          payload.set("phone_number", values.phone_number);
          axios({
            url: "/send_code",
            method: "post",
            data: payload,
            params: {
              passwd: vm.$store.state.password
            }
          }).then(res => {
            vm.stage++;
          });
        }
      });
    },
    submit() {
      let vm = this;
      vm.form.validateFields((err, values) => {
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
              passwd: vm.$store.state.password
            }
          }).then(res => {
            vm.$emit("done", values);
          });
        }
      });
    }
  }
};
</script>
