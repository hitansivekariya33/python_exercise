'''
 Here you are given two series input one is arithmetic progression (A.P.) and another one is geometric progress (G.P.). In which, one of the terms is wrong. Your task is to find out the wrong term and replace it with correct term.
 Arithmetic progression: An arithmetic sequence is a sequence of numbers where the differences between every two consecutive terms is the same.
For example: 1, 2, 3, 4, 5, 6, 7, 8 is an A.P. as consecutive terms difference (2-1 = 3-2 = 4-3 = 5-4 = 6-5 = 7-6 = 8-7 = 1) is equal.
 Geometric progression:
 A geometric sequence is a special type of sequence where
 the ratio of every two successive terms is a constant.
 For example: 2, 4, 8, 16, 32, 64 is an G.P. ratio of every two successive (4/2 = 8/4 =
 16/8 = 32/16 = 64/32 = 2) is constant
 Input:
One term wrong A.P. = [2, 5, 8, 11, 15, 17] One term wrong G.P. = [3, 9, 27, 81, 244, 729]
 Output:
Correct A.P. = [2, 5, 8, 11, 14, 17] Correct G.P. = [3, 9, 27, 81, 243, 729]
'''
ratio = int(input("Enter ratio:~"))
arithmetic = [2, 5, 8, 11, 15, 17]
for i in range(len(arithmetic)-1):
    if arithmetic[i+1]-arithmetic[i]!= ratio:
        arithmetic[i+1] = arithmetic[i]+ratio
print(arithmetic)


geometric = [3, 9, 27, 81, 244, 729]
for i in range(len(geometric)-1):
    if geometric[i+1]/geometric[i]!= ratio:
        geometric[i+1] = geometric[i]*ratio
print(geometric)     