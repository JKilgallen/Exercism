import re

def abbreviate(words):
    words = re.sub('\'|_', '', words)
    return ''.join(re.findall(r'\b\w', words)).upper()
