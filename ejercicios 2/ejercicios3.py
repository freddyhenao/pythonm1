
print(' Esta Aplicacion calcula la estatura promedio de un grupo de personas,  ')
print(' cuyo numero de mienbros se desconoce, el ciclo debe efectuarce siempre')
print(' y cuando se tenga una estatura registrada')



contador=0
cont=0
suma=0
estatura=1


while estatura !=0:
	estatura= float(input('Digite Estatura del estudiante( 0 para terminar):'))
	suma +=estatura
	contador += 1

	if estatura ==0:
		promedio=suma/(contador-1) 
		cont=contador-1
		print('El Promedio de Estatura las {} Persona ingresadas es igual a {}.'.format(cont, promedio))

	else:
		promedio=suma/contador 
		print('El Promedio de Estatura las {} Persona ingresadas es igual a {}.'.format(contador, promedio))



