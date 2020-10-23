import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("HELLO THIS IS PYTHON")
# Pandas : Multiindex : https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
iterables=[['shirt', 'pants'], ['red', 'blue', 'green']]
index = pd.MultiIndex.from_product(iterables, names=['item','color'])
pd.Series(np.random.randn(6), index=index)
# MatplotLib : Simple plotting here https://matplotlib.org/tutorials/introductory/pyplot.html
t = np.arange(0, 5, 0.2)
plt.title(r'$\sigma_i=?$')
plt.plot(t, t, 'r', t, t*2, 'bs', t, t**3, 'g^')