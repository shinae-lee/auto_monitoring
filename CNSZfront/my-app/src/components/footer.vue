<template>
  <footer class="footer">
    <div class="footer-content">
      <img src="/static/lg-cns-logo.png" alt="LG CNS Logo" class="footer-logo" />
      <p class="footer-text">아키텍처 운영팀</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
/* 푸터 스타일 */
.footer {
  background-color: #f8f9fa; /* 밝은 회색 */
  color: #333;
  text-align: center;
  padding: 1rem 0;
  border-top: 1px solid #e0e0e0;
  font-family: 'Arial', sans-serif;
}

.footer-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.footer-logo {
  width: 120px; /* 로고 크기 */
  height: auto;
}

.footer-text {
  font-size: 1rem;
  font-weight: bold;
  margin: 0;
}
</style>