# stem words

from nltk import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["excite", "excited", "exciting", "excitingly", "excitement"]

for word in example_words:
    print(ps.stem(word))

# Stemming is the process of reducing a word into its stem, i.e. its root form. The root form is not necessarily a word by itself, but it can be used to generate words by concatenating the right suffix.

# For example, the words fish, fishes and fishing all stem into fish, which is a correct word. On the other side, the words study, studies and studying stems into studi, which is not an English word.

# Source: https://marcobonzanini.com/2015/01/26/stemming-lemmatisation-and-pos-tagging-with-python-and-nltk/
