import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Tokenization is the act of breaking up a sequence of strings into pieces such as words, keywords, phrases, symbols and other elements called tokens. Tokens can be individual words, phrases or even whole sentences. In the process of tokenization, some characters like punctuation marks are discarded."

print(sent_tokenize(example_text)) # tokenizes the whole sentences 

print() # prints out a blank row

print(word_tokenize(example_text)) # tokenizes words

print() # prints out a blank row

for i in sent_tokenize(example_text):
    print(i)   # loops over the each tokenized sentence

print() # prints out a blank row

for i in word_tokenize(example_text):
    print(i)   # loops over the each tokenized word
