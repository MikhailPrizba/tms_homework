def gen(path:str, letter:str):
    
    with open(path, mode='r') as file:
        for line in file:
            if line.startswith(letter):
                yield line
    
        
my_gen = gen('unsorted_names.txt','C')               

while True:
    try:
        print(next(my_gen))
    except StopIteration:
        break