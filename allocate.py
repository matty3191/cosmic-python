# Action --> Calculation --> Data
class AllocationService:
    def check_already_allocated(self):
        pass

def pre_allocate_check(order_line, batch) -> bool:
    return batch.available_qty >= order_line.qty


def allocate(order_line, batch, can_allocate):
    if can_allocate:
        batch.available_qty = batch.available_qty - order_line.qty
    return batch.available_qty

