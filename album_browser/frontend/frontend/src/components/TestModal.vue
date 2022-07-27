<template>      
  <b-modal :id="modalId">{{albumName}}</b-modal>
</template>

<script>

  export default {
    props: {
      modalId: { required: true, type: String },
      albumName: { required: true, type: String }
    },
    data() {
      return {
    };
  }
  };
</script>
