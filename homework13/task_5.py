def endless_fib_generator():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2

gen = endless_fib_generator()
while True:
	print(next(gen))