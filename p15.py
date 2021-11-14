import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

s=['1st','2nd','3rd']
sc=[98,89,97]
com=[96,99,92]
hum=[92,87,95]
a = np.arange(len(s))
plt.bar(a, sc, label='Science', width=0.25, color='green')
plt.bar(a+.25, com, label='Commerce', width=0.25, color='red')
plt.bar(a+.50, hum, label='Humanities', width=0.25, color='gold')
plt.xticks(a, s)
plt.xlabel('Position')
plt.ylabel('Percentage')
plt.title('Result Analysis')
plt.legend()
plt.show()