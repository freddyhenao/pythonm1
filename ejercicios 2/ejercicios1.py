
print(' Esta Aplicacion calcula la edad promedio de un grupo de N alumnos,   ')
print(' si algun alumno tiene mas de 18 años, se muestra el promedio que se lleva ')
print(' sin contar el alumno de 18 años.  ')
print(' El usuario decide si cierra el programa o lo ejecuta muevamente.  ')



contador=0
suma=0
Edad=1

while Edad !=18:
	Edad= int(input('Digite Edad del estudiante(18 para terminar):'))
	suma +=Edad
	contador += 1

	if contador ==0:
		print('No digito ningun numero.')

	else:

		promedio=suma/contador 
		print('El Promedio de Edad los {} Estudiantes ingresados es igual a {}.'.format(contador, promedio))
