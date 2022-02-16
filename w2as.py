import re

name = input("Enter File: ")
if len(name) < 1:
    name = "regex_sum_1277287.txt"

handle = open(name)
text = handle.read()
list = re.findall('[0-9]+',text)
sum = 0
count = 0
for num in list:
    Num = int(num)
    sum = sum + Num
    count = count + 1
print('There are', count, 'values with a sum=', sum)
