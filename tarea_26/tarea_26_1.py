import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import statistics as stat
data=pd.read_csv('26_1.csv',encoding="ISO-8859-1", header=0, sep = ';')
data_copy=data.copy
registro=len(data)
data.head(registro)
data.describe()
pd.to_datetime(data["Baliozkotze-data / Fecha Validacion"],dayfirst='True').dt.strftime("%y%m%d")
dias=(data["Baliozkotze-data / Fecha Validacion"].astype('datetime64[D]').dt.dayofyear)
x=data["Baliozkotze-data / Fecha Validacion"]
y=data["Araba: Positiboa / Álava: Positivo "]
x = np.arange(0, registro)
plt.plot(x, y,label='Álava: Positivo')
x1=data["Baliozkotze-data / Fecha Validacion"]
y1=data["Bizkaia: Positiboa / Bizkaia: Positivo "]
x1 = np.arange(0, registro)
plt.plot(x1, y1,label='Bizkaia: Positivo')
plt.xlabel('dias')
plt.ylabel('nº contagios')
plt.title('nº de contagios por '+str(registro)+' dias(01/03/2020 hasta 12/05/2020)\n'
	+'CAE Media:'+str(np.mean(data["EAE: Positiboa / CAE: Positivo "]))+"  "
	+'CAE Moda: '+str(stat.mode(data["EAE: Positiboa / CAE: Positivo "]))+"  "
	+'CAE Mediana: '+str(stat.median(data["EAE: Positiboa / CAE: Positivo "]))+"\n"
	+'CAE Varianza:'+str(np.var(data["EAE: Positiboa / CAE: Positivo "]))+"  "
	+'CAE Desviacion Estandar: '+str(np.std(data["EAE: Positiboa / CAE: Positivo "]))+"  "
	+'CAE Rango: '+str(np.max(data["EAE: Positiboa / CAE: Positivo "])-np.min(data["EAE: Positiboa / CAE: Positivo "]))+"\n"
		,fontsize = 7)
x2=data["Baliozkotze-data / Fecha Validacion"]
y2=data["Gipuzkoa: Positiboa / Gipuzkoa: Positivo "]
x2 = np.arange(0, registro)
plt.plot(x2, y2,label='Gipuzkoa: Positivo')

xt=data["Baliozkotze-data / Fecha Validacion"]
yt=data["EAE: Positiboa / CAE: Positivo "]
xt = np.arange(0, registro)
plt.plot(xt, yt,label='CAE: Positivo')

plt.legend()
plt.savefig('comunidades_autonomas_covid.png')
plt.show()

