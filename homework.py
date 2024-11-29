import random
locations = [random.randint(1,7) for i in range (3)]
weight = [200, 213, 300]
print('Enter three locations:')
while true:
    attemps = [int(input()) for i in range (3)]
    if attemps == weight:
        totweight = sum(weight)