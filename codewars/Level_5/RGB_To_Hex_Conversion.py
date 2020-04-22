
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def init(n):
    if n < 0:
        return 0
    if n > 255:
        return 255
    return n
    
def rgb(r, g, b):
    answer = [hex(init(s)).upper().replace('X','') if s < 16 else hex(init(s)).upper().replace('0X','') for s in [r, g, b]]
    return ''.join(answer)
    


# Other Solution
# def limit(num):
#     if num < 0:
#         return 0
#     if num > 255:
#         return 255
#     return num


# def rgb(r, g, b):
#     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))