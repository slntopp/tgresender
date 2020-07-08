<template>
  <a-drawer
    placement="bottom"
    :title="form_title"
    :visible="visible"
    @close="visible = false"
    height="1000"
  >
    <a-row>
      <a-table bordered :data-source="conf.data" :columns="columns">
        <a-tooltip slot="from" slot-scope="id">
          <template slot="title">
            Click
            <a @click="copy(id)">here</a> or on the cell to copy the username or id
          </template>
          <a-button type="link" @click="copy(id)">{{ users.filter(u => u.id == id)[0].title }}</a-button>
        </a-tooltip>
        <a-tooltip slot="to" slot-scope="id">
          <template slot="title">
            Click
            <a @click="copy(id)">here</a> or on the cell to copy the username or id
          </template>
          <a-button type="link" @click="copy(id)">{{ users.filter(u => u.id == id)[0].title }}</a-button>
        </a-tooltip>
        <a-switch slot="copy" slot-scope="[copy, i]" :checked="copy">
          {{ i }}
          <a-icon slot="checkedChildren" type="copy" />
          <a-icon slot="unCheckedChildren" type="close" />
        </a-switch>
      </a-table>
      <a-row type="flex" justify="center" style="margin-top: 20px">
        <a-col :span="8">
          <a-button
            type="primary"
            icon="plus"
            style="background-color: #00e400; border-color: #00e400; width: 100%"
            @click="addRule"
          >Add rule</a-button>
        </a-col>
      </a-row>

      <createRuleModal
        :visible="create_rule_visible"
        :users="users"
        @cancel="create_rule_visible = false"
        @create="res => {conf.data.push(res); create_rule_visible = false}"
      />
    </a-row>
  </a-drawer>
</template>

<script>
import createRuleModal from "./setResenderData/createRuleModal";

// import axios from "axios";
export default {
  name: "setResenderData",
  props: ["visible", "form_title", "conf"],
  components: {
    createRuleModal
  },
  data() {
    return {
      users: [],
      create_rule_visible: false,
      columns: [
        {
          title: "From",
          dataIndex: "from",
          key: "from",
          scopedSlots: { customRender: "from" }
        },
        {
          title: "To",
          dataIndex: "to",
          key: "to",
          scopedSlots: { customRender: "to" }
        },
        {
          title: "Copy",
          dataIndex: "copy",
          key: "copy",
          scopedSlots: { customRender: "copy" }
        }
      ]
    };
  },
  async mounted() {
    let vm = this;
    // vm.users = (
    //   await axios({
    //     url: "/get_users/",
    //     method: "get",
    //     params: { passwd: vm.$store.state.password }
    //   })
    // ).data;
    vm.users = [
      { title: "Mikitko Iwanowski", id: "slnt_opp" },
      { title: "Fucking shit", id: "-23423424423423" }
    ];
  },
  methods: {
    copy(id) {
      const el = document.createElement("textarea");
      el.value = id;
      document.body.appendChild(el);
      el.select();
      document.execCommand("copy");
      document.body.removeChild(el);
    },
    addRule() {
      this.create_rule_visible = true;
    }
  }
};
</script>
