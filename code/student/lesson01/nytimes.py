#!/usr/bin/python
# Import required libraries
import sys

# Start counters and store the textfile in memory
totalImpressions = 0
totalClicks = 0
sumOfAge = 0
numOfNoSignedIn = 0
oldestAge = 0 

lines = sys.stdin.readlines()
lines.pop(0)
totalNumOfRecords = len(lines)

# For each line
for line in lines:
  	totalImpressions = totalImpressions + int(line.strip().split(',')[2])
  	age = int(line.strip().split(',')[0])
  	sumOfAge = sumOfAge + age
  	if age > oldestAge:
  		oldestAge = age
  	totalClicks = totalClicks + int(line.strip().split(',')[3])
  	if int(line.strip().split(',')[0]) == 0:
		numOfNoSignedIn = numOfNoSignedIn + 1

print 'Impression Sum: ', totalImpressions

#print 'Number of Record:', totalNumOfRecords

#print 'Number of not-signed-in record: ', numOfNoSignedIn

print 'A. Average Age: ', float(sumOfAge)/ (totalNumOfRecords - numOfNoSignedIn)

# print 'Total number of clicks: ', totalClicks

print 'B. Click through rate: ', float(totalClicks) / float(totalImpressions) * 100, '%'

print 'C. Oldest Age: ', oldestAge, 'years old'

#print 'Number of records (by using len method): ', len(lines)


### EOF ###