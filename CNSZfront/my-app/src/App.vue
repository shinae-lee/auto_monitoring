<script setup lang="ts">
  import Header from './components/header.vue'
  import Footer from './components/footer.vue'
</script>

<template>
  <Header />
 
  <main>
    <RouterView />
  </main>

  <Footer />
</template>

<style scoped></style>
