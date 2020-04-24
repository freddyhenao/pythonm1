

print('Este programa calcula la conversion de Dolares a Pesos Colombianos')
TRM = float(input('Ingrese la TRM del Hoy\n'))

Dolares  = float(input('Ingrese la cantidad de dolares\n'))
print('La cantidad de dolares es:\n' + str(Dolares))

Pesos = Dolares * TRM
print('El Valor de Su US$ en Pesos Colombianos para hoy es:\n' + str(Pesos))
