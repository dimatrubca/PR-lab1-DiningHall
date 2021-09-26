import json
import requests
import logging

from .table import TableState

logger = logging.getLogger(__name__)


class Waiter:
    def __init__(self, id) -> None:
        self.serving_tables = []
        self.prepared_orders = []
        self.id = id
        

    def serve_tables(self, tables):
        while True:
            for table in tables:
                if table.state == TableState.WAITING_TO_MAKE_ORDER:
                    order = table.generate_random_order(self.id)

                    logger.info(f"Sending post request to http://localhost:5000/order, id = " + str(order.id))
                    r = requests.post('http://localhost:5000/order', json=order.__dict__)
                    print(r.ok)
                    
                    self.serving_tables.append(table)
                    table.state = TableState.WAITING_ORDER_TO_BE_SERVED

                    break

            for order in self.prepared_orders:
                for table in self.serving_tables:
                    if table.validate_order(order):
                        table.state = TableState.FREE

                        logger.info(f"Order served by waiter {self.id}")