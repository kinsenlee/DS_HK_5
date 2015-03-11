# Import required libraries
from __future__ import division
import sys
 
# Start a counter and store the textfile in memory
lines = sys.stdin.readlines()
lines.pop(0)
 
# initialization of variables
impressions = 0
age = 0
clicks = 0
max_age = 0
 
def getColumn(line,idx):
	return int(line[idx])

# For each line, find the sum of index 0,2 & 3 in the list.
for line in lines:
	line = line.strip().split(',')
	
	age = age + getColumn(line, 0)
	impressions = impressions + getColumn(line, 2)
	clicks = clicks + getColumn(line, 3)
	
	max_age = max(max_age, getColumn(line, 0))
 
print 'No. Impressions:', impressions
print 'Mean Age:', age / len(lines)
print 'Click-Through-Rate:', clicks / impressions
print 'Oldest Age:', max_age
