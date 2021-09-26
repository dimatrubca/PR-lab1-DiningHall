import requests
from table import TableState

class Waiter:
    def __init__(self) -> None:
        self.serving_table = []
        pass

    def serve_orders(self, tables):
        while True:
            for table in tables:
                if table.state == TableState.WAITING_TO_MAKE_ORDER:
                    order = table.generate_random_order()
                    r = requests.post('http://localhost:5000/', json=order)
                    self.serving_tables.append(table)

                    break