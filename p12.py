import pandas as pd
import numpy as np

df = pd.read_csv("student_result.csv")
print(df)

#To display Student_result file with new column names.
df1 = pd.read_csv("student_result.csv",skiprows = 1,

names = ['Adno','Sex','Name','English','Hindi',

'Maths','Science','SSt','Sanskrit','CA','Perc'])

print("To display Student_result file with new column names")
print(df1)

df2 = pd.read_csv("student_result.csv")
print(df2)

print("To modify the Percentage of student below 40 with NaN value.")
df2.loc[(df2['PERCENTAGE'] <40, 'PERCENTAGE')] = np.nan
print(df2)