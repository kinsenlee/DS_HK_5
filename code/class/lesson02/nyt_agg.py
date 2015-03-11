#!/usr/bin/python
# Import required libraries
from __future__ import division
from itertools import groupby
import sys
import csv

def make_row(key, group):
    """
    return the summary for a key
    """
    clicks = [x[3] for x in group]
    impressions = [x[2] for x in group]
    avg_click = sum(clicks) / len(clicks)
    avg_impr = sum(impressions) / len(impressions)
    max_click = max(clicks)
    max_impr = max(impressions)
    return list(key) + [avg_click, avg_impr, max_click, max_impr]

# store the textfile in memory
lines = sys.stdin.readlines()
lines.pop(0)

# sort and group
keyfunc = lambda x: (x[0], x[1], x[4])
lines = [map(int, line.strip().split(",")) for line in lines]
lines = sorted(lines, key=keyfunc)
groups = []
keys = []
for k, g in groupby(lines, keyfunc):
    keys.append(k)
    groups.append(list(g))

# prepare a list of results
results = []
for idx, k in enumerate(keys):
    group = groups[idx]
    results.append(make_row(k, group))

# header for csv
header = ["age", "gender", "signed_in", "avg_click", "avg_impressions",
          "max_click", "max_impressions"]

# write results to csv
with open("result.csv", "wb") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    for line in results:
        csvwriter.writerow(line)
    f.close()

### EOF ###
