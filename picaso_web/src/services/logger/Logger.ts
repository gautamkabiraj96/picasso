import { ILogService } from './ILogService'
import { FileLoggerService } from './FileLoggerService'
import { ConsoleLoggerService } from './ConsoleLoggerService'

let logger: ILogService

if (typeof window === 'undefined') {
	logger = new FileLoggerService('app.log')
} else {
	logger = new ConsoleLoggerService()
}

export { logger }
