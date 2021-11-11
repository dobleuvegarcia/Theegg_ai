import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('26_2.csv',encoding="ISO-8859-1", header=0, sep = ';')
registro=len(data)
#print(registro)
data_filtrado=data.fillna(0)
#print(data_filtrado.head(registro))

for i in range(1,5):
	
	if i==2:  
		xh = np.arange(0, registro)
		yh=data_filtrado["Gizonak: positiboak / Hombres: positivos"]
		plt.plot(xh, yh, label='Hombres: positivos')
		xh = np.arange(0, registro)
		ym=data_filtrado["Emakumeak: positiboak / Mujeres: positivos"]
		plt.plot(xh, ym, label='Mujeres: positivos')
		xpt = np.arange(0, registro)
		y_t=data_filtrado["Guztira p / Total p"]
		plt.plot(xpt, y_t, label='Total')
		plt.xlabel('edad')
		plt.ylabel('nº contagios')
		plt.legend()

	elif i==3:
		xhf = np.arange(0, registro)
		yhf=data_filtrado["Gizonak: hildakoak / Hombres: fallecimientos"]
		
		plt.plot(xhf, yhf,label='Hombres: fallecimientos')
		
		xmf = np.arange(0, registro)
		ymf=data_filtrado["Emakumeak: hildakoak / Emakumeak: fallecimientos"]
		
		plt.plot(xmf, ymf,label='Emakumeak: fallecimientos')
		xpt = np.arange(0, registro)
		y_m_t=data_filtrado["Guztira f/ Total f"]
		plt.plot(xpt, y_m_t, label='Total')
		plt.xlabel('edad')
		plt.ylabel('nº contagios')
		plt.legend()

	elif i==4:
		xph = np.arange(0, registro)
		y_h=data_filtrado["Gizonak: hilgarritasuna / Hombres: letalidad"]
		plt.plot(xph, y_h, label=' Hombres: letalidad')
		y_m=data_filtrado["Emakumeak: hilgarritasuna / Mujeres: letalidad"]
		plt.plot(xph, y_m, label='Mujeres: letalidad')
		y_t_p=data_filtrado["Guztira l / Total l"]
		plt.plot(xph, y_t_p, label='Media')
		plt.xlabel('edad')
		plt.ylabel('porcentaje de contagios')
		plt.legend()
	plt.subplot(2, 2,i)



plt.savefig('positivos_fallecimientos_letalidad.png')	
plt.show()	

		



		

		






