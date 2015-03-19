#!/usr/bin/python

# Import required libraries
from __future__ import division
from collections import defaultdict
import sys
import csv


# Let's first write a little helper function which will take in
# a list of records containing all [(clicks, impressions)] data
# for a given key. Come back to this later to see how it's used.
def get_statistics(records):
    """
    return the summary for a key
    """
    clicks = []
    impressions = []

    for record in records:
        clicks.append(record[0])
        impressions.append(record[1])

    avg_click = sum(clicks) / len(clicks)
    avg_impr = sum(impressions) / len(impressions)
    max_click = max(clicks)
    max_impr = max(impressions)

    return [avg_click, avg_impr, max_click, max_impr]

# store the textfile in memory
lines = sys.stdin.readlines()
lines.pop(0)

# split up the CSV into list of lists of ints
lines = [map(int, line.strip().split(",")) for line in lines]

# Use a default dict to structure our dataset
# For defaultdict, see http://goo.gl/3rxCsr
# for the nesting, see http://goo.gl/GMx8h6
tree = lambda: defaultdict(tree)
data = tree()

# build up the grouped data object
for line in lines:

    # Unnecessary creation of variables, makes the code more readable
    age = line[0]  # age
    sex = line[1]  # sex
    clicks = line[2]  # clicks
    impressions = line[3]  # impressions
    signed_in = line[4]  # signed_in

    # Create a 'group' variable which references the composite key
    # of age, sex, and signed_in in the data object
    group = data[age][sex][signed_in]

    # The actual data that we which to store, represented as a tuple
    record = (clicks, impressions)

    # Check if key 'records' already exists, if it does we append the
    # data, else we create the list and add the first record to it.
    # For details, see http://goo.gl/zS8fru

    if 'records' in group:
        group['records'].append(record)
    else:
        group['records'] = [record]

# Empty list to collect our results in
results = []

# Now that we have constructed our data object, we can iterate through
# it again to come up with our summary statistics for each grouping.

# Ah - the infamous nested loop!

for age, i in data.iteritems():
    for sex, j in i.iteritems():
        for signed_in, k in j.iteritems():
            row = [age, sex, signed_in] + get_statistics(k['records'])
            results += [row]

# Now let's write our results to CSV

# header for csvmake_row
header = ["age", "gender", "signed_in", "avg_click", "avg_impressions",
          "max_click", "max_impressions"]

# write results to csv
with open("result.csv", "wb") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    for line in results:
        csvwriter.writerow(line)

# ### EOF ###
