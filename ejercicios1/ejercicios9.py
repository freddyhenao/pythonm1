
print(' Esta Aplicacion calcula la cantidad de meses transcurridos desde la   ')
print('fecha de nacimiento de un usuario ')


añoNac = int(input('Ingrese el año en el que ud nació:\n'))
mesNac= int(input('Ingrese el mes en el que ud nació 1 al 12:\n'))
añoActual = int(input('Ingrese el año en el que esta actualmente:\n'))
mesActual= int(input('Ingrese el mes en el que esta actualmenta 1 al 12:\n'))

añoTotal = añoActual - añoNac-1
mesTotal = (12- mesNac)+(mesActual)+(12*añoTotal)
print('En este momento ud tiene: ' + str(añoTotal) + ' años' + ' y han transcurrido ' + str(mesTotal) + ' meses desde entonces...')
