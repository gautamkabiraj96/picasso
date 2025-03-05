import axios, {
  AxiosError,
  InternalAxiosRequestConfig,
  CancelTokenSource,
} from 'axios'
import { ApiRequestConfig } from './INetworkService'

const AxiosInstance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || '/api',
  timeout: 10000,
})

AxiosInstance.interceptors.request.use(
  (config: InternalAxiosRequestConfig<any>) => {
    const cfg = config as ApiRequestConfig

    const token =
      cfg.token ||
      (typeof window !== 'undefined' ? localStorage.getItem('token') : null)
    if (token) {
      cfg.headers = cfg.headers || {}
      cfg.headers['Authorization'] = `Bearer ${token}`
    }

    if (cfg.cancellable && !cfg.cancelToken) {
      const source: CancelTokenSource = axios.CancelToken.source()
      cfg.cancelToken = source.token
      cfg.cancelTokenSource = source
    }

    return cfg
  },
  (error) => Promise.reject(error)
)

AxiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (axios.isAxiosError(error)) {
      const axiosError = error as AxiosError<any>

      if (axios.isCancel(axiosError)) {
        return Promise.reject({ canceled: true, message: 'Request canceled' })
      }

      if (!axiosError['response']) {
        return Promise.reject({
          networkError: true,
          message: 'Network error',
        })
      }

      const config = axiosError['config'] as ApiRequestConfig
      if (config && config.retry !== undefined && config.retry > 0) {
        config.retry--
        return new Promise((resolve) => {
          setTimeout(() => {
            resolve(AxiosInstance(config))
          }, 1000)
        })
      }
    }

    return Promise.reject(error)
  }
)

export default AxiosInstance
