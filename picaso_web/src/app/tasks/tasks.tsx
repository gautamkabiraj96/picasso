import { useTasks } from '@/hooks/useTasks'

export default function TaskList() {
  const { data: tasks, isLoading, error } = useTasks()

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error loading tasks</div>

  return (
    <ul>
      {(tasks as any).map((task: any) => (
        <li key={task.id}>{task.title}</li>
      ))}
    </ul>
  )
}
