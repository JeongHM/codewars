# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# solution("camelCasing")  ==  "camel Casing"


def solution(s):
    return ''.join([f' {_s}' if _s.isupper() else _s for _s in s])

solution("camelCasing")


# Other Solution
# import re
# def solution(s):
#     return re.sub('([A-Z])', r' \1', s)