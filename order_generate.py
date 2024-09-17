import random

#Объявление класса
class COrder : 
    #Инициализация
    def __init__(self):
        self.weight = 0
        self.floor = 0
        self.elevator = False 
    #Генерация случайного заказаa
    def Generate_Order(self):
        self.weight = random.randint(1, 300)
        
        self.floor = random.randint(1, 50)
        
        check_elevator = random.random()
        if (check_elevator >= 0.5) :
            self.elevator = True
        else :
            self.elevator = False
        return self

