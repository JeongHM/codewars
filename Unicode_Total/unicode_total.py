# You'll be given a string, and have to return the total of all the unicode characters as an int. Should be able to handle any characters sent at it.

# examples:

# uniTotal("a") == 97 uniTotal("aaa") == 291

def uni_total(string):
    if not string:
        return 0
    return sum([ord(s) for s in string])

uni_total("abc")
uni_total("Mary Had A Little Lamb")