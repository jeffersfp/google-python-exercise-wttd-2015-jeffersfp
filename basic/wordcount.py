#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def helper(filename):
    """
    Reads file and build dictionary with words and their quantities in k,v
    :param filename: the file to be read
    :return: a dict with word: quantity
    """

    # get words for file (splited by space)
    words = [w for line in open(filename).readlines() for w in line.split()]

    # remove pontuation and transform lowercase
    for i in range(len(words)):
        words[i] = re.sub(r'(_|\+|-|\.|,|\?|\!|@|#|\$|%|\^|&|\*|\(|\)|;|\\|\/|\||<|>|\"|\')', '', words[i])
        words[i] = words[i].lower()

    # cast to set to remove repeated words and sort by alphabetical order
    words_set = set(words)

    # build dictionary with word => quantity
    words_dict = dict()
    for w in words_set:
        words_dict[w] = words.count(w)

    # finally return the dict
    return words_dict


# 1. For the --count flag, implement a print_words(filename) function that counts
# how often each word appears in the text and prints:
# word1 count1
# word2 count2
# ...
#
# Print the above list in order sorted by word (python will sort punctuation to
# come before letters -- that's fine). Store all the words as lowercase,
# so 'The' and 'the' count as the same word.
def print_words(filename):
    # build dict through helper
    words_dict = helper(filename)

    # simply iterate and print values
    for w,q in words_dict.items():
        print(w, q)


# 2. For the --topcount flag, implement a print_top(filename) which is similar
# to print_words() but which prints just the top 20 most common words sorted
# so the most common word is first, then the next most common, and so on.
#
# Use str.split() (no arguments) to split on all whitespace.
def print_top(filename):
    # build dict through helper
    words_dict = helper(filename)

    # builds a list containing tuples from the words and quantities respectively
    wq_list = list()
    for w,q in words_dict.items():
        wq_list.append((w,q))

    # sort the list by quantity (reversed to put most repeated words first)
    wq_list.sort(reverse=True, key=lambda x: x[-1])

    # simply print it
    for w,q in wq_list[:20]:
        print(w, q)

###


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
