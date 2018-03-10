import random

row = []
numbers = (list(range(1,41)))
for p in range(0, 7):
        row.append(random.choice(numbers))

row.sort()
print (row)
