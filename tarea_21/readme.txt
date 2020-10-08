
ENUNCIADO
Un programa que dado un número introducido entre 0,0001 y 0,9999 (no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible. Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.
Programación en lenguaje phyton:
Utilizo un try y un except genérico para controlar la excepción.
Si introduces algún string por ejemplo coma en vez de punto salta la excepción y se acaba el programa.
Pido por consola el numero decimal y valoro si esta entre 0.0001 y 0.9999 lo paso a entero multiplicándolo por 10000 para obtener la fracción primaria .
Uso un for para el recorrido de los números divisibles hasta el numero introducido por consola.
Utilizo un while para que me ejecute el bucle mientras sean divisibles los dos numerador y denominador.
Convierto el numero usuario y el denominador a entero ya que por alguna razón que desconozco al imprimir en pantalla me aparecía un hexadecimal
Imprimo por pantalla la fracción irreducible concatenando en string los números enteros.



