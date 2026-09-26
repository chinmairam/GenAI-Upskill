# Task 1
import pandas as pd
df = pd.Series([78, 85, 90, 66, 72])
print(df.values)
print(df.index)
print(df.dtype)
print('First Element:', df[0])
print('Last Two Element:', df[-1:len(df)-3:-1].values)

# Task 2
print('Adding 5 grace marks:')
print(df+5)
print('Subtract 2 marks:')
print(df-2)
print('Multiply all marks by 1.05:')
print(df*1.05)
print('Divide all marks by 2:')
print(df/2)

# Task 3
import numpy as np
print('Maximum Marks:', df.max())
print('Minimum Marks:', df.min())
print('Sum of Marks:', df.sum())
print('Mean Marks:', df.mean())
passed = df.apply(lambda x: x>=70)
print('Passed Students:')
print(passed)
count_passed = np.where(passed == True)
print('Count of Passed Students:', len(count_passed[0]))

# Task 4
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Age': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df_students = pd.DataFrame(students)
print(df_students.head(3))
print(df_students.tail(2))
print(df_students.shape)
print(df_students.columns)

# Task 5
print(df_students.info())
print(df_students.describe())
print(df_students.head())
print(df_students.tail())
df_students.sort_values(by='Marks', ascending=False)
df_students.reset_index(drop=True)

# Task 6
print("Students Marks > 75:")
print(df_students[df_students['Marks'] > 75])
print("Students Subject Math:")
print(df_students[df_students['Subject'] == 'Math'])
print("Students Marks > Avg.Marks:")
print(df_students[df_students['Marks'] > df_students['Marks'].mean()])
print("Failed Students:")
print(df_students[df_students['Marks'] < 70])

# Task 7
print(df_students.groupby('Subject')['Marks'].mean())
print(df_students.groupby('Subject')['Name'].count())
print(df_students.groupby('Subject')['Marks'].max())

# Task 8
print(df_students.plot(kind='bar', title='Student Name Vs Marks', x='Name', y='Marks'))
print(df_students.plot(kind='line', title='Student Name Vs Marks', x='Name', y='Marks'))
print(df_students.plot(kind='hist', title='Student Marks Histogram'))

# Task 9
sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1220, 1500, 900, 2000, 1800]
}
df_sales = pd.DataFrame(sales)
print('Total Revenue:', df_sales['Revenue'].sum())
print('Avg. Daily Revenue:', df_sales['Revenue'].mean())
highest_revenue = df_sales.loc[df_sales['Revenue'].idxmax()]
print(f"The day with the highest revenue is {highest_revenue['Day']}")
above_avg = df_sales[df_sales['Revenue'] > df_sales['Revenue'].mean()]
print('Days with revenue above average:')
print(above_avg)
print(df_sales.plot(kind='bar', x='Day', y='Revenue', title='Sales Data'))