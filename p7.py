import pandas as pd
s = {
    'Invoice': [1, 2, 3, 4, 5, 6, 7],
    "Product":
    ['TV', 'Fridge', 'AC', 'Speaker', 'Headset', 'Monitor', 'Washing Machine'],
    'Quantity': [1, 2, 1, 1, 2, 2, 1],
    'Price': [20000, 60000, 40000, 100000, 34000, 3000, 97000]
}
a=pd.DataFrame(s)
print(a['Price'].describe().round(2))