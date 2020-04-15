# What's in a name?
# ..Or rather, what's a name in? For us, a particular string is where we are looking for a name.
# Task
# Test whether or not the string contains all of the letters which spell a given name, in order.
#
# The format
# A function passing two strings, searching for one (the name) within the other. ``function nameInStr(str, name){ return true || false }``
# Examples
# nameInStr("Across the rivers", "chris") --> true
#             ^      ^  ^^   ^
#             c      h  ri   s
#
# Contains all of the letters in "chris", in order.
# nameInStr("Next to a lake", "chris") --> false
#
# Contains none of the letters in "chris".
# nameInStr("Under a sea", "chris") --> false
#                ^   ^
#                r   s
#
# Contains only some of the letters in "chris".
# nameInStr("A crew that boards the ship", "chris") --> false
#              cr    h              s i
#              cr                h  s i
#              c     h      r       s i
#              ...
#
# Contains all of the letters in "chris", but not in order.
# nameInStr("A live son", "Allison") --> false
#            ^ ^^   ^^^
#            A li   son
#
# Contains all of the correct letters in "Allison", in order,
# but not enough of all of them (missing an 'l').

from collections import OrderedDict
def name_in_str(str, name):
    result = [s for s in str for n in name if s == n]
    print(''.join(list(OrderedDict((x, None) for x in result))))
    print(name)
    # if ''.join(list(OrderedDict((x, None) for x in result))) == name : return True
    # else: return False
    # if list(OrderedDict((x, None) for x in result) == ''.join(name)


    # result = [n for n in name for s in str if n == s]
    # print(set(result))
    # if set(sorted(result)) == set(sorted(name)): return True
    # else: return False

name_in_str("Across the rivers", "chris")
# name_in_str("Across the rivers", "chris")
# name_in_str("A crew that boards the ship", "chris")