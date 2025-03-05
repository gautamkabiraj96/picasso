import { InternalAxiosRequestConfig, CancelTokenSource } from 'axios'

export interface ApiRequestConfig extends InternalAxiosRequestConfig<any> {
  retry?: number
  cancellable?: boolean
  cancelTokenSource?: CancelTokenSource
  token?: string
}

export interface INetworkService {
  get<T>(url: string, config?: ApiRequestConfig): Promise<T>
  post<T>(url: string, data?: any, config?: ApiRequestConfig): Promise<T>
  put<T>(url: string, data?: any, config?: ApiRequestConfig): Promise<T>
  patch<T>(url: string, data?: any, config?: ApiRequestConfig): Promise<T>
  delete<T>(url: string, config?: ApiRequestConfig): Promise<T>
}
