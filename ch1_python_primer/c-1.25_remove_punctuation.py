"""
C-1.25 Write a short Python function that takes a strings, representing 
a sentence, and returns a copy of the string with all punctuation removed. 
For example, if given the string "Let s try, Mike.", this function would return "Lets try Mike".
"""
def remove_punctuation(data):
    new_str_list = []
    alphabets = [chr(char) for char in range(ord('a'), ord('z')+1)]
    whitespace = ' '
    for char in data:
        if char.lower() in alphabets or char.lower() in whitespace:
            new_str_list.append(char)
    return ''.join(new_str_list)

data_str = "What's wrong?!! Nothing wrong!!!!"
print("The sentence:\t {}".format(data_str))
print("New sentence:\t {}".format(remove_punctuation(data_str)))

# output:
# The sentence:	 What's wrong?!! Nothing wrong!!!!
# New sentence:	 Whats wrong Nothing wrong
