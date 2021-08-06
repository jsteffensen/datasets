import numpy as np
import pandas as pd

dataframe = pd.read_csv('C:/Users/root/workspace/machine-learning-datasets/crypto_btc_usd_10_sec.csv', sep=',')

dataframe['Volume_up'] = dataframe.Volume > dataframe.Volume.shift(1)

print(dataframe)