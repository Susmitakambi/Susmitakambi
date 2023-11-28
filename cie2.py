# -*- coding: utf-8 -*-
"""CIE2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17hjqfH8gBEth3g8hQg48f9i8NtKpcjOQ
"""

import pandas as pd
import numpy as np
df=pd.read_csv('/content/titanic (4).csv')
df.head()

df.describe()

df.info()

df['Age'].unique()

df.duplicated().sum()

df.isnull().sum()

import pandas as pd
df=pd.read_csv('/content/titanic (4).csv')
age_mean=df['Age'].mean()
age_median=df['Age'].median()
age_mode=df['Age'].mode()
print('mean of age',age_mean)
print('median of age',age_median)
print('mode of age',age_mode)
print('_________________________________')
Fare_mean=df['Fare'].mean()
Fare_median=df['Fare'].median()
Fare_mode=df['Fare'].mode()
print('mean of Fare',Fare_mean)
print('median of Fare',Fare_median)
print('mode of Fare',Fare_mode)
print('________________________________')

import pandas as pd
data = pd.read_csv('/content/titanic (4).csv')
null_age = data['Age'].isnull().sum()
null_fare = data['Fare'].isnull().sum()
mean_age = data['Age'].mean()
mean_fare = data['Fare'].mean()
data['Age'].fillna(mean_age, inplace=True)
data['Fare'].fillna(mean_fare, inplace=True)
null_age_after = data['Age'].isnull().sum()
null_fare_after = data['Fare'].isnull().sum()
print(f"Null values in Age column before",null_age)
print(f"Null values in Age column after:",null_age_after)
print(f"Null values in Fare column before",null_fare)
print(f"Null values in Fare column after",null_fare_after)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv('/content/titanic (4).csv')
from scipy import stats
z_scores=np.abs(stats.zscore(df['Age']))
threshold=3
outlires=df['Age'][z_scores > threshold]
sns.boxplot(df['Age'],color='skyblue')
plt.title('boxplot of fare column')
plt.xlabel('Age')
plt.show()
print('outliers')

import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv('/content/titanic (4).csv')
df['Survived'].replace({0:'not Survived',1:'Survived'},inplace=True)
Survived_counts=df['Survived'].value_counts()
sns.countplot(x='Survived',hue='Pclass',data=df)
plt.show()
df.head()

df.describe()

data.isnull().sum()