from batch import Batch
from order_line import OrderLine
from allocate import allocate, pre_allocate_check
from allocate import AllocationService

class TestAllocation:

    def test_pre_allocation_check_on_order_line_and_batch(self):
        order_line = OrderLine(10)
        batch = Batch(20)

        assert pre_allocate_check(order_line, batch)

    def test_batch_available_quantity_decreases_after_successful_order_line_allocation(self):
        order_line = OrderLine(10)
        batch = Batch(20)

        assert batch.available_qty == 20
        allocate(order_line, batch, can_allocate=True)
        assert batch.available_qty == 10

    def test_batch_available_quantity_is_less_than_order_line_quantity_at_allocation(self):
        order_line = OrderLine(20)
        batch = Batch(10)

    def test_allocations_are_idempotent(self):
        allocation_service = AllocationService()
        order_line = OrderLine("RED-CHAIR", 10)
        batch = Batch("RED-CHAIR", 20)

        allocation_service.check_already_allocated(order_line)
        allocation_service.allocate(order_line, batch, pre_allocate_check(order_line, batch))
        allocation_service.update_allocations(order_line)
        allocation_service.check_already_allocated(order_line)
        allocation_service.allocate(order_line, batch, pre_allocate_check(order_line, batch))

        assert not allocation_service.check_already_allocated
