from random import randint
from itertools import combinations

x=30

list1=[randint(1,30)for i in range (8)]
print (list1)
comb= list(combinations(list1,2))
print(comb)
for item in comb:
    if(item[0]+item[1])==x:
        print(f"{item} sum is{x}")
