# -*- coding: utf-8 -*-

'''
© 2017 Finn Bear All Rights 
'''

import csv
import random

words = []

with open('../datasets/csv/sat_vocab.csv', 'r') as file:
	reader = csv.reader(file)
	words = list(reader)

word = random.choice(words)

print(word[0].strip() + " is a " + word[2].strip() + " that means " + word[1].strip())