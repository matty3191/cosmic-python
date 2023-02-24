from batch import Batch
from order_line import OrderLine
from allocate import allocate, pre_allocate_check, AllocationService

class TestAllocation:

    def test_pre_allocation_check_on_order_line_and_batch(self):
        order_line = OrderLine(sku="RED-CHAIR", qty=10)
        batch = Batch(sku="RED-CHAIR", available_qty=20)
        assert pre_allocate_check(order_line, batch)

    def test_batch_available_quantity_decreases_after_successful_order_line_allocation(self):
        order_line = OrderLine(sku="REC-CHAIR", qty=10)
        batch = Batch(sku="RED-CHAIR", available_qty=20)

        assert batch.available_qty == 20
        allocate(order_line, batch, can_allocate=True)
        assert batch.available_qty == 10

    def test_batch_available_quantity_is_less_than_order_line_quantity_at_allocation(self):
        order_line = OrderLine(sku="RED-CHAIR", qty=20)
        batch = Batch(sku="RED-CHAIR", available_qty=10)

        allocate(order_line, batch, pre_allocate_check(order_line, batch))
        assert batch.available_qty == 10

    def test_allocations_are_idempotent(self):
        allocation_service = AllocationService()
        order_line = OrderLine(sku="RED-CHAIR", qty=10)
        batch = Batch(sku="RED-CHAIR", available_qty=20)

        assert batch.available_qty == 20
        allocation_service.allocate(order_line, batch, pre_allocate_check(order_line, batch))
        assert batch.available_qty == 10
        allocation_service.allocate(order_line, batch, pre_allocate_check(order_line, batch))
        assert batch.available_qty == 10
