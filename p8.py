import pandas as pd
import numpy as np
def fl_ser():
    n = np.arange(21,32,1.5)
    s = pd.Series(n)
    print(s)
fl_ser()