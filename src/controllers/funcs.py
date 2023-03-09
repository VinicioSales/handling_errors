from .custom_error import CustomError

def calculate(num1: float, num2: float)-> float:
    """
    Calculates the result of dividing num1 by num2.

    params:
        - float: num1
        - float: num2
    
        returns:
            - float: result
    """
    result = num1 / num2
    if num1 + num2 == 2:
        raise CustomError("Result 2!")
    return result