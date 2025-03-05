import AxiosInstance from './AxiosInstance';
import { INetworkService, ApiRequestConfig } from './INetworkService';

export class ApiService implements INetworkService {
 async get<T>(url: string, config?: ApiRequestConfig): Promise<T> {
  const response = await AxiosInstance.get<T>(url, config);
  return response.data;
 }

 async post<T>(url: string, data?: any, config?: ApiRequestConfig): Promise<T> {
  const response = await AxiosInstance.post<T>(url, data, config);
  return response.data;
 }

 async put<T>(url: string, data?: any, config?: ApiRequestConfig): Promise<T> {
  const response = await AxiosInstance.put<T>(url, data, config);
  return response.data;
 }

 async patch<T>(url: string, data?: any, config?: ApiRequestConfig): Promise<T> {
  const response = await AxiosInstance.patch<T>(url, data, config);
  return response.data;
 }

 async delete<T>(url: string, config?: ApiRequestConfig): Promise<T> {
  const response = await AxiosInstance.delete<T>(url, config);
  return response.data;
 }
}
