<script>
import { default as configureForm } from "./forms/setResenderData";
// import { default as showData } from "./forms/getResenderData";

import configurationForm from "@/confForm";

export default {
  name: "ResenderConf",
  mixins: [configurationForm],
  components: {
    configureForm
    // showData
  }
};
</script>
