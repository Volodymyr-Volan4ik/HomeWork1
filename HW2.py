import random

min = 1
max = 1000
quantity = 8

def get_numbers_ticket(min, max, quantity):

    if min >= max or quantity <= 0 or (max - min + 1) < quantity:

        return []
    
    numbers_set = set()

    while len(numbers_set) < quantity:

        numbers_set.add(random.randint(min, max))

    return sorted(list(numbers_set))

print(get_numbers_ticket(min, max, quantity))


    


    
