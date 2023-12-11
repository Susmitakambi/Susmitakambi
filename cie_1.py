# -*- coding: utf-8 -*-
"""CIE 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/155wn8Ezk7BQvdUMYuwKJz6roYHoWmLPY
"""

import pandas as pd
mtcars=pd.read_csv("/content/mtcars.csv")
mtcars

plt.figure(figsize=(8, 6))
plt.hist(data['mpg'], bins=10, edgecolor='k', color='pink')
plt.title('Histogram of MPG (Miles per gallon)')
plt.xlabel('MPG')
plt.ylabel('Frequency')

plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(data['wt'], data['mpg'], color='black', marker='o')
plt.title('Scatter Plot: Car Weight vs. MPG')
plt.xlabel('Car Weight')
plt.ylabel('MPG')

plt.show()

transmission_counts = data['am'].value_counts()
plt.figure(figsize=(8, 6))
transmission_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency Distribution of Transmission Type')
plt.xlabel('Transmission Type (0 = Automatic, 1 = Manual)')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot(data['mpg'], vert=False, notch=True, patch_artist=True, boxprops=dict(facecolor='red'))
plt.title('Box and Whisker Plot of MPG')
plt.xlabel('MPG')

plt.show()

import pandas as pd
series_a = pd.Series([1, 2, 3, 4, 5])
series_b = pd.Series([2, 4, 6, 8, 10])
common_items = series_a[series_a.isin(series_b)]
common_series = pd.Series(common_items)
print(common_series)