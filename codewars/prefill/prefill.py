def prefill(count,word) :
    try :
        List = [word for i in range(int(count))]
        return List
    except :
        raise TypeError('{0} is invalid'.format(count))
if __name__ == '__main__' :
    prefill(3, prefill(2, '2d'))
