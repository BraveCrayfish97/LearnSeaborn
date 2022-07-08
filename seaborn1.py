import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sbn
df = pd.read_csv('flights.csv')
#df = sbn.load_dataset('flights')
print(sbn.relplot(x='passengers', y = 'month', data = df))
