from src.controllers.error_handler import error_handler
from src.controllers.funcs import calculate

try:
    result = calculate(1, 1)
    print(f"result: {result}")
except Exception as exception:
    error_handler(exception)
