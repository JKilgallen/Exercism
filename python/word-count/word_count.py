import re
from collections import Counter

word_finder = re.compile(r"\b([A-z0-9']+)\b")

def count_words(sentence):
    sentence = re.sub(',|_', ' ', sentence).lower()
    return Counter(re.findall(word_finder, sentence))