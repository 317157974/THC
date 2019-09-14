#
# Dylan Ramirez Hernandez
# python 3.7.3
# 10/09/2019
# 13/09/2019
#
# Calcular el trabajo empleado de una bomba que sube 1 m^3 de agua a un altura de 30 m en 15 min.
# Datos: peso especifico del agua = 9800 N/m³
# Con la formula de trabajo W = |F|*|d|*Cos(ángulo) , con |F| en Newtons, |d| en metros y el resultado en Jules (J).
# Para este problema , el Cos (0) = 1, por lo tanto no lo escribo en el producto porque no afecta el resultado. 
# Ejemplo de cadena multilinea que nos sirve en un principio como comentario 
x = 9800
k = 30 
w = k*x
print(w)
print("""El trabajo de una bomba
que sube 1 m³ de agua a una altura de k=%g
y una fuerza x=%f"""%(k,x)) 
print("""El trabajo de una bomba\nque sube 1 m³ de agua a una altura de k=%g\ny una fuerza x=%g"""%(k,x)) 
