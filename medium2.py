from collections import Counter
import math
nums =list(map(int,input().split()))
result=[]
n=math.floor(len(nums)/3)
count=Counter(nums)
for i in count.keys():
    if (count[i]>n):
        result.append(i)
print(result)
