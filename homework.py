import random
locations = [random.randint(1,7) for i in range (3)]
weight = [200, 213, 300]
print('Enter three locations:')
while True:
    attemps = [int(input()) for i in range (3)]
    if attemps == locations:
        totweight = sum(weight)
        if totweight == 713:
            print('Excellent! You have finded all boxes, total weight is', totweight)
        else:
            print('You have finded all boxes, but the weight is wrong')