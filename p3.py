import pandas as pd

data = [['CAR', 'Maruti', 1000000],
        ['AC', 'Hitachi', 55000],
        ['AIRCOLLER', 'Bajaj', 12000],
        ['WASHING MACHINE', 'Sumsung', 15000],
        ['CAR', 'Ford', 7000000],
        ['AC', 'Haier', 45000],
        ['AIRCOLLER', 'Symphony', 20000],
        ['WASHING MACHINE', 'LG', 25000]]

Col = ['category', 'itemname', 'expenditure']

qrtsales = pd.DataFrame(data, columns=Col)
print (qrtsales)