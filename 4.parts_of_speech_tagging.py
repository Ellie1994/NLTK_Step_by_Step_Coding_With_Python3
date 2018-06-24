import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import PunktSentenceTokenizer

train_text = gutenberg.raw("austen-persuasion.txt")
sample_text = gutenberg.raw("austen-persuasion.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


print(process_content())

# it will be able to print the whole book, to stop the printing press ctrl. + s
# ctrl. + q will run it further after the stop.
