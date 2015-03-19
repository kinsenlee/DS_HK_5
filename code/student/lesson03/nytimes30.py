import pandas as pd
import numpy as np
import pycurl
import sys
#from io import BytesIO

#read remote 30 files into local files
for count in range(30):

	count += 1

	remotePath = "http://stat.columbia.edu/~rachel/datasets/" + "nyt" + str(count) + ".csv"

	localPath = r"../../../data/" + "nyt" + str(count) + ".csv"

	with open(localPath, 'wb') as f:
		c = pycurl.Curl()
		c.setopt(c.URL, remotePath)
		c.setopt(c.WRITEDATA, f)
		
		#debug
		#print "start download from " + remotePath + ", please wait..."
		c.perform()
		c.close()
		

#initiate empty dataframe
df = pd.DataFrame()

#read 30 local files and put them into dataframes
for count in range(30):

	count += 1
	localPath = r"../../../data/" + "nyt" + str(count) + ".csv"
	newData = pd.read_csv(localPath)
	
	"""
	#debug
	print "get data from ", localPath
	print "newData tail::"
	print newData.tail()
	"""

	df = df.append(newData)		
	
	"""
	#debug
	print "df description after appending newData:"
	print df.describe()
	"""

#create summary dataframe for CTR calculation
dfg = df.groupby(['Age', 'Gender', 'Signed_In']).agg(np.sum)

#calculate mean and max
#summary = df.groupby(['Age', 'Gender', 'Signed_In']).agg([np.mean, np.max])


#reset index and change column lables
dfgReset = dfg.reset_index()
dfgReset.columns = ['Age', 'Gender', 'Signed_In', 'Impressions', 'Clicks']

#calculate CTR
dfgReset['CTR'] = dfgReset['Clicks'] / dfgReset['Impressions']

"""
#debug
print dfgReset.head()
"""

#Export to csv, exclude the index column
location = r"../../../data/nytimes_aggregation.csv"
dfgReset.to_csv(location, index=False)




