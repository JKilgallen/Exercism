def find_anagrams(word, candidates):
    return [x for x in candidates if is_anagram(x, word)]

def is_anagram(w1, w2):
    return sorted(w1.lower()) == sorted(w2.lower()) and w1.lower() != w2.lower()