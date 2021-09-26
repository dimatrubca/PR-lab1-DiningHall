import threading
import logging

from .menu import RestaurantMenu
from .table import Table
from .waiter import Waiter

logger = logging.getLogger(__name__)


class DinningHall:
    
    def __init__(self, num_tables = 5, num_waiters=2) -> None:
        self.tables = [Table(dinning_hall=self, id=i) for i in range(num_tables)]
        self.waiters = [Waiter(id=i) for i in range(num_waiters)]

        self.menu = RestaurantMenu()
        self.last_order_id = 0


    
    def run_simulation(self):
        logger.warn("Starting dinning hall simulation...")
        for waiter in self.waiters:
            threading.Thread(target=waiter.serve_tables(self.tables), args=(self.tables, )).start() # join?