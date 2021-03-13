#
# #Random word generator - based on format of words
#
# #Another way to get just consonants would be to use string.ascii_lowercase
# #(all letters) and remove the vowels.
#
# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#
# word_format = "ccvcvvc"
# word = ""
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     else:
#         word += random.choice(VOWELS)
#
# print(word)


def fn(x, y):
    z = x + y


print(fn(1, 2)) # it will print none because the function has nothing inside.