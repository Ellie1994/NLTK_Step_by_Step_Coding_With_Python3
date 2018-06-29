# A wordlist is useful for solving word puzzles. Our program iterates through every word and checks whether it meets the conditions.

import nltk
from nltk import FreqDist

puzzle = nltk.FreqDist("anbeioplq")

oblig = "n"
wordlist = nltk.corpus.words.words()

puzzle_solved = [w for w in wordlist if len(w) >= 5
and oblig in w
and nltk.FreqDist(w) <= puzzle]

# The  FreqDist comparison method permits us to check that the frequency of each letter in the candidate word is less than or equal to the frequency of the corresponding letter in the puzzle.

print(puzzle_solved)
