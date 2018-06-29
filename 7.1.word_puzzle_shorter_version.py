import nltk

x = [w for w in nltk.corpus.words.words() if len(w) >= 4 and "d" in w and nltk.FreqDist(w) <= nltk.FreqDist("awdptklop")]

print(x)
