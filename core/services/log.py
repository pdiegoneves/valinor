from loguru import logger


class LoggerSingleton:
    _instance = None
    _logger = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
        return cls._instance

    @property
    def get_logger(self):
        if self._logger is None:
            logger.add(
                "logs.log",
                rotation="100 MB",
                retention="1 day",
                format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
                level="INFO",
                backtrace=True,
                diagnose=True,
            )
            self._logger = logger
        return self._logger
