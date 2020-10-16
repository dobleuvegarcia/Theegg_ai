ENUNCIADO

Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la
Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea
perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa.
Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada
vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de
leche, observando el límite de peso del camión.
1.- Para este propósito tienes que definir las siguientes entradas:
Entrada: Número total de vacas en la zona de Tolosa que están a la venta.
Entrada: Peso total que el camión puede llevar.
Entrada: Lista de pesos de las vacas.
Entrada: Lista de la producción de leche por vaca, en litros por día.
2.- El algoritmo que programes tiene que calcular la siguiente salida:
Salida: Cantidad máxima de producción de leche se puede obtener.

PROGRAMACION EN PHYTON

#creo un diccionario de datos e introduzco los datos de consola al diccionario.
#tambien creo una clave index numerica para el diccionario para saber k numero de vaca a sido seleccionada
#un litro de leche equivale a 1.03 kilos 
#le resto los litros a los kilos de la vaca par ver si produce mucho o solo es carne y poca leche
#guardo la relacion de carne-leche en el cuerpo en un campo del diccionario
#añado el diccionario al array de diccionarios
#ordeno el array por kilos de carne en el cuerpo ascendente siendo los kilos restantes de leche de mayor a meor en el cuerpo
#comparo si es menor los kilos acumulados con el maximo del camion
#sumo los pesos acumulados sin sobrepasar el limite del  camion
#guardo en la variable los acumulados de leche que puede llevar el camion
#enumero  la vaca seleccionada +1 ya que comienza por 0 en el indice del diccionario
#por ultimo muestro los resultados.

lo he comprobado con todas las posibilidades y funciona correctamente
un saludo
