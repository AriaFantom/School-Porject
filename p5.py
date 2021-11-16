import pandas as pd 
data={'Name':['Aman','Rohit','Deepika','Aman','Deepika','Sohit','Geeta'], 
'Sales':[8500,4500,4600,8500,4600,9600,8400]} 
sales=pd.DataFrame(data) 

duplicated = sales[sales.duplicated(keep=False)]
print("Duplicate Row:\n",duplicated)