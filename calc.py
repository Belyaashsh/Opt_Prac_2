from order_generate import COrder

class calc :
    def Calculate_Price(order = COrder) :
        if (order.weight <= 50) :
            if (order.elevator == True) :
                return 300
            else :
                return (300 * (order.floor - 1) + 2000)
        if (order.weight > 50 and order.weight <= 100) :
            if (order.elevator == True) :
                return 1000
            else :
                return round(300 * (order.weight / 100) * (order.floor - 1) + 2000)
        if (order.weight > 100) :
            if (order.elevator == True) :
                return 1200
            else :
                return round(300 * (order.weight / 100) * (order.floor - 1) + 2000)    