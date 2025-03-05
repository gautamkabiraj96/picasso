import { LogLevel } from './LogLevel'

export interface ILogService {
  log(level: LogLevel, message: string, ...meta: any[]): void
  debug(message: string, ...meta: any[]): void
  info(message: string, ...meta: any[]): void
  warn(message: string, ...meta: any[]): void
  error(message: string, ...meta: any[]): void
  fatal(message: string, ...meta: any[]): void
}
