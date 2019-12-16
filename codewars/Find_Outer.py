def find_outlier(integers):
    for i in range(0, len(integers) - 2):
        x, y, z = integers[i] % 2, integers[i + 1] % 2, integers[i + 2] % 2
        if (x == y and x != z) or (x == z and x != y) or (y == z and x != y):
            xyz = [x, y, z]
            s_dict = {xyz.count(s): s for s in xyz}
            return integers[i + xyz.index(s_dict.get(1))]
