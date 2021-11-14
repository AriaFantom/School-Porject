import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('data.csv')
print(df)
slices= (df['Population'].head(6))
states= (df['States'].head(6))
cols=['m','c','g','b','r','gold']
exp=[0,0,0,0,0,0.1]
plt.pie(slices, labels=states,colors=cols,startangle=90, explode=exp,shadow=True,autopct='%.1f%%')
plt.title('2011 Cencus Data')
plt.legend()
plt.show()