import pandas as pd
ser_length = int(input("Enter the length of the series: "))
data = []
for i in range(ser_length):
    val = int(input("Enter a val:"))
    data.append(val)
    ser = pd.Series(data)
print(ser.head(3))