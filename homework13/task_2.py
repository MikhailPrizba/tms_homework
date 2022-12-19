class MySquareIterator:
    def __init__(self,list) -> None:
        self.list = list
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            i = self.list[self.index]
        except IndexError:
            raise StopIteration
        self.index +=1
        return i**2

lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for el in itr:
	print(el)