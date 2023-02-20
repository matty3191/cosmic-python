import pytest

from src import allocate, Batch, Orderline


# When we allocate an order line to batch stock, 
# we should decrement the batch by the amount allocated


def test_decrement_orderline_from_batch():
    orderline = Orderline(10)
    batch = Batch(20)
    allocate(orderline, batch)
    assert batch.qty == 10



# # amount in batch must be >= amount in order line qty before allocation
# # happy path
# # e.g. if amount == 6 and orderline == 6 or less --> allocation of stock
# # if amount == 6 and orderline == 4 then error
# batch = int(input())
# orderline = int(input())
# def allocate(batch, orderline):
#     if orderline <= batch:
#         batch -= orderline
#         print(batch)
#         return True
#     else: 
#         print("cannot allocate when batch is less than orderline")

# def test_allocate_function_happy_path():
#     assert allocate(9, 6) == True

# def test_allocate_function_unhappy_path():
#     assert allocate(6, 9) == None

# allocate(batch=5, orderline=1)
# # unhappy path
# # common
# # if amount == 6 and orderline == 4 then nothing happens
# # try to order a letter / special character
# # try to order when theres no stock in "orderline"
# # try to order nothing

# # edge - extreme (max / min)
# # try to order 3000
# # try to order -1

# # corner - multiple parameters are at the extreme simultaneously
# # "dont click order twice yo, itll cahrge you twice"
# # 


# # order line can only be allocated once
# # happy path
# # line is processed once with confirmation / something blocking another accidental allocation
# # unhappy path
# # 

# # common
# # orderline is processed twice


# # edge - extreme (max / min)


# # corner - multiple parameters are at the extreme simultaneously


# # after allocation of orderline batch must be decremetned accordingly
# # happy path
# # unhappy path
# # common
# # edge - extreme (max / min)
# # corner - multiple parameters are at the extreme simultaneously


# # the warehouse batch must be used before teh shipment batch
# # happy path
# # unhappy path
# # common
# # edge - extreme (max / min)
# # corner - multiple parameters are at the extreme simultaneously


# # when the shipment batch must be used the product with the shortest eta needs to be allocated first
# # happy path
# # unhappy path
# # common
# # edge - extreme (max / min)
# # corner - multiple parameters are at the extreme simultaneously


# # happy path
# # unhappy path
# # common
# # edge - extreme (max / min)
# # corner - multiple parameters are at the extreme simultaneously
