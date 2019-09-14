#
# Dylan Ramirez Hernandez
# python 3.7.3
# 12/09/2019
# 13/09/2019
#
# Calcular el trabajo empleado de una bomba que sube 1 m^3 de agua a un altura de 30 m en 15 min.
# Datos: peso especifico del agua = 9800 N/m^3
# Con la formula de trabajo W = |F|*|d|*Cos(ángulo) , con |F| en Newtons, |d| en metros y el resultado en Jules (J).
# Para este problema , el Cos (0) = 1, por lo tanto no lo escribo en el producto porque no afecta el resultado. 
# Ejemplo no recomendable por ser muy largo y no tan practico
# pero se llega al mismo resultado
FUERZA= 9800
DISTANCIA= 30
Coseno_de_0= 1
TrabajoEmpleadoDeBomba= FUERZA*DISTANCIA*Coseno_de_0
print(TrabajoEmpleadoDeBomba)
 
