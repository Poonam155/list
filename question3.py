import random
l=[random.randrange(1,30) for x in range(50)]
print("The list containing duplicate values is :",l)
for i in l:
    for j in l:
        if(i==j):
            l.remove(i)
print("The modified list after removing the duplicate values is :",l)

