

"""
C-1.24 Write a short Python function that counts the number of vowels in a given
character string.
"""
def count_vowel(data):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in data:
        if char in vowels:
            count += 1
    return count

data_str = 'Idea of Life As a Gift'

print("The sentence '{}' has {} vowels.".format(data_str, count_vowel(data_str)))

# output: 
# The sentence 'Idea of Life As a Gift' has 9 vowels.
