'''
Recursion:
 Create a recursive function which returns the n-th Fibonacci number. [Fibonacci
sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]
o Input: N=8
o Output: 21
o Also, check if your recursive function is able to return the Fibonacci value at 60th or 90th term? If no, then check the concept of memoization for Fibonacci in recursive way.
 Create a recursion function that calculate the sum of numbers present in the list. o Input:
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
o Output: 152
'''

'''Create a recursive function which returns the n-th Fibonacci number. [Fibonacci
sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]'''

input_num = int(input("Enter a valid number::"))
memoized = {0: 0, 1: 1}
def fibonacci(number):
   if number in memoized: 
       return memoized[number]
   memoized[number] = fibonacci(number - 1) + fibonacci(number - 2)  
   return memoized[number]
print(fibonacci(input_num))
