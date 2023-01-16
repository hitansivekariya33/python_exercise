from itertools import combinations
'''
You are given a list of numbers and your task is to find out the pairs that have sum equals n (provided during input).
 No duplicate pair or similar pair should be in the output.  For example, if sum=12,
o [4, 8] can’t come twice in the output.
o Also, consider [4, 8] and [8, 4] as similar, so only [4, 8] have to come, not
both.
 Input:
o Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8] o n = 12
 Output:
o [[3, 9], [4, 8], [2, 10]]
See here, each pair addition is equals to 12 i.e. (3+9=12, 4+8=12, 2+10=12)
'''

numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
#find unique combination
combination = list(combinations(set(numbers),2))
#check sum of each pair
input_sum = int(input("Enter sum :~"))
list_sum = []
for combo in combination:
    if combo[0]+combo[1] == input_sum:
       list_sum.append(list(combo))
print(list_sum)