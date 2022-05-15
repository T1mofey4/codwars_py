# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, 
# False if not. Ignore numbers and punctuation.

import string
import re

s = "The quick, brown fox jumps over the lazy do!"

def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    regexp = re.sub('\s', '', s)
    low = regexp.lower()
    for i in alphabet:
        if i not in low:
            return False
    return True



print(is_pangram(s))