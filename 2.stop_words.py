from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

# stopwords do not contain important significance to be used in search 1ueries. Usually these words are filtered out from search queries because they return vast amount of unnecessary information. 
# for more information about corpora visit: https://www.nltk.org/book/ch02.html

example = "so, in computing, stop words are words which are filtered out before or after processing of a text."

stop_words = set(stopwords.words("english")) # you can also use "german", "spanish", "russian", etc..

print(stop_words) # prints out stop words in english
print(len(stop_words)) # prints out a number of the stop words

print() # prints out a blank row for better overview

words = word_tokenize(example)

filt_sent = []

for w in words:
    if w not in stop_words:
        filt_sent.append(w)

print(filt_sent)
