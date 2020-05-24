# Take a string str and return a string that is made up of the number of occurances of each english letter in str, followed by that letter. The string shouldn't contain zeros; leave them out.
#
# An empty string, or one with no letters, should return an empty string.
#
# Notes
# Ignore all case
# str will never be null
# Examples
# "This is a test sentence."  =>  "1a1c4e1h2i2n4s4t"
# ""  =>  ""
# "555"  =>  ""


def string_letter_count(s):
    s = s.lower()
    _s = sorted(set(s))
    answer = [f'{s.count(_)}{_}' for _ in _s if _.isalpha() and _.islower()]
    return ''.join(answer)



string_letter_count("The quick brown fox jumps over the lazy dog.")


# from collections import Counter

# def string_letter_count(s):
#     cnt = Counter(c for c in s.lower() if c.isalpha())
#     return ''.join(str(n)+c for c,n in sorted(cnt.items()))