def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# use sorted function ,sort by the order of alphabet
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# use funtion pop to delete a word from words and print it
def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print(word)
    
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """Take in a full sentence and returns the sorted word."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# thins for debug    
sentence = "All good things come to those who wait."
words = break_words(sentence)
print(words)
sorted_words = sort_words(words)
print(sorted_words)
print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
print(sorted_words)
sorted_words = sort_sentence(sentence)
print(sorted_words)
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)