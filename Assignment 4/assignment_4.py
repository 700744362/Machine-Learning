# -*- coding: utf-8 -*-
"""Assignment 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AT_2b9xPqTfSo3zbShkhXCHz3wYVeOBl
"""

import pandas as pd
url="https://raw.githubusercontent.com/700744362/Machine-Learning/main/Dataset/"
data = pd.read_csv(url+"data.csv")
print(data.describe(),"\n")
print(data)
data=data.fillna(data.mean())
print(data,"\n")

print(data.agg({'Maxpulse':['min','max','count','mean'],'Calories':['min','max','count','mean']}),"\n")

print(data[(data['Calories']>=500) & (data['Calories']<=1000)],"\n")

print(data[(data['Calories'] > 500) & (data['Pulse'] < 100)],"\n")

df_modified = data.drop('Maxpulse', axis=1)
print("Modified Data \n",df_modified)

data.drop('Maxpulse', axis=1, inplace=True)
print(" Data after  droping Maxpulse in Original Data set \n",data)

data['Calories']=data['Calories'].astype(int)
print(data.dtypes)

import matplotlib.pyplot as plt
data.plot.scatter(x='Duration', y='Calories')
plt.title('Calories Burned vs. Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Calories Burned')
plt.show()

import seaborn as sns
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
train_df = pd.read_csv(url+'train.csv')
test_df = pd.read_csv(url+'test.csv')
titanic = [train_df, test_df]
 
for dataset in titanic:
    dataset['Sex'] = dataset['Sex'].map( {'female': 1, 'male': 0} ).astype(int)
  


g = sns.FacetGrid(train_df, col='Survived')
g.map(plt.hist, 'Sex', bins=20)

import pandas as pd
from scipy.stats import pearsonr


titanic['sex'] = pd.factorize(titanic['sex'])[0]

corr, p_value = pearsonr(titanic['survived'], titanic['sex'])

print('Correlation coefficient:', corr)
print('P-value:', p_value)

# 2
titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.isnull().sum())
sns.barplot(x='sex', y='survived', data=titanic)
sns.catplot(x='class', y='survived', hue='sex', data=titanic, kind='bar')
plt.show()


corr = titanic.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
sns.pairplot(titanic, hue='sex', diag_kind='hist')
plt.suptitle('Scatter Plot Matrix of Glass Dataset')
plt.show()

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
 
print(titanic)
X = titanic.drop(["Survived"], axis=1)
y = titanic['Survived']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = GaussianNB()


model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
url="https://raw.githubusercontent.com/700744362/Machine-Learning/main/Dataset/"
 
glass = pd.read_csv(url+"glass.csv")

glass.reindex( ['id', 'ri', 'na', 'mg', 'al', 'si', 'k', 'ca', 'ba', 'fe', 'glass_type'])

X = glass.drop(["RI"], axis=1)
y = glass['Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)


score = model.score(X_test, y_test)
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)

print('Accuracy:', score)
print('Classification report:\n', report)

X = glass.drop('Type', axis=1)
y = glass['Type']

# split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# print the shapes of the training and testing data
print('Training data shape:', X_train.shape, y_train.shape)
print('Testing data shape:', X_test.shape, y_test.shape)

corr = glass.corr()

  sns.heatmap(corr, annot=True, cmap='coolwarm')
  sns.pairplot(glass, hue='Type', diag_kind='hist')
  plt.suptitle('Scatter Plot Matrix of Glass Dataset')
  plt.show()

#SVM
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report



X = glass.drop('Type', axis=1)
y = glass['Type']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


svm = LinearSVC(random_state=42)

svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)


print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))