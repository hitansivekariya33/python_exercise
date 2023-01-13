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
