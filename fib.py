def fib(digit):
	if digit <= 1:
 		return (digit)
	else:
 		return (fib(digit-1) + fib(digit-2))
 
number_of_digit = 12
for i in range(number_of_digit):
 	print(fib(i))