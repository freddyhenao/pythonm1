 # Conversion de Grados Celsius a Fahrenheit
print('Esta Aplicacion Convierte los Grados Centigrados a Fahrenheit:\n')

celsius = float(input('Ingrese Grados Celsius\n'))
print('Los Grados Celsius Ingresados son:\n' + str(celsius))

fahrenheit = (celsius * 9)/5 + 32
print('Equivalen a:'+ ' ' + str(fahrenheit) + '°F')
