import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
data=pd.read_csv('26_2.csv',encoding="ISO-8859-1", header=0, sep = ';')
registro=len(data)
print(registro)
print(data.head(registro))