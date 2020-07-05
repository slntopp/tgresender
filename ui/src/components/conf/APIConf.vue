<script>
import { default as configureForm } from "./forms/setAPIData";
import { default as showData } from "./forms/showAPIData";

import configurationForm from "@/confForm";

export default {
  name: "APIConf",
  mixins: [configurationForm],
  components: {
    configureForm,
    showData,
  },
};
</script>
