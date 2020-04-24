
print('Esta Aplicacion Calcula el numero de vueltas necesarias para recorrer un km ')
print('Sabiendo Sabiendo que el Diametro de la llanta es de 50cm ')
print('y ecuacion para el calcualar el perimetro de una Circunfenrecia es L=2 *PI* r')
print('L: Longitude del perimetro')
print('PI: Constante de relacion de la circunferencia y el radio de la misma  equivale a 3.1416 ')

pi = 3.1416
radio = 25
llanta = (2 * pi) * 25
vueltas = 100000 / llanta # 100000 es la conversion de km a cm
print('El numero de vueltas de la llanta son '+str(vueltas))