

class PKOrFRError(Exception):
    def __init__(self, message: str = '') -> None:
        self.message = message
        super().__init__(self.message)


class PKDoesNotExists(Exception):
    def __init__(self, message: str = '') -> None:
        self.message = message
        super().__init__(self.message)


class RowDoesNotExists(Exception):
    def __init__(self, message: str = '') -> None:
        self.message = message
        super().__init__(self.message)
