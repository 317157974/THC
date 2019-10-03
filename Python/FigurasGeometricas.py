l = 2

a1 = 0
a2 = 0
b1 = 0 + l
b2 = 0
c1 = 0
c2 = 0 + l
d1 = 0 + l
d2 = 0 + l

print("""Coordenadas de un cuadrado de lado dos, con un
vertice en el origen y inscrito en el primer cuadrante.

A = (%g, %g)
B = (%g, %g)
C = (%g, %g)
D = (%g, %g)"""%(a1,a2,b1,b2,c1,c2,d1,d2))

l = 2
l2 = 6

e1 = 0
e2 = 0
f1 = 0 + l2
f2 = 0
g1 = 0
g2 = 0 + l
h1 = 0 + l2
h2 = 0 + l

print("""Coordenadas de un rectangulo de base seis y altura de dos,
con un vertice en el origen y incrito en el primer cuadrante.

E = (%g, %g)
F = (%g, %g)
G = (%g, %g)
H = (%g, %g)"""%(e1,e2,f1,f2,g1,g2,h1,h2))

l = 2

i1 = 0
i2 = 0
j1 = 0 + l
j2 = 0
k1 = 0 + l
k2 = 0 + l
m1 = 2*l
m2 = 0 + l

print("""Coordenadas de un paralelogramo de base dos,
con un vertice en el origen y inscrito en el primer cuadrante.

I = (%g, %g)
J = (%g, %g)
K = (%g, %g)
M = (%g, %g)"""%(i1,i2,j1,j2,k1,k2,m1,m2))

from math import sqrt

l = 2

n1 = 0
n2 = 0
p1 = 0 + l
p2 = 0
q1 = l/2
q2 = l * (sqrt(3)/2) # sin(60°)= sqrt(3)/2


print("""Coordenadas de un triangulo equilatero
de base dos, con un vertice en el origen y inscrito en el primer cuadrante.

N = (%g, %g)
P = (%g, %g)
Q = (%g, %1.2f)"""%(n1,n2,p1,p2,q1,q2))
