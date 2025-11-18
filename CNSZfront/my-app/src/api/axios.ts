// src/api/axios.ts
import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 5000,
})

// 요청 인터셉터 (토큰 붙이기 등 하고 싶을 때 사용)
apiClient.interceptors.request.use(
  (config) => {
    // 예: 로컬스토리지에 토큰 있으면 헤더에 붙이기
    // const token = localStorage.getItem('token')
    // if (token) {
    //   config.headers.Authorization = `Bearer ${token}`
    // }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 응답 인터셉터 
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

export default apiClient