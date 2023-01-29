import Manager

man=Manager.Manager()

average_lead_time=man.get_Ave_LeadTime()

def calculate_ROP(qty):
    safety_stock=30/100*qty
    Reorder_Level=average_lead_time[0]+safety_stock

    return Reorder_Level
