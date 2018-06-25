# Let's write a short program to display other information about each text in the gutenberg-corpus, computing statistics for each text. For a compact output display, we will round each number to the nearest integer, using round(). #


from nltk.corpus import gutenberg 

for w in gutenberg.fileids():
    print(w)


for fileid in gutenberg.fileids():
    num_char = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_char/num_words), round(num_words/num_sents), round(num_words/num_vocab))


# It displays three statistics for each text: average word length, average sentence length and the number of times each vocabulary item appears in the text on average (our lexical diversity score). The num_chars variable counts space characters.) #

# ctrl. + s = stop; ctrl. + q = continue; ctrl. + c = cancel #
