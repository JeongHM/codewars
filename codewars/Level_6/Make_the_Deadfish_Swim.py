# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]


def parse(items):
    init_num = 0
    answer = list()
    for item in items:
        if item == 'i':
            init_num += 1
        elif item == 'd':
            init_num -= 1
        elif item == 's':
            init_num = init_num ** 2
        elif item == 'o':
            answer.append(init_num)
    return answer
