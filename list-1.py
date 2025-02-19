import random
odd=[random.randrange(1,100,2) for i in range(5)]
even=[random.randrange(2,100,2) for i in range(4)]
print("The odd list is odd",odd)
odd[2:3]=even#flatten list
print("The modified list is",odd)
