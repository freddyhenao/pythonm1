

lista1= print(list(filter((lambda x: x%2!=1),range(1,101))))  # pares

lista2=print(list(filter((lambda x: x%2!=0),range(1,101))))  # impares 
numero = 100
cont=0
mult = 1
for i in range(1, numero + 1):
            cont=cont+1
            mult= mult * cont
            print('multiplicacion {}.'.format(mult))