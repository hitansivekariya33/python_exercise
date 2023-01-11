'''
Find how many number of times the substring occurs in the given string.
 Input:
string = “PQRQRQRQ” substring = “QRQ”
 Output: 3

'''
import re
string = "PQRQRQRQ"
print(len(re.findall('(?=QRQ)', string)))
