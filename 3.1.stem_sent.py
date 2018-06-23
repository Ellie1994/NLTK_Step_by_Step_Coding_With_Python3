# stem sentences 

from nltk import PorterStemmer 
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

text = "it is exciting to learn with excitement and be excited about new skills."

words = word_tokenize(text)

for word in words:
    print(ps.stem(word)) 
