

import pandas as pd
import numpy as np

data = pd.read_csv('NSL-KDD/KDDTest+.txt', delimiter= ',', header = None)
print(data.head())
print(data.shape)
print(data.dtypes)

# for col in data.columns:
#     print('\t%s: %d' % (col,data[col].isna().sum()))

