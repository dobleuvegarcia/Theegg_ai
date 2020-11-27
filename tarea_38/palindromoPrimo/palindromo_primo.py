import itertools
def primo(num):
	p=num
	for i in range(2,num):
		while num%i==0:
			num=num/i
	if num==1:
		return(0)
	else:
		return(p)
def buscarPrimoMayor(num):
	bp=primo(num)
	while bp==0:
		num=num+1
		bp=primo(num)
	return(bp)
def PalindromoPrimo(p_may):
	invert=str(p_may)
	busc_palindromo=invert[::-1]
	if invert==busc_palindromo:
		return(p_may)
	else:
		return(0)
		

n=int(input("Introduce un numero:  "))
pm=0
while pm==0 and n<=1000000:
	bpm=buscarPrimoMayor(n)
	pm=PalindromoPrimo(bpm)
	if pm==0:
		n=bpm+1
print("Numero primo palindromo : ",pm)
if n>=1000000:
	print("no hay numeros primos palindromos superiores")