#Exporting Data From Python to CSV
import pandas as pd
df= pd.DataFrame({
    'Name':["Priya","Shan","Arya"],
    'Class':["XI","X","XI"],
    'RollNo':["20","42","10"]
})
#Exporting Data From Python to CSV
df.to_csv('project.csv')
print("File Created!")

#Importing Data From CSV to Python
df2 = pd.read_csv('Book1.csv')
print(df2)

