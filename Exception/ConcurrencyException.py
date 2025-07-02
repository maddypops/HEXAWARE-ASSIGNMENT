class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency conflict detected. Please retry."):
        super().__init__(message)
