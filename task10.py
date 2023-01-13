'''
Print the following patterns. In the patterns ‘_’ (underscore) denotes the space.
'''

numbers = int(input("Enter a number::"))

print("---------------------------------------------")
#pattern 1
'''
** **
*   *

*   *
** **
'''
for i in range(1, numbers+1):
  i = i - (numbers//2 +1)
  if i < 0:
    i = -i
  print("*" * i + " " * (numbers - i*2) + "*"*i)

print("---------------------------------------------")
#pattern2
'''
  *  
 *** 
*****
 *** 
  *  
'''
for i in range(1, numbers+1):
  i = i - (numbers//2 +1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (numbers - i*2) + " "*i)

print("---------------------------------------------")
#pattern 3
'''
*
**
* *
*  *
*****
'''
for i in range(1,numbers+1):
    for j in range(1,i+1):
        if i==1 or j==1 or i==numbers or j==i:
            print("*", end="")
        else:
            print(" ",end="")
    print()

print("---------------------------------------------")
#pattern 4
'''
*****
*   *
*   *
*   *
*****
'''
for i in range(0, numbers):
    for j in range(0, numbers):
        if i==0 or j==0 or i == numbers-1 or j == numbers-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
