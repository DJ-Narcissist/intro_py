def print_upper_words(words):
    """Print each word on sep line, uppercased.

         print_upper_words(["we", "are", "cool", "right"])
      
    """

    for word in words:
        print(word.upper())

word_list = ["we", "are", "cool", "right"]
print_upper_words(word_list)



def upper_word(words)
#Print words that start with the letter 'e' in uppercase

# words(list): list of words

    for word in words
        if word.starts('e'):
            print(word.upper())

word_list =["hello", "excitement","boats", "excutive","keyboard"]
upper_word(word_list)

def upper_words
"""
Print words that start with specific letters in uppercase

    words(list): List of words
    start(set):A set of letters to filter words
"""
for word in words:
    if word[0].lower() in start:
        print(word.upper())

word_list = ["hello", "excitement","boats", "excutive","keyboard"]
letters_set = {'h','e'}
upper_words(word_list,letters_set)