import nltk
nltk.download()
from nltk.util import ngrams
simplText = 'welcome to Data Science Lab'
NGRAMS = ngrams(sequence=nltk.word_tokenize(simplText), n=3)
for grams in NGRAMS:
  print(grams)