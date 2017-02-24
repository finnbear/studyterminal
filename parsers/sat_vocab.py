import re
import csv

csv_lines = []

with open("../datasets/raw/sat_vocab.txt") as file:
    for raw_line in file:
    	# Remove double spaces
    	single_spaced_line = re.sub(' +', ' ', raw_line)

    	# Split the line on spaces
    	split_line = single_spaced_line.split();

    	# Remove the useless line number
    	split_line.pop(0);

    	# Add a comma after the term
    	split_line[0] += ','

    	# Add a comma after the definition
    	split_line[-2] += ','

    	# Add a space to the end of each fragment, except the last
    	spaced_line = [fragment + ' ' for fragment in split_line]
    	spaced_line[-1].strip()

    	# Convert back to a string
    	csv_line = ''.join(str(fragment) for fragment in spaced_line)

        csv_lines.append(csv_line)

print("Successfully read " + str(len(csv_lines)) + " lines.")

with open('../datasets/csv/sat_vocab.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(csv_lines)