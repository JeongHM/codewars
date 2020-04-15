# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.
#

def expanded_form(num):
    string = str(num)
    length = len(string)

    result = [str(int(i) * (10 ** (int(length) - n - 1))) for n, i in enumerate(string) if i != '0']
    return ' + '.join(result)

expanded_form(12)
expanded_form(70304)


# def expanded_form(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')