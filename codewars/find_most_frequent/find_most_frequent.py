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
