from .custom_error import CustomError
from .configuring_error_log import logger

def error_handler(error):
    """
    Handles the raised errors

    params:
        - exeption: error
    """
    if isinstance(error, CustomError):
        print(f"status code: {(error.status_code)}")
        logger.error(error)
    
    if isinstance(error, ZeroDivisionError):
        print(error)
        logger.error(error)
    
    if isinstance(error, TypeError):
        print(error)
        logger.error(error)
