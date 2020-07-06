<template>
  <a-drawer
    placement="bottom"
    :title="form_title"
    :visible="visible"
    @close="visible = false"
    height="1000"
  >
    <a-row>
      <a-table bordered :data-source="conf.data" :columns="columns"></a-table>
    </a-row>
  </a-drawer>
</template>

<script>
// import axios from "axios";
export default {
  name: "setResenderData",
  props: ["visible", "form_title", "conf"],
  data() {
    return {
      columns: [
        {
          title: "From",
          dataIndex: "from",
          key: "from"
        },
        {
          title: "To",
          dataIndex: "to",
          key: "to"
        },
        {
          title: "Copy",
          dataIndex: "copy",
          key: "copy"
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
      { title: "Fucking shit", id: -23423424423423 }
    ];
  }
};
</script>
