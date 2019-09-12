# 
# Dylan Ramirez Hernandez
# python 3.7.3
# 10/09/2019, 16/09/2019
# 12/09/2019, 17/09/2019
#
# Calcula la posicion de una pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos
# cadena multilinea pero toma el trabajo de un comentario
v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print(y)
print('En el tiempo t=%g segundos, la altura de la pelota es %.2f metros'%(t,y))
print("""
En t=%g segundos, la pelota con
velocidad inicial v0=%.3E m/s
se encuentra a %.2f metros de altura""" % (t,v0, y))
print("""En t=%g segundos la pelota con\nvelocidad inicial v0=%.3E m/s\nse encuentra a %.2f metros de altura"""%(t,v0, y))
    

