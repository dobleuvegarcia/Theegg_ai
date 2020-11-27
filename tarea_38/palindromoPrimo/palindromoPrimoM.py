import itertools
def primo(num):
	p=num
	for i in range(2,num):
		while num%i==0:
			num=num/i
	if num==1:
		return(False)
	else:
		return(p)


def PalindromoPrimo(p_may):
	p=p_may
	invert=str(p_may)
	busc_palindromo=invert[::-1]
	if invert==busc_palindromo:
		return(p)
	else:
		return(False)

def PalindromoYprimo(num):
	if num<=1000000:
		while PalindromoPrimo(num)==False or primo(num)==False:
			num+=1

	return(num)


		
n=int(input("Introduce un numero:  "))
pm=0
n+=1
#while pm==0 and n<=1000000:
p_p=PalindromoYprimo(n)

if n>=1000000:
	print("no hay numeros primos palindromos superiores")
	print("Numero primo palindromo : ",p_p," supera a 1000000")
else:
	print(p_p)


