# def hello_decorator(func):
#     def inner1(*args, **kwargs):
#         print("before Execution")
#
#         # getting the returned value
#         returned_value = func(*args, **kwargs)
#         print("after Execution")
#
#         # returning the value to the original frame
#         return returned_value
#
#     return inner1
#
#
# # adding decorator to the function
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
#
#
# a, b = 1, 2
#
# # getting the value through return of the function
# print("Sum =", sum_two_numbers(a, b))



# # code for testing decorator chaining
# def decor1(func):
# 	print('hi')
# 	def inner():
# 		print('hello')
# 		x = func()
# 		print(x)
# 		return x * x
# 	return inner
#
# def decor(func):
# 	print('how')
# 	def inner():
# 		print('yea')
# 		x = func()
# 		print(x)
# 		return 2 * x
# 	return inner
#
# @decor1
# @decor
# def num():
# 	print('hlooo')
# 	return 10
#
# print(num())


# Python code to illustrate
# Decorators with parameters in Python

def decorator(*args, **kwargs):
	print("Inside decorator")

	def inner(func):
		# code functionality here
		print("Inside inner function")
		print("I like", *args)

		func()

	# returning inner function
	return inner


@decorator("geeksforgeeks")
def my_func():
	print("Inside actual function")


# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
memory = {}


def memoize_factorial(f):
	# This inner function has access to memory
	# and 'f'
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
			print('result saved in memory')
		else:
			print('returning result from saved memory')
		return memory[num]

	return inner


@memoize_factorial
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num - 1)


print(facto(5))
print(facto(6))  # directly coming from saved memory
