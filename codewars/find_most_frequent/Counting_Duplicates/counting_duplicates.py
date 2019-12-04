def duplicate_count(text):
    lower_text = text.lower()
    ct_dict = {i: lower_text.count(i) for i in set(text) if lower_text.count(i) > 1}
    return len(ct_dict.keys())

duplicate_count('aabBcde')