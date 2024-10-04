from typing import Dict
from enum import Enum

class ErrorCode(Enum):
    INVALID_INPUT = 1
    DATABASE_ERROR = 2
    NETWORK_ERROR = 3

class Error(Exception):
    def __init__(self, code: ErrorCode, message: str):
        self.code = code
        self.message = message

    def to_dict(self) -> Dict:
        return {
            'code': self.code.value,
            'message': self.message
        }

class ErrorHandler:
    def __init__(self):
        self.errors = {}

    def add_error(self, code: ErrorCode, message: str):
        self.errors[code] = message

    def get_error(self, code: ErrorCode) -> Error:
        message = self.errors.get(code)
        if message:
            return Error(code, message)
        else:
            return None

    def handle_error(self, error: Error):
        # Implement error handling logic here
        pass

error_handler = ErrorHandler()

def handle_error(error: Error):
    error_handler.handle_error(error)
