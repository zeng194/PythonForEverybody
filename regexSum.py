#In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

filex = open("regex_sum_997429.txt","r")
sum = 0
for line in filex :
    nums = re.findall('[0-9]+', line)
    if len(nums) > 0 :
        for x in nums :
            sum = sum + int(x)
print(sum)