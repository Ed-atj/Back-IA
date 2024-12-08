class BaseException(Exception):
    """Exceção base para todas as exceções personalizadas."""
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        return f"{self.status_code} - {self.message}"

class AgendamentoNotFoundException(BaseException):
    def __init__(self, detail: str, message: str = "Usuário não encontrado"):
        message = f'{message}\nInfo: {detail}'
        super().__init__(message, status_code=404)

class AgendamentoAlreadyExistsException(BaseException):
    def __init__(self, detail: str, message: str = "Usuário já existente"):
        message = f'{message}\nInfo: {detail}'
        super().__init__(message, status_code=400)

class InvalidDataException(BaseException):
    def __init__(self, message: str = "Dados inválidos fornecidos"):
        super().__init__(message, status_code=422)
