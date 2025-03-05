import fs from 'fs'
import path from 'path'
import { ILogService } from './ILogService'
import { LogLevel } from './LogLevel'

export class FileLoggerService implements ILogService {
  private logFilePath: string

  constructor(logFileName = 'app.log') {
    this.logFilePath = path.join(process.cwd(), 'logs', logFileName)
  }

  log(level: LogLevel, message: string, ...meta: any[]): void {
    if (typeof window !== 'undefined') {
      console.warn('FileLoggerService is not available in the browser.')
      return
    }

    const timestamp = new Date().toISOString()
    const metaString = meta && meta.length > 0 ? JSON.stringify(meta) : ''
    const logLine = `[${timestamp}] [${level}] ${message} ${metaString}\n`

    try {
      fs.appendFileSync(this.logFilePath, logLine, { encoding: 'utf8' })
    } catch (err) {
      console.error(`Failed to write log to file: ${this.logFilePath}`, err)
    }
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
