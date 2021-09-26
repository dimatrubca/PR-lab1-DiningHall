from enum import Enum

class TableState(Enum):
    FREE = 1
    WAITING_TO_MAKE_ORDER = 2
    WAITING_ORDER_TO_BE_SERVED = 3

class Table:
    def __init__(self) -> None:
        self.state = TableState.FREE
        self.order = None

    def generate_random_order(self):
        pass


    def validate_order():
        pass