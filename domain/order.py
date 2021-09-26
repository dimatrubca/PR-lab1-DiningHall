
class Order:
    def __init__(self, id, items, priority, max_wait) -> None:
        self.id = id
        self.items = items
        self.priority = priority
        self.max_wait = max_wait

    
    @staticmethod
    def generate_random_order(menu):
        pass