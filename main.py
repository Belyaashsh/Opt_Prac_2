from calc import calc
from order_generate import COrder

order = COrder
order.Generate_Order(order)

price = calc.Calculate_Price(order)

print("Расчет стоимости подъема груза на этаж")
print("------------------")
print("Weight:" , order.weight)
print("Floor:", order.floor)
print("Elevator:", order.elevator)
print("Total price:", price)
print("------------------")