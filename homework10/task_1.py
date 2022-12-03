


class Auto:
    '''class describing the car'''
    color = 'blue'
    weight = 10
    def __init__(self,brand:str,age:int,mark:str) -> None:
        self.brand = brand
        self.age = age
        self.mark = mark
    
    def drive(self):
        print(f'Car {self.brand} {self.mark} drives')
    
    def stop(self):
        print(f'Car {self.brand} {self.mark} stops')
    
    def use(self):
        self.age += 1

