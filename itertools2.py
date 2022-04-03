from itertools import permutations
from random import randint

def is_prime(no):
    limit=int(no/2)+1
    for i in range(2,limit):
        if no%i >0:
            return True
        return False
list1= [randint(1,30)for i in range (10)]
print (list1)
plist1= list(permutations(list1,3))
print(plist1)
for items in plist1:
    if  is_prime(items[0]) and is_prime(items[1]) and is_prime(items[2]):
        print(f"{items} is prime")
