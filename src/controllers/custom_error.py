class CustomError(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = "Error Type Example"
        self.status_code = 404