class Dish:
    
    def __init__(self, count:int, name:str, price:int, mass:int ) -> None:
        self.count = count
        self.name = name
        self.price = price
        self.mass = mass

class Order:
    def __init__(self) -> None:

        self.orders:list = []
        self.all_count:int = 0
        self.all_price:int = 0
        self.all_mass:int = 0
    
    def adding_dish(self, meals:object):
        self.orders.append(meals)
        self.all_count += meals.count
        self.all_mass += meals.mass
        self.all_price += meals.price
    
    def voice_order(self):
        print(f'count = {self.all_count}, price = {self.all_price}, mass = {self.all_mass}')
    
    def pay(self, money:int):
        
        if self.all_price == money or self.all_price == 0:
            print('nice day')
        elif self.all_price > money:
            self.all_price -= money
            print(f'pay another {self.all_price} ')
            return self.all_price
        else:
            money -= self.all_price
            print(f'your change is {money}')
            self.all_price = 0
            money = 0
            return self.all_price, money
fish = Dish(2,'okyn',20,4)
meat = Dish(3,'salo',22,1)
water = Dish(1,'mineralka',10,3)
orders = Order()
orders.adding_dish(fish)
orders.adding_dish(meat)
orders.adding_dish(water)
orders.voice_order()
orders.pay(39)
orders.voice_order()
orders.pay(20)
orders.pay(14)

    
