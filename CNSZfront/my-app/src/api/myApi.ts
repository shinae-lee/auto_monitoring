import apiClient from "./axios"


export interface RootMessageResponse {
    title: string;
    description: string;
  }
  

export async function fetchRootMessage(): Promise<RootMessageResponse> {
  const res = await apiClient.get<RootMessageResponse>('/')
  console.log(res.data);
  return res.data
}