import random
l=[random.randrange(-100,100) for i in range(30)]
l1=[]
l2=[]
for ele in l:
    if (ele>=0):
        l1.append(ele)
    else:
        l2.append(ele)
print("The list containing positive integers is ",l1)
print("The list containing negative integers is ",l2)
