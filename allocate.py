# Action --> Calculation --> Data
class AllocationService:
    def __init__(self):
        self.allocations = {}
    @staticmethod
    def pre_allocate_check(order_line, batch):
        return batch.available_qty >= order_line.qty
    def check_already_allocated(self, order_line):
        return order_line not in self.allocations
    def allocate(self, order_line, batch, can_allocate, not_already_allocated):
        if can_allocate and not_already_allocated:
            batch.available_qty = batch.available_qty - order_line.qty
            self.allocations[order_line] = 1
        return batch.available_qty
