from collections import Counter

'''
You are given a list of person names. Your task is to find out the three most frequent and three least frequent names.
 Input:
names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
 Output:
o Names: 'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White'] o Name lengths: [5, 7, 8, 5, 5, 5, 6, 6, 5, 6, 8, 6, 7, 5]
o The three most frequent name lenghts are:
6 names of length 5: ['Smith', 'Jones', 'Brown', 'Davis', 'Moore'] 4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']
2 names of length 8: ['Williams', 'Anderson']
o The three least frequent name lenghts are:
2 names of length 7: ['Johnson', 'Jackson']
2 names of length 8: ['Williams', 'Anderson']
4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']
'''

#find length of each word 
names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

dict_len = {}
for name in names:
    dict_len[name] = len(name)
print(dict_len)

#print only length 
print("length is ::",list(dict_len.values()))

#name with length in sorted order
sorted_dict=sorted(dict_len.items(), key=lambda x: x[1])
print("name with length::",sorted_dict)

len_wise_name = dict()
for name_len in sorted_dict:
    if name_len[1] in len_wise_name.keys():
        len_wise_name[name_len[1]].append(name_len[0])
    else:
        len_wise_name[name_len[1]] = [name_len[0]]
print(len_wise_name)

#three most frequent
most = dict(sorted(len_wise_name.items())[:3])
for three_most_key,three_most_value in most.items():
    print(len(three_most_value),"name of length is",three_most_key,":",three_most_value)
