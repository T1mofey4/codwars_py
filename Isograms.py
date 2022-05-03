# An isogram is a word that has no repeating letters, 
# consecutive or non-consecutive. Implement a function
# that determines whether a string that contains only 
# letters is an isogram. Assume the empty string is an 
# isogram. Ignore letter case.

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)
import re

str = 'abA'

def is_isogram(string):
    chk = re.findall(r"(.).*\1", string.lower())
    if len(chk) == 0:
        return True
    else:
        return False

print(is_isogram(str))