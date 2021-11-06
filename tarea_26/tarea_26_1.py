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
x=dias
y=data["Araba: Positiboa / Álava: Positivo "]
x = np.arange(0, registro)
plt.plot(x, y,label='Álava: Positivo')
x1=dias
y1=data["Bizkaia: Positiboa / Bizkaia: Positivo "]
x1 = np.arange(0, registro)
plt.plot(x1, y1,label='Bizkaia: Positivo')
x2=dias
y2=data["Gipuzkoa: Positiboa / Gipuzkoa: Positivo "]
x2 = np.arange(0, registro)
plt.plot(x2, y2,label='Gipuzkoa: Positivo')
xt=dias
yt=data["EAE: Positiboa / CAE: Positivo "]
xt = np.arange(0, registro)
plt.plot(xt, yt,label='CAE: Positivo')
plt.xlabel('dias')
plt.ylabel('nº contagios')

media=np.mean(data["EAE: Positiboa / CAE: Positivo "])
moda=stat.mode(data["EAE: Positiboa / CAE: Positivo "])
mediana=stat.median(data["EAE: Positiboa / CAE: Positivo "])
varianza=np.var(data["EAE: Positiboa / CAE: Positivo "])
desviacion_estandar=np.std(data["EAE: Positiboa / CAE: Positivo "])
rango=np.max(data["EAE: Positiboa / CAE: Positivo "]-np.min(data["EAE: Positiboa / CAE: Positivo "]))
plt.title('nº de contagios por '+str(registro)+' dias(01/03/2020 hasta 12/05/2020)\n'
	+'CAE Media:'+str(media)+"  "
	+'CAE Moda: '+str(moda)+"  "
	+'CAE Mediana: '+str(mediana)+"\n"
	+'CAE Varianza:'+str(varianza)+"  "
	+'CAE Desviacion Estandar: '+str(desviacion_estandar)+"  "
	+'CAE Rango: '+str(rango)+"\n"
		,fontsize = 7)


plt.legend()
plt.savefig('comunidades_autonomas_covid.png')
plt.show()
