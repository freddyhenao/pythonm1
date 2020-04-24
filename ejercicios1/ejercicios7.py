# # Longitud de la sombra de un edificio

print(' Esta Aplicacion Calcula la Longitud de la sombra de un edificio ')
print('Conociendo la altura de 20Mts y el angulo del sol con el suelo 22 Grados')

Altura  = 20
Angulo = 22 # tan 22°
tangente = 0.40402623
longitud = Altura / tangente

print('La longitud de la sombra del edificio en Mtros: '+ str(longitud)+'mts')

