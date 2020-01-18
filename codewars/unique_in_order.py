from itertools import groupby


def unique_in_order(iterable):

    answer = [i[0] for i in groupby(iterable)]
    return answer
