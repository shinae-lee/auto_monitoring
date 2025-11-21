<template>
  <div class="home">
    <main class="feed">
      <div 
        v-for="(post, index) in posts" 
        :key="index" 
        class="post"
      >
        <div class="post-content">
          <h2 class="post-title">{{ post.title }}</h2>
          <p class="post-description">{{ post.description }}</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue'
import {fetchRootMessage} from '@/api/myApi'

type Post = {
  title: string;
  description: string;
}

const posts = ref<Post[]>([])

onMounted(async () => {
  try {
    const data = await fetchRootMessage()
    posts.value.push({
      title: data.title,
      description: data.description
    })

    console.log("Fetched root message:", data)
  } catch (error) {
    console.error("Error fetching root message:", error)
  }
})

</script>

<style scoped>
/* 전체 페이지 스타일 */
.home {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f9;
}

/* 피드 스타일 */
.feed {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2rem auto;
  max-width: 800px;
}

/* 게시물 스타일 */
.post {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 1rem 0;
  overflow: hidden;
  width: 100%;
}

.post-image {
  width: 100%;
  height: auto;
}

.post-content {
  padding: 1rem;
}

.post-title {
  margin: 0.5rem 0;
  color: #333;
}

.post-description {
  color: #555;
}
</style>