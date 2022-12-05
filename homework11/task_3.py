class DataObject:
    def __init__(self, data) -> None:
        self.data = data


class Deque:
    
    list_deque:list = []

    @classmethod
    def append_left(cls, obj:object):
        if len(Deque.list_deque) == 5:
            print('deque is full')
        elif isinstance(obj, DataObject):
            Deque.list_deque.insert(0, obj.data)
        else:
            print('Not is DataObject')
    
    @classmethod
    def append_right(cls, obj:object):
        if len(Deque.list_deque) == 5:
            print('deque is full')
        elif isinstance(obj, DataObject):
            Deque.list_deque.append(obj.data)
        else:
            print('Not is DataObject')
    
    @classmethod
    def pop_left(cls):
        return Deque.list_deque.pop()
    
    @classmethod
    def pop_right(cls):
        return Deque.list_deque.pop(0)

a1 = DataObject(1)
a2 = DataObject(2)
a3 = DataObject(3)
a4 = DataObject(4)   
a5 = DataObject(5)
a6 = DataObject(6)
Deque().append_left(a1)
Deque().append_left(a2)
Deque().append_left(a3)
Deque().append_right(a4)
Deque().append_left(a5)
Deque().append_left(a6)
print(Deque.pop_left())
print(Deque.list_deque)