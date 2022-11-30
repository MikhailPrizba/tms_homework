import task_1 as t1
import time

class Truck(t1.Auto):
    max_load = 30

    def __init__(self, brand: str, age: int, mark: str) -> None:
        super().__init__(brand, age, mark)

    def drive(self):
        print('Attention!')
        return super().drive()
    
    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Sedan(t1.Auto):
    max_speed =100
    def __init__(self, brand: str, age: int, mark: str) -> None:
        super().__init__(brand, age, mark)

    def drive(self):
        super().drive()
        print(f'max speed of sedan {self.brand} {self.mark} is {Sedan.max_speed}')

auto1 = Truck('tesla', 1,'truck')
auto2 = Sedan('volkswagen',3,'Polo')
auto1.drive()
auto1.load()
auto2.drive()
print(Truck.max_load)
print(Sedan.max_speed)
