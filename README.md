# Machine Learning Datasets

Collections of datasets to use with machine learning examples

To keep filesizes < 50Mb per Github recommendation use:

```
import numpy as np
import pandas as pd

dataframe = pd.read_csv('C:/Users/root/workspace/machine-learning-datasets/crypto_eth_usd_10_sec.csv', sep=',')
dataframe = dataframe[:650000]
dataframe.to_csv(r'C:/Users/root/workspace/machine-learning-datasets/crypto_eth_usd_10_sec.csv')
```
