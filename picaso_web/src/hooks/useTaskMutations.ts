import { useMutation, useQueryClient } from '@tanstack/react-query'
import { ApiService } from '@/services/network/ApiService'

const api = new ApiService()

export function useCreateTask() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (newTask: { title: string }) => api.post('/tasks/', newTask),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] })
    },
  })
}

export function useUpdateTask() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: number; data: any }) =>
      api.patch(`/tasks/${id}/`, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] })
    },
  })
}

export function useDeleteTask() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (id: number) => api.delete(`/tasks/${id}/`),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] })
    },
  })
}

// Usage

/*
import { useCreateTask } from '@/hooks/useTaskMutations'

function CreateTaskForm() {
  const createTask = useCreateTask()

  const handleSubmit = () => {
    createTask.mutate({ title: 'New Task' })
  }

  return <button onClick={handleSubmit}>Add Task</button>
}
*/
