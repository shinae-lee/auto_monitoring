<template>
  <header class="header">
    <div class="logo">
      🍋 My Blog 
    </div>
    <nav class="nav">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
/* 헤더 스타일 */
.header {
  background-color: #fffacd; /* 레몬색 */
  color: #333;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
}

/* 로고 스타일 */
.logo {
  font-size: 1.5rem;
  font-weight: bold;
  display: flex;
  align-items: center;
}

/* 네비게이션 스타일 */
.nav ul {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin: 0;
  padding: 0;
}

.nav ul li {
  font-size: 1rem;
}

.nav ul li a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  transition: color 0.3s ease;
}

.nav ul li a:hover {
  color: #ffcc00; /* 레몬색 강조 */
}
</style>