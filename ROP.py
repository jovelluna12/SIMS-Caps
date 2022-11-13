# Reorder Point (ROP) refers to the minimul level of inventory that determines when it is time to reorder.
# https://www.shipbob.com/blog/reorder-point-formula/
# DEMO Implementation Only. Information from CLient Required for Full Implementation

def calculate_ROP():
    lead_time_demand=30*5000 # 30 as lead time (number of days between placing an order and receiving the order), 5000 as average daily sales

    # To find demand during lead time, just multiply the lead time (in days) for a product by the average number of units sold daily:

    safety_stock=1000-900 # 1000 (Max Daily Orders*Max Lead Time), 900 (Average Daily Orders*Average Lead Time)

    # To find the proper safety stock level for a given product:
    # Multiply the maximum number of daily orders by the maximum lead time that may be required in case of supplier delays.
    # Multiply the average number of daily orders by the average lead time.
    # Subtract the result of Step 2 from the result of Step 1.

    ROP=lead_time_demand+safety_stock # ROP Formula
    return ROP
