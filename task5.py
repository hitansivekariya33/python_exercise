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
main_list = []
def find(num_list, len, sum):
    print("Pairs whose sum = ", sum)
    for row in range(len):
        for column in range(row, len):
            sum_list = []
            if (num_list[row] + num_list[column]) == sum_no:
                sum_list.append(num_list[row])
                sum_list.append(num_list[column])
                main_list.append(sum_list)          
num_list = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
sum_no = int(input("Enter a sum::"))
find(num_list, len(num_list), sum_no)
tuple_list = list(set(tuple(sorted(sort_list)) for sort_list in main_list))
final_list = [list(sub) for sub in tuple_list]
print(final_list)
