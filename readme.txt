
ENUNCIADO
Un programa que dado un n�mero introducido entre 0,0001 y 0,9999 (no m�s de 4 cifras decimales), obtenga y muestre la correspondiente fracci�n irreducible. Por ejemplo, el n�mero 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracci�n irreducible es 1/4, que est� formada por un numerador y un denominador que son primos entre s�.
Programaci�n en lenguaje phyton:
Utilizo un try y un except gen�rico para controlar la excepci�n.
Si introduces alg�n string por ejemplo coma en vez de punto salta la excepci�n y se acaba el programa.
Pido por consola el numero decimal y valoro si esta entre 0.0001 y 0.9999 lo paso a entero multiplic�ndolo por 10000 para obtener la fracci�n primaria .
Uso un for para el recorrido de los n�meros divisibles hasta el numero introducido por consola.
Utilizo un while para que me ejecute el bucle mientras sean divisibles los dos numerador y denominador.
Convierto el numero usuario y el denominador a entero ya que por alguna raz�n que desconozco al imprimir en pantalla me aparec�a un hexadecimal
Imprimo por pantalla la fracci�n irreducible concatenando en string los n�meros enteros.



