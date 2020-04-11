# Welcome to the Codewars Bar!
# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
#
# Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting how many glasses of water you should drink to not be hungover.

#
# Example parties:
# Input 0:
# "1 beer"
#
# Output 0:
# "1 glass of water"
#
# Explaination 0:
# You drank one standard drink
#
# Input 1:
# "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"
#
# Output 1:
# "10 glasses of water"



def hydrate(drink_string):
    result = list()
    for string in drink_string.split(' '):
        try:
            _int = int(string)
        except Exception as e:
            continue
        else:
            result.append(_int)
    sum_result = sum(result)
    if sum_result == 1:
        return '1 glass of water'
    return f'{sum_result} glasses of water'




# Best Answer
# def hydrate(drink_string):
#     c=sum(int(c) for c in drink_string if c.isdigit())
#     return "{} {} of water".format(c,'glass') if c==1 else "{} {} of water".format(c,'glasses')