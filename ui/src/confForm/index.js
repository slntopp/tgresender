const configurationForm = {
  props: {
    conf: {
      required: true
    },
    form_title: {
      required: true
    },
    disabled: {
      default: false
    }
  },
  data() {
    return {
      editing: false
    };
  },
  methods: {
    configure() {
      this.editing = true;
    },
    done(values) {
      console.log("Done", values);
      this.conf = { unset: false, ...values };
      this.editing = false;
      this.$emit("updated", this.conf);
    }
  },
  template: `
    <div>
      <a-card :title="form_title" style="min-height: 300px;" :loading="disabled">
        <a-button
          slot="extra"
          type="link"
          @click="configure"
        >Edit</a-button
        >
        <a-button
          v-if="conf.unset"
          type="dashed"
          icon="plus"
          style="font-size: 150px; min-height: 250px; min-width: 100%;"
          @click="configure"
        />
        <showData :conf="conf" v-else />
        <configureForm
          :conf="conf"
          :visible="editing"
          :form_title="form_title"
          @cancel="editing = false"
          @done="done"
        />
      </a-card>
    </div>`
};

export default configurationForm;
