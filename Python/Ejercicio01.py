# Numeros
2+2 
50 - 5*6 
(50 - 5*6) / 4 
8/5
# Operaciones basicas de matematicas
# como : suma, resta, multiplicacion, division y uso de parentesis.

#division
17 / 3  
17 // 3 # division entera
17 % 3 # resto de division
5 * 3 + 2 

#potencias
5 ** 2 
2 ** 7 
9 ** 0.5
2 ** 1/2 #primero potencia 1 y luego division de 2 
2 ** (1/2) #potencia de 1/2

#uso de variables
ancho = 20 
alto = 5 * 9
ancho * alto # operacion con variables

n #no esta definido 

4 * 3.75 - 1 #operacion con decimal 

iva = 16/100 #variables
precio = 120.5
precio * iva #operacion con variables
precio + _ #precio más iva  
round(_, 2) #redondeo a dos digitos

# Cadenas
'una cadena' #una cadena delimitada por comillas
'La comilla simple \'' 
'La comilla simple \''
"\"Si,\" afirmo"
#(\' ó \") es otra forma de representar comillas simples y dobles.
#cuando se utiliza (\' ó \") las comillas que delimitan a la cadena se cambian
#a simples o dobles dependiendo que comilla se utilizó dentro de la cadena. 

"\"Si,\" afirmo" #mismo concepto
print("\"Si,\" afirmo") #el print quita las comillas que delimitan a la cadena 

c = 'Primera linea.\nSegunda linea.'
c
print(c) #el (\n), imprime con un salto de linea
len(c) # cantidad de elementos de c


print('Una ruta en windows C:\algun\nombre')
print(r'Una ruta en windows C:\algun\nombre') #la r le quita sentido a las (\a y \n)


print("""\
Uso: ssh [OPCIONES] <usuario>@<servidor>
     -v                 muestra informacion adiciona de la conexion
     -p puerto          Puerto para la conexion segura, 22 es el predeterminado
""")
#espacios para hacer apartados o una tipo lista. 

2 * 'goya ' + 'cachun' #worales, operacion con cadenas

'Py' 'thon' #juntar cadenas

text = ('Escribe varias cadenas dentro del par´entesis '
        'para tenerlas unidas')
text #muestra la cadenas juntas

prefijo = 'Py'
prefijo 'thon' 
('un' * 3) 'ium' #errores de sintaxis

prefijo + 'thon' #correccion de sintaxis 

nombre = "Ada"
apellido = "Lovelace"

print(nombre.upper()) #nombre en mayusculas
print(nombre.lower()) #nombre en minusculas
#Ciertos o falsos de nombre.
print(nombre.isalnum()) #caracteres numericos o alfabeticos ?
print(nombre.isalpha()) #todos los caracteres alfabeticos ?
print(nombre.islower()) #todos los caracteres minusculas?
print(nombre.isnumeric()) #todos los caracteres son numericos?
print(nombre.isspace()) #contiene espacios en blanco?
print(nombre.istitle()) #nombres propios (comienzan con mayuscula)?
asignatura = "Taller De Herramientas Computacionales"
print(asignatura.istitle()) #nombre propio ?
print(asignatura.isupper()) #todas mayusculas ?

#ciertos y falsos sobre numero y vocales
#usando conceptos anteriores
numero = "1024"
vocales = "aeiou"
print(numero.isnumeric()) #todos los caracteres del numero son numeros ?
print(vocales.isnumeric()) 

#ciertos y falso sobre pelicula, libro y poema
#usando conceptos anteriores 
pelicula = "2001: UNA MENTE BRILLANTE"
libro = "Cinco Ecuaciones Que CAmbiaron Al Mundo"
poema = "nadie en oro se convertirá:"

print(pelicula.islower())
print(pelicula.isupper())

print(libro.istitle())
print(libro.isupper())

print(poema.istitle())
print(poema.islower())

cadena = "Linux es un kernel."
" ".join(cadena) #espacia a la cadena y cambia comillas a simples
print(cadena) #imprime la cadena
print(" ".join(cadena)) #espacia la cadena sin comillas porque es con print 

print("".join(reversed(cadena))) #imprime cadena revertida 

# https://docs.python.org/3/tutorial/introduction.html#strings
# https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
