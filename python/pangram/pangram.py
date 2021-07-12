from collections import Counter
from string import ascii_lowercase

def is_pangram(sentence):
    x = Counter([char for char in sentence.lower()])
    for char in ascii_lowercase:
        if x[char] == 0:
            return False
    return True