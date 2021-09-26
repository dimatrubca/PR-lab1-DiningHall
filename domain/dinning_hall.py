import threading
import logging

from .menu import RestaurantMenu
from .table import Table
from .waiter import Waiter
import config

logger = logging.getLogger(__name__)


class DinningHall:
    
    def __init__(self, num_tables = config.NUM_TABLES, num_waiters=config.NUM_WAITERS) -> None:
        self.tables = [Table(dinning_hall=self, id=i) for i in range(num_tables)] # todo: convert to dict
        self.waiters = [Waiter(id=i) for i in range(num_waiters)]

        self.menu = RestaurantMenu()

    
    def run_simulation(self):
        logger.warn("Starting dinning hall simulation...")
        for waiter in self.waiters:
            threading.Thread(target=waiter.serve_tables(self.tables), args=(self.tables, )).start()
            

    def notify_order_received(self, distribution):
        for waiter in self.waiters:
            if waiter.id == distribution.waiter_id:
                logger.info(f"Waiter {waiter.id} notified about received order {distribution.order_id}")
                waiter.prepared_orders.append(distribution)