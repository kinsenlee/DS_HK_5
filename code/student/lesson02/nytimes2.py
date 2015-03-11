#!/usr/bin/python
# Import required libraries
import sys
#import operator

f = open('nytimes.csv', 'r')

lines = f.readlines()  #list of lines

#create list of list as records
records = []
lines.pop(0)
for line in lines:
	record = line.split(",")
	record[4] = record[4].rstrip()
	
	#make age field with same number of characters --> prepare age-gender-signed_in key for sorting later
	age_ID = record[0] 
	if len(record[0]) == 1:
		age_ID = '00' + record[0]
	elif len(record[0]) == 2:
		age_ID = '0' + record[0]

	#create a unquie key for each age-gender-signed-in combination, and append to each record
	record.append(age_ID+"-"+record[1]+"-"+record[4])
	records.append(record)

#create dicionary, with unique combination as key.  Store records as lists under each key respectively
# NOTE: each key may contain more than 1 list
dictionary = {}

for record in records:
	if record[5] not in dictionary:
		dictionary[record[5]] = []
		dictionary[record[5]].append(record)
	else:
		dictionary[record[5]].append(record)

#create summary statistics for each key in the dictionary
# NOTE: one list (and later on 1 ilne) for each unique key
summary = []

for key in dictionary:
	# NOTE: dictionary[key] is a list of records
	age = int(dictionary[key][0][0])
	gender = int(dictionary[key][0][1])
	signed_in = int(dictionary[key][0][4])

	avgClick = 0
	avgImpression = 0
	maxClick = 0
	maxImpression = 0
	
	for record in dictionary[key]:
		# NOTE: record is a list, i.e. a line in the csv
				
		#max click calculation
		if record[3] > maxClick:
			maxClick = record[3]

		#prepare average click calculation
		avgClick += int(record[3])

		#max impression calculation
		if record[2] > maxImpression:
			maxImpression = record[2]

		#prepare average impression calculation
		avgImpression += int(record[2])

	avgClick = float(avgClick) / len(dictionary[key])
	avgImpression = float(avgImpression) / len(dictionary[key])

	summary.append([key, age, gender, signed_in, avgClick, avgImpression,int(maxClick), int(maxImpression)])

sortedSummary = sorted(summary)

#take away unique ID, which is not part of the required output
for record in sortedSummary:
	record.pop(0)

#add the heading
sortedSummary.insert(0,['age','gender','signed_in','avg_click','avg_impressions','max_click','max_impressions'])

#output to a csv file, file name: nytimes_summary.csv
summaryFile = open("nytimes_summary.csv", "w")

for record in sortedSummary:
	#transform all information in each record into string type
	for n in range(len(record)):
		record[n] = str(record[n])

	#prepare each line, and add new line character
	line = ",".join(record)
	line = line + '\n'
	summaryFile.write(line)

### EOF ###