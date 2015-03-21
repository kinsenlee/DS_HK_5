# Lesson05 Classwork
"""
1. Go through the same steps, but this time generate a new model use the log of
brain and body, which we know generated a much better distribution and cleaner
set of data. Compare the results to the original model. Remember that exp() can
be used to "normalize" our "logged" values. Note: Make sure you start a new
linear regression object!
"""
%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Set some Pandas options
pd.set_option('max_columns', 30)
pd.set_option('max_rows', 20)

# Default Plotting Size
mpl.rc('figure', figsize=(20, 8))

# DATA_DIR
DATA_DIR = "../data/"

mammals = pd.read_csv(DATA_DIR + 'mammals.csv')

# log(body) & log(brain)
mammals['log_body'] = np.log(mammals['body'])
mammals['log_brain'] = np.log(mammals['brain'])

# model fitting (original)
from sklearn import linear_model

regr = linear_model.LinearRegression()

X = mammals[['body']].values
y = mammals['brain'].values

regr.fit(X, y)
# score (original)
print("coef: %s" % regr.coef_)
print("SSE: %.2f" % np.mean((regr.predict(X) - y) ** 2))
print("score: %.2f" % regr.score(X, y))

# model fitting (log model)

lregr = linear_model.LinearRegression()

X = mammals[['log_body']].values
y = mammals['log_brain'].values

lregr.fit(X, y)

# score (log model)
print("coef: %s" % lregr.coef_)
sse = np.mean((np.exp(lregr.predict(X)) - np.exp(y)) ** 2)
print("SSE: %.2f" % sse)
print("score: %.2f" % lregr.score(X, y))

# Comparison

"""
2. Using your aggregate data compiled from nytimes1-30.csv, write a python
script that determines the best model predicting CTR based off of age and
gender. Since gender is not actually numeric (it is binary), investigate ways
to vectorize this feature. Clue: you may want two features now instead of one.
"""
nyt = pd.read_csv(DATA_DIR + 'nyagg.csv')

from sklearn import linear_model

regr = linear_model.LinearRegression()

X = nyt[['Age','Gender']].values
y = nyt['Ctr'].values

regr.fit(X, y)

# score
print("coef: %s" % regr.coef_)
print("SSE: %.2f" % np.mean((regr.predict(X) - y) ** 2))
print("score: %.2f" % regr.score(X, y))

"""
3. Compare this practice to making two separate models based on Gender, with
Age as your one feature predicting CTR. How are your results different? Which
results would you be more confident in presenting to your manager? Why's that?
"""
# model fitting (female)
regrf = linear_model.LinearRegression()

X = nyt[nyt.Gender==0][['Age','Gender']].values
y = nyt[nyt.Gender==0]['Ctr'].values

regrf.fit(X, y)

# score (female)
print("coef: %s" % regrf.coef_)
print("SSE: %.2f" % np.mean((regrf.predict(X) - y) ** 2))
print("score: %.2f" % regrf.score(X, y))

# model fitting (male)
regrm = linear_model.LinearRegression()

X = nyt[nyt.Gender==1][['Age','Gender']].values
y = nyt[nyt.Gender==1]['Ctr'].values

regrm.fit(X, y)

# score (male)
print("coef: %s" % regrm.coef_)
print("SSE: %.2f" % np.mean((regrm.predict(X) - y) ** 2))
print("score: %.2f" % regrm.score(X, y))

"""
4. Evaluate what data you could still use to improve your nytimes model.
Consider plotting your model to service your explanations and write a short
blurb about insights gained and next steps in your "data collection."
"""
nyt['LogAge'] = np.log(nyt['Age'])

regrl = linear_model.LinearRegression()

X = nyt[['Age','LogAge','Gender']].values
y = nyt['Ctr'].values

regrl.fit(X, y)

# score
print("coef: %s" % regrl.coef_)
print("SSE: %.2f" % np.mean((regrl.predict(X) - y) ** 2))
print("score: %.2f" % regrl.score(X, y))

# plot
age_f = nyt[nyt.Gender==0]['Age']
ctr_f = nyt[nyt.Gender==0]['Ctr']
age_m = nyt[nyt.Gender==1]['Age']
ctr_m = nyt[nyt.Gender==1]['Ctr']

plt.scatter(age_f, ctr_f, color='r', alpha=0.5, label='actual (female)')
plt.scatter(age_m, ctr_m, color='g', alpha=0.5, label='actual (male)')

nyt = nyt.sort(['Age','Gender'])
age_f = nyt[nyt.Gender==0]['Age']
X_f = nyt[nyt.Gender==0][['Age','LogAge','Gender']].values
age_m = nyt[nyt.Gender==1]['Age']
X_m = nyt[nyt.Gender==1][['Age','LogAge','Gender']].values
plt.plot(age_f, regrl.predict(X_f), color='r', linewidth=3,
         label='predict (female)')
plt.plot(age_m, regrl.predict(X_m), color='g', linewidth=3,
         label='predict (male)')
plt.legend(frameon=False, loc='upper left')
plt.show()
