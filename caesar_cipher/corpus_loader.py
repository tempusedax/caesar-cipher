from nltk.corpus import words, names
import ssl
import nltk


nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

word_list = words.words()
name_list = names.words()