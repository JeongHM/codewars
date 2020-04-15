# ### find_most_frequent
# ---
# #### Find the most frequent element or elements in the list.
# ​
# Example:
# ​
# find_most_frequent([1, 1, 2, 3]) == set([1])
#
# find_most_frequent([1, 1, 2, 2, 3]) == set([1, 2])
#
# find_most_frequent([1, 1, '2', '2', 3]) == set([1, '2'])


def find_most_frequent(param=[]) :
    Dict = dict()
    # {1: 2, 2: 2, 3: 1}
    for i in param :
        Dict.update({ i : param.count(i) })
        
    Count = max(Dict.values())

    List = [k for k,v in Dict.items() if Count == v]
    print(List)
    return List

if __name__ == '__main__' :
    # find_most_frequent([1, 1, 2, 3])
    find_most_frequent([1, 1, 2, 2, 3])
