import { ILogService } from './ILogService'
import { LogLevel } from './LogLevel'

export class ConsoleLoggerService implements ILogService {
  private consoleMethodMapping: Record<
    LogLevel,
    (message?: any, ...optionalParams: any[]) => void
  > = {
    [LogLevel.DEBUG]: console.debug,
    [LogLevel.INFO]: console.info,
    [LogLevel.WARN]: console.warn,
    [LogLevel.ERROR]: console.error,
    [LogLevel.FATAL]: console.error,
  }

  log(level: LogLevel, message: string, ...meta: any[]): void {
    const timestamp = new Date().toISOString()
    const consoleMethod = this.consoleMethodMapping[level] ?? console.log
    consoleMethod(`[${timestamp}] [${level}] ${message}`, ...meta)
  }

  debug(message: string, ...meta: any[]): void {
    this.log(LogLevel.DEBUG, message, ...meta)
  }

  info(message: string, ...meta: any[]): void {
    this.log(LogLevel.INFO, message, ...meta)
  }

  warn(message: string, ...meta: any[]): void {
    this.log(LogLevel.WARN, message, ...meta)
  }

  error(message: string, ...meta: any[]): void {
    this.log(LogLevel.ERROR, message, ...meta)
  }

  fatal(message: string, ...meta: any[]): void {
    this.log(LogLevel.FATAL, message, ...meta)
  }
}
