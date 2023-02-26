import random

def random_list_summer(n): 
# was it supposed to be random_list_number? what does this have to do with summer lol
    list = []
    for i in range(n):
        list.append(random.randrange(-100,100))
    return(list)

print(random_list_summer(5))