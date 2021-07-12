from collections import Counter

def is_isogram(string):
    x = Counter([char for char in string.lower() if char.isalpha()])
    return max(x.values(), default=0) <= 1
