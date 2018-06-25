# prints the sentence if you give its number

from nltk.corpus import gutenberg

caesar_sents = gutenberg.sents("shakespeare-caesar.txt")
print(caesar_sents[157]) # in [] give a number of a sentence you want to find

#######################################
# print the longest sentence

longest_sent = max(len(s) for s in caesar_sents)

print(longest_sent)
# the longest sentence is the sentence Nr. 157.
