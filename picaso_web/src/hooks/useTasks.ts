import { useQuery } from '@tanstack/react-query'
import { ApiService } from './../services/network/ApiService'

const api = new ApiService()

export function useTasks() {
 return useQuery({
  queryKey: ['tasks'],
  queryFn: () => api.get('/tasks/'),
 })
}