import logging
from functools import wraps

logger = logging.getLogger(__name__)

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Вызвана функция: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper




