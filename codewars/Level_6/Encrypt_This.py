# Acknowledgments:
# I thank yvonne-liu for the idea and for the example tests :)

# Description:
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"


def encrypt_this(text):
    answer = list()
    for t in text.split():
        if len(t) == 1:
            answer.append(f'{ord(t)}')
        elif len(t) == 2:
            answer.append(f'{ord(t[0])}{t[1]}')
        elif len(t) == 3:
            answer.append(f'{ord(t[0])}{t[2]}{t[1]}')
        else:
            answer.append(f'{ord(t[0])}{t[len(t) - 1]}{t[2:len(t) - 1]}{t[1]}')
    return ' '.join(answer)
