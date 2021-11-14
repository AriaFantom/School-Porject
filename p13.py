import pandas as pd 
import matplotlib.pyplot as plt


subject = ['Physic','Chemistry','Mathematics', 'Biology','Computer']
marks =[40,75,80,78,82]

plt.plot(subject,marks,'r',marker ='*')    

plt.title('Marks Scored')

plt.xlabel('SUBJECT')          

plt.ylabel('MARKS')            
plt.show()