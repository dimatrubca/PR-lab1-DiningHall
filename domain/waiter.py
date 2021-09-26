from typing import List
from domain.distribution import Distribution
from config import TIME_UNITS
import json
import requests
import logging

from .table import TableState
import service
import time
import random

logger = logging.getLogger(__name__)


class Waiter:
    def __init__(self, id) -> None:
        self.serving_tables = []
        self.prepared_orders:List[Distribution] = []
        self.id = id
        

    def serve_tables(self, tables):
        while True:
            for table in tables:
                if table.state == TableState.WAITING_TO_MAKE_ORDER:
                    order = table.generate_random_order(self.id)
                    table.state = TableState.WAITING_ORDER_TO_BE_SERVED
                    time.sleep(random.randint(2, 4) * TIME_UNITS)

                    service.send_order_to_kitchen(order)
                    
                    self.serving_tables.append(table)

                    break

            for distribution in self.prepared_orders:
                for table in self.serving_tables:
                    if table.validate_order(distribution):
                        table.free_table()

                        logger.info(f"Order {distribution.order_id} served by waiter {self.id}")

                self.serving_tables[:] = [table for table in self.serving_tables if not table.validate_order(distribution)] # todo: replace with somewhat more efficient