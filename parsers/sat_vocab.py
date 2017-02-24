# -*- coding: utf-8 -*-

'''
© 2017 Finn Bear All Rights 
'''

import re
import csv

comma_replacement = '`'

csv_lines = []

with open("../datasets/raw/sat_vocab.txt") as file:
    for raw_line in file:
    	# Replace all existing commas with a symbol
    	comma_symbol_line = re.sub(',', comma_replacement, raw_line)

    	# Remove double spaces
    	single_spaced_line = re.sub(' +', ' ', comma_symbol_line)

    	# Split the line on spaces
    	split_line = single_spaced_line.split();

    	# Remove the useless line number
    	split_line.pop(0);

    	# Add a comma after the term
    	split_line[0] += ','

    	# Add a comma after the definition
    	split_line[-2] += ','

    	# Add a space to the end of each fragment, except the firsts and lasts of each column (No longer necessary)
    	spaced_line = [fragment + ' ' for fragment in split_line]
    	spaced_line[-1] = spaced_line[-1].rstrip()

    	# Convert back to a string
    	csv_line_string = ''.join(str(fragment) for fragment in spaced_line)

    	# Split the string on commas
    	comma_symbol_csv_line = csv_line_string.split(',')

    	# Convert symbols back to commas
    	csv_line = [re.sub(comma_replacement, ',', fragment) for fragment in comma_symbol_csv_line]

        csv_lines.append(csv_line)

print("Successfully read " + str(len(csv_lines)) + " lines.")

with open('../datasets/csv/sat_vocab.csv', 'wb') as file:
    writer = csv.writer(file)
    for csv_line in csv_lines:
    	writer.writerow(csv_line)