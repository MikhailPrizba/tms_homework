
class EvenRange:
    
    def __init__(self,num1:int,num2:int) -> None:
        self.num1 = num1
        self.num2 = num2
        self.result = 0
    
    
    
    def __next__(self):
        
        if self.result == 'Out of number!':
            raise StopIteration()

        if self.num1 % 2 != 0:
            self.num1 += 1

        if self.num1 % 2 == 0:
            self.result = self.num1
            self.num1 += 2
            if self.num1 > self.num2:
                self.result = 'Out of number!'
            return self.result
            
        
        
       
        
    
    def __iter__(self):
        return self
        
ier2 = EvenRange(3, 16)
for number in ier2:
    print(number)