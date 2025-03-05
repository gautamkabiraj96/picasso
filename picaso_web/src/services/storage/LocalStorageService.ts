import { IStorageService } from './IStorageService'

export class LocalStorageService implements IStorageService {
  get<T>(key: string): T | null {
    if (typeof window === 'undefined') return null
    const item = localStorage.getItem(key)
    try {
      return item ? (JSON.parse(item) as T) : null
    } catch (error) {
      console.error(`Error parsing localStorage key "${key}":`, error)
      return null
    }
  }

  set<T>(key: string, value: T): void {
    if (typeof window !== 'undefined') {
      try {
        localStorage.setItem(key, JSON.stringify(value))
      } catch (error) {
        console.error(`Error setting localStorage key "${key}":`, error)
      }
    }
  }

  remove(key: string): void {
    if (typeof window !== 'undefined') {
      localStorage.removeItem(key)
    }
  }
}
