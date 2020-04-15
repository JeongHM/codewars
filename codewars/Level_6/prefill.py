# ## prefill
# ---
#
# #### Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.
#
# #### You have to validate input:
# - v can be anything (primitive or otherwise)
# - if v is ommited, fill the array with undefined
# - if n is 0, return an empty array
# - if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
# - When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.


def prefill(count,word) :
    try :
        List = [word for i in range(int(count))]
        return List
    except :
        raise TypeError('{0} is invalid'.format(count))
if __name__ == '__main__' :
    prefill(3, prefill(2, '2d'))
