import pandas as pd
import csv
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

def __init__(self):
	self.train = pd.read("train.tsv", header=0, delimiter="\t", quoting=3)

def clean_data(self,raw_text):
	text = Beautifulsoup(raw_text).get_text()
	letters = re.sub("[^a-zA-z]"," ",text)
	words = letters_only.lower()
	words = words.split()
	stops = set(stopwords.words("english"))
	meaningful_words = [w for w in words if not w in stops]
	return ( " ".join( meaningful_words ))

def get_data(self):
	num = self.train["EssayText"].size
	data = []
	for i in xrange(0,num):
		data.append( clean_data( self.train["EssayText"][i]))
	return data


