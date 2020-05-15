# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.

#
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating

# def rot13(message):
#     answer = []
#     upper_map = {i: i + 13 if i <= 77 else i - 13 for i in range(65, 91)}
#     lower_map = {i: i + 13 if i <= 109 else i - 13 for i in range(97, 123)}
    
#     for m in message:
#         _m = m
#         if m.islower():
#             _m = chr(lower_map[ord(m)])

#         elif m.isupper():
#             _m = chr(upper_map[ord(m)])
        
#         answer.append(_m)
#     return ''.join(answer)

a = [1,2,3]
print(a[4])
