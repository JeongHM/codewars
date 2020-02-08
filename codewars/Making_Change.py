# Making Change
# Complete the method that will determine the minimum number of coins needed to make change for a given amount in American currency.

# Coins used will be half-dollars, quarters, dimes, nickels, and pennies, worth 50¢, 25¢, 10¢, 5¢ and 1¢, respectively. 
# They'll be represented by the symbols H, Q, D, N and P (symbols in Ruby, strings in in other languages)

# The argument passed in will be an integer representing the value in cents. 
# The return value should be a hash/dictionary/object with the symbols as keys, and the numbers of coins as values.
#  Coins that are not used should not be included in the hash.
#  If the argument passed in is 0, then the method should return an empty hash.

# Examples
# make_change(0)   -->  {}
# make_change(1)   -->  {"P":1}
# make_change(43)  -->  {"Q":1, "D":1, "N":1, "P":3}
# make_change(91)  -->  {"H":1, "Q":1, "D":1, "N":1, "P":1}


def make_change(amount):
    answer = {}
    names = ['H', 'Q', 'D', 'N', 'P']
    coins = [50, 25, 10, 5, 1]
    for name, coin in zip(names, coins):
        if amount >= coin:
            answer.update({name: amount // coin})
            amount = amount % coin
        else: 
            continue
    return answer
make_change(0)
    # your code here


