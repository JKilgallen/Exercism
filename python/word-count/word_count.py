import re
from collections import Counter

punctuation = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'

def count_words(sentence):
    sentence = re.sub(',|_', ' ', sentence)
    return Counter(''.join(re.findall(r"(\w+'\w+?|[\w\d\s])?",sentence.lower())).split())