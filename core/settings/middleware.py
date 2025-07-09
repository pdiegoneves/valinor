# core/middleware.py
import time

from django.db import connection

from core.services.log import LoggerSingleton

logger = LoggerSingleton().get_logger


class DatabaseConnectionMonitor:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        sql_queries_start = len(connection.queries)

        response = self.get_response(request)

        duration = time.time() - start
        sql_queries_end = len(connection.queries)
        queries_executed = sql_queries_end - sql_queries_start

        if duration > 0.5:  # Log requisições lentas (mais de 0.5s)
            logger.warning(
                f"Requisição lenta: {request.path} - "
                f"Tempo: {duration:.2f}s - "
                f"Queries: {queries_executed}"
            )

        return response
