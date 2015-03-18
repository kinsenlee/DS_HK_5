#!/usr/bin/env python
"""
General Assembly - Data Science
Lesson 3 : New York Times, Aggregated CTR
"""
from __future__ import division
import urllib
from urlparse import urlparse
import pandas as pd
import os.path

# Define the location of the data directory in relation to this script.
DATA_DIR = '../../../data/'

def download_series(base_url, extension, limit):
    """
    download a series of files with incremental numeric suffix

    @param str base_url     base url to download from
    @param str extension    file format extension
    @param int limit        how many files should be downloaded
    @return list            list of file locations
    """
    # Create an empty list to store the file locations in
    file_list = []
    # for all numbers from 0 up to limit do the following
    for i in range(limit):
        # build up the filename by cutting off the last part of the url, adding the
        # number, and then appending the file extenstion
        file_name = urlparse(base_url).path.split('/')[-1] + str(i+1) + '.' + extension
        # build up the file's url by using the base_url, adding the number, and
        # then appending the file extenstion
        file_url = base_url + str(i+1) + '.' + extension
        # download the file from the file_url, save in DATA_DIR as file_name
        urllib.urlretrieve(file_url, DATA_DIR + file_name)
        # Inform the user the progress is being made
        print "Downloading %s..." % file_name
        # Add the file location to the list of downloaded CSVs
        file_list.append(DATA_DIR + file_name)

    return file_list

def merge_csv(file_list, output, headers=True):
    """
    Merge a list of CSVs into one large CSV, expect headers

    @param list file_list   list of CSVs to merge
    @param str output       name of the output file
    @param boolean headers  whether CSVs contain headers or not
    @return str             location of output file
    """
    # open the output file for writing, as output_file
    with open(DATA_DIR + output, 'a') as output_file:
        # the first CSV might contain headers, so write every line
        for line in open(file_list[0]):
            # write each line into output_file
            output_file.write(line)
        # now the rest:
        for file_name in file_list[1:]:
            # open the CSV file, as f
            f = open(file_name)
            # if the CSVs contain headers...
            if headers:
                # skip them, else continue
                f.next()
            # then write each line into the output_file again
            for line in f:
                 output_file.write(line)

    # return the ouput_file location
    return DATA_DIR + output

def load_nytimes_dataset():
    """
    Load NYT datasets into a Pandas DataFrame

    @return DataFrame      DataFrame of NYT Impressions
    """

    # Check whether the seperate CSVs have already been
    if not os.path.isfile(DATA_DIR + 'nyt_agg.csv'):
        # What base_url fo all files have in common?
        base_url = 'http://stat.columbia.edu/~rachel/datasets/nyt'
        # Download the series of CSVs and store the file_list.
        file_list = download_series(base_url, 'csv', 31)
        # Merge the CSVs listed in the file_list into nyt_agg.csv
        merge_csv(file_list, 'nyt_agg.csv')

    # read nyt_agg.csv into a pandas DataFrame
    df = pd.read_csv(DATA_DIR + 'nyt_agg.csv')

    return df

# Call the function which loads the NYT dataset into a DataFrame
df = load_nytimes_dataset()

# Aggregate by 'Age','Gender','Signed_In' to summarise for the whole group.
dfg = df.groupby(['Age','Gender','Signed_In'])

# Find the mean for "Clicks", "Impressions", given the groupings
dfx = dfg["Clicks", "Impressions"].mean()

# Add a new column with the CTR
dfx["CTR"] = dfx["Clicks"] / dfx["Impressions"]

# Only export the relevant data, CTR with indices.
dfx    ["CTR"].to_csv(DATA_DIR + 'nytimes_agg_CTR.csv')
