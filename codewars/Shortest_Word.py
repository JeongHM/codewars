# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.


def find_short(s):
    l = len(sorted(s.split(), key=lambda s: len(s))[0])
    return l
    # return l  # l: shortest word length


find_short('bitcoin take over the world maybe who knows perhaps')
