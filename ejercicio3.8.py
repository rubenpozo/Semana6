print("Claculo de indice de masa corporal")
p=float(input("Ingrese su peso en kilogramos"))
a=float(input("Ingrese su altura en metros"))

def imc(p,a):
	calculo=p/(a*a)
	c=round(calculo,2)
	print("su indice de masa corporal es: "+ str(c))

	if c<16.00:
		print("Infrapeso:Delgadez Severa")
	elif 16.00<c<16.99:
		print("Infrapeso:Delgadez Moderada")
	elif 17.00<c<18.49:
		print("Infrapeso:Delgadez Aceptable")
	elif 18.50<c<24.99:
		print("peso normal")
	elif 25.00<c<29.99:
		print("Sobrepeso")
	elif 30.00<c<34.99:
		print("Obeso:Tipo I")
	elif 35.00<c<40.00:
		print("Obeso tipo II")
	else:
		print("Obeso tipo III")

imc(p,a)