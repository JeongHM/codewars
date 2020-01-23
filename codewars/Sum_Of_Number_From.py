def show_sequence(n):
    if n <0:
        return str(n) + '<0'
    if n==0:
        return '0=0'        
    s = list(range(n+1))
    return '+'.join([str(i) for i in s]) + ' = ' + str(sum(s))