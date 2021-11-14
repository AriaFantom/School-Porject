import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("student_result.csv")

plt.hist([df['ENG'],df['HINDI'],df['MATHS'],df['SCIENCE'],df['SSC'],df['SANSK'],df['CA']],color=['red', 'yellow', 'blue','green','orange','black','pink'])
plt.title('Number of Students against Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.legend(['English', 'Hindi', 'Maths','Science','SSt','Sanskrit','CA'])
plt.show()

y = ['ENGG','HINDI','MATHS','SCIENCE','SSC','SANSK','CA']
width = [df['ENG'].max(),df['HINDI'].max(),df['MATHS'].max(),df['SCIENCE'].max(),df['SSC'].max(),df['SANSK'].max(),df['CA'].max()]

plt.figure(figsize = (12,2))
plt.barh(y = y, width = width)
plt.title('Average Scores')
plt.xlabel('Average Score')
plt.ylabel('Subjects')
for i,v in enumerate(width):
    plt.text(v, i, " "+str(round(v,2)), color='blue', va='center', fontweight='bold')
plt.show()