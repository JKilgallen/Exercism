import re
from collections import Counter

punctuation = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'

def count_words(sentence):
    sentence = re.sub(r'[\w\d\s]+[\']?[\w\s\d]', '', sentence)
    print(sentence)

count_words("car: carpet as java: javascript!!&@$%^&")