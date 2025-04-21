import random
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
chance = random.random()*10
if (chance >= 8):
    print (friends[0])
elif (chance >=6):
    print (friends[1])
elif (chance >=4):
    print (friends[2])
elif (chance >=2):
    print (friends[3])
else:
     print (friends[4])