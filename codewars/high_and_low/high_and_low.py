def high_and_low(numbers):
    # in list (string)
    # convert string to int list value
    num = [int(n) for n in numbers.split(' ')]
    return "{0} {1}".format(max(num), min(num))

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
