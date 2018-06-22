from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

example = "so, in computing, stop words are words which are filtered out before or after processing of a text."

stop_words = set(stopwords.words("english")) # you can also use "german", "spanish", "russian", etc..

words = word_tokenize(example)

filt_sent = [w for w in words if not w in stop_words]

print(filt_sent)
