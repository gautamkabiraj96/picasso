import { IStorageService } from './IStorageService'

export class CookieStorageService implements IStorageService {
  get<T>(key: string): T | null {
    if (typeof document === 'undefined') return null
    const nameEQ = `${key}=`
    const cookies = document.cookie.split(';')
    for (let cookie of cookies) {
      cookie = cookie.trim()
      if (cookie.indexOf(nameEQ) === 0) {
        const cookieValue = cookie.substring(nameEQ.length)
        try {
          return JSON.parse(decodeURIComponent(cookieValue)) as T
        } catch (error) {
          console.error(`Error parsing cookie "${key}":`, error)
          return null
        }
      }
    }
    return null
  }

  set<T>(key: string, value: T): void {
    if (typeof document === 'undefined') return
    try {
      const stringValue = encodeURIComponent(JSON.stringify(value))
      document.cookie = `${key}=${stringValue}; path=/`
    } catch (error) {
      console.error(`Error setting cookie "${key}":`, error)
    }
  }

  remove(key: string): void {
    if (typeof document === 'undefined') return
    document.cookie = `${key}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/`
  }
}
