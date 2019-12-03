# When given a string of space separated words, return the word with the longest length. If there are multiple words with the longest length, return the last instance of the word with the longest length.

# Example:

# 'red white blue' //returns string value of white

# 'red blue gold' //returns gold

def longest_word(string_of_words):
    split_words = string_of_words.split(' ')
    word_dict = {s: len(s) for s in split_words}
    max_len = max(word_dict.values())
    max_len_list = [key for key, value in word_dict.items() if value == max_len]
    return max_len_list.pop()
    


# other solution
# def longest_word(string_of_words):
#     return max(reversed(string_of_words.split()), key=len)

# def longest_word(s):
#     return sorted(s.split(), key = len)[-1]