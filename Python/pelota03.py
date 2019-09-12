#
# Dylan Ramirez Hernandez
# python 3.7.3
# 12/09/2019
#
# Calcula la posicion de una pelota con una velocidad inicial
# de 5 m/s y un timpo de 0.6 segundos utiliazando nombres de variables
# descriptivos muuuy largos
# A pesar de que funciona esto no es recomendable.
# Aunque nos de el mismo resultado no es practico por set tan largo

velocidad_inicial = 5
constante_de_gravedad = 9.81
TIEMPO = 0.6
PosicionVerticalDeLaBola = velocidad_inicial*TIEMPO - 0.5*constante_de_gravedad*TIEMPO**2
print(PosicionVerticalDeLaBola) 
