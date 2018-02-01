#A pangram is a sentence that contains every single letter of the alphabet at#
#least once. For example, the sentence "The quick brown fox jumps over the lazy dog"
#is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

#Difficulty: 6kyu.
#Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    alphabet = dict(zip(string.ascii_lowercase, [False]*26))
    for character in s.lower():
        if character.isalpha:
            alphabet[character] = True
    for there in alphabet.values():
        if not there:
            return False
    return True

assert True == is_pangram("The quick, brown fox jumps over the lazy dog")
assert True == is_pangram("Pack my box with five dozen liquor jugs")
assert True == is_pangram("New job: fix Mr Gluck's hazy TV, PDQ")
assert False == is_pangram("The fox jumps over the dog")
assert False == is_pangram("Is this sentence a pangram?")
assert False == is_pangram("How about this one?")