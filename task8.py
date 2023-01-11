'''
You are given a list of numbers and your task is to sort the list without any inbuilt method of python.
 Input:
numbers = [2, 5, 6, 1, 3, 8, 9, 10]
 Output:
[1, 2, 3, 5, 6, 8, 9, 10]
'''

#sort list without in-built function
numbers = [2, 5, 6, 1, 3, 8, 9, 10]
for i in range (len(numbers)):
    for j in range(len(numbers)):
        if(numbers[i] < numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print("sorted list ::",numbers)
