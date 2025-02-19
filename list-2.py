import random
l=[random.randrange(1,100) for ele in range(20)]
print("The list is ",l)
n=int(input("Enter the number between 1 to 100: "))
count=0
for i in l:
    if(n==i):
        count=count+1
if(count!=0):
    print("The occurence=",count)
else:
    print("Number not found")
