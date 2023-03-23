class Counter:
    
    def __init__(self, start = 0, stop = float('inf')) -> None:
        self.start = start
        self.stop = stop
        
    def increment(self):
        if self.start == self.stop:
            print('Maxima value is reached')
        else:
            self.start +=1
    
    def get(self):
        print(self.start)
a = Counter(start=42)
a.increment()
a.get()

b = Counter()
b.increment()
b.get()
b.increment()
b.get()

c = Counter(start=42, stop=43)
c.increment()
c.get()
c.increment()
c.get()