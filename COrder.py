import random

#Объявление класса
class COrder : 
    #Инициализация
    def __init__(self):
        self.weight = 0
        self.floor = 0
        self.elevator = False 
    
    #Генерация случайного заказа
    def Generate_Order(self):
        self.weight = random.uniform(1, 300)
        self.floor = random.uniform(1, 50)
        
        check_elevator = random.random()
        if (check_elevator >= 0.5) :
            self.elevator = True
        else :
            self.elevator = False
        return self

