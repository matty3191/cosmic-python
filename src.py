class Orderline:
    def __init__(self, qty):
        self.qty = qty


class Batch:
    def __init__(self, qty):
        self.qty = qty


def allocate(orderline, batch):
    batch.qty = batch.qty - orderline.qty
    return batch.qty

