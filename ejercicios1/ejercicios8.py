
print(' Esta Aplicacion compara las edades ingresadas de dos personas  ')
print('Dice si son no iguales ')

edad1 = int(input('Ingrese la edad de la Primera Persona \n'))
print('La Edad De La Primera Persona Ingresada Es: ' + str(edad1))
edad2 = int(input('Ingrese la edad de la Segunda Persona\n'))
print('La Edad De La Segunda Persona Ingresada Es: ' + str(edad2))

igual = edad1==edad2

if igual==True :
		print('Las Personas Tienen Las misma edad')
else:
		print('Las Personas Tienen Diferente edad')	
	


