"""
Write a function called word_index that takes one argument,a list of 
strings and returns the index of the longest word in thelist.
If there is no longest word (if all the strings are of the samelength), 
the function should return zero (0). For example, the listbelow should 
return 2.
"""

def word_index(words):
    """Finds the index of the longest word in a list of words.

    Args:
    words: A list of strings.

    Returns:
    The index of the longest word in the list, or 0 if all words are the same length.
 """

    if not words:
       return 0

    longest_length = max(len(word) for word in words)
    return words.index(next(word for word in words if len(word) == longest_length))



words1 = ["Hate", "remorse", "vengeance"]  # return 2
words2 = ["Love", "Hate"]  # return 0

print(word_index(words1))
print(word_index(words2))

