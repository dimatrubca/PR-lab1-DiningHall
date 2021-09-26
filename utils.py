from domain.distribution import Distribution
from typing import Dict


def distribution_request_to_distribution(distribution:Dict):
    order_id = distribution['order_id']
    table_id = distribution['table_id']
    waiter_id = distribution['waiter_id']
    items = distribution['items']
    priority = distribution['priority']
    max_wait = distribution['max_wait']
    pick_up_time = distribution['pick_up_time']
    cooking_time = distribution['cooking_time']
    cooking_details = distribution['cooking_details']

    distribution_obj = Distribution(order_id, table_id, waiter_id, items, priority, max_wait,
                                    pick_up_time, cooking_time, cooking_details)

    return distribution_obj