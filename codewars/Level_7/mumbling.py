# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(string):
    return '-'.join([(s.upper()) + (n * s) for n, s in enumerate(string.lower())])

def accum(string):
    result = [(s.upper()) + (n * s) for n, s in enumerate(string.lower())]
    return '-'.join(result)


def accum(string):
    result = []
    for n, s in enumerate(string.lower()):
        result.append(s.upper() + (n * s))

    return '-'.join(result)

accum('abcd')