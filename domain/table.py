import json
import random
import uuid
from datetime import datetime
import logging

from .order import Order
from enum import Enum


logger = logging.getLogger(__name__)


class TableState(Enum):
    FREE = 1
    WAITING_TO_MAKE_ORDER = 2
    WAITING_ORDER_TO_BE_SERVED = 3


class Table:
    def __init__(self, dinning_hall, id) -> None:
        self.state = TableState.WAITING_TO_MAKE_ORDER
        self.order = None
        self.dinning_hall = dinning_hall
        self.id = id


    def generate_random_order(self, waiter_id):
        order_id = str(uuid.uuid4())
        num_items = random.randint(1, 10)
        items = random.choices(self.dinning_hall.menu.foods, k=num_items)
       # print(json.dumps(items))
        max_wait = max([1.3 * food_item['preparation-time'] for food_item in items]) # preparation-time_
        priority = random.randint(1, 5)
        
        self.order = Order(order_id, items, priority, max_wait, self.id, waiter_id)
        self.order.pick_up_time = datetime.utcnow().timestamp()

        logger.info("Random order generated:  " + str(self.order.id))

        return self.order

    def validate_order(self, distribution): # TODO: expand logic (mapper)
        if self.order.id != distribution.order_id:
            return False
        
        return False

    def free_table(self):
        self.order = None
        self.state = TableState.FREE