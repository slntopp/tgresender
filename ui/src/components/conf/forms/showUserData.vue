<template>
  <h3>
    Logged in as <b>{{ conf.name }}</b
    >.
  </h3>
</template>

<script>
export default {
  name: "showData",
  props: {
    conf: {
      required: true
    }
  }
};
</script>
