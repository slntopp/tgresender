<script>
import { default as configureForm } from "./forms/getUserData";
import { default as showData } from "./forms/showUserData";

import configurationForm from "@/confForm";

export default {
  name: "UserConf",
  mixins: [configurationForm],
  components: {
    configureForm,
    showData
  }
};
</script>
