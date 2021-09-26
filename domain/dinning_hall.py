from table import Table
from waiter import Waiter

class DinningHall:
    
    def __init__(self, num_tables = 5, num_waiters=2) -> None:
        self.tables = [Table() for table in num_tables]
        self.waiters = [Waiter() for waiter in num_waiters]

