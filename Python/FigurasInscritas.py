from math import sin, cos, sqrt, pi

import matplotlib.pyplot as plt
import numpy as np

r = 5
l = 10
a = 2*pi/l

x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)
x6 = r*cos(6*a)
x7 = r*cos(7*a)
x8 = r*cos(8*a)
x9 = r*cos(9*a)
x10 = r*cos(10*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)
y6 = r*sin(6*a)
y7 = r*sin(7*a)
y8 = r*sin(8*a)
y9 = r*sin(9*a)
y10 = r*sin(10*a)

x = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x1])
y = np.array([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y1])


print("""Las coordenadas del decágono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
F = (%5.2f,%5.2f)
G = (%5.2f,%5.2f)
H = (%5.2f,%5.2f)
I = (%5.2f,%5.2f)
J = (%5.2f,%5.2f)
"""%(r, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10,y10))

circulo = plt.Circle((0,0), radius=r, color='g')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='b')
ax.add_patch(circulo)

plt.legend()
plt.show()


r = 5
l = 9
a = 2*pi/l


x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)
x6 = r*cos(6*a)
x7 = r*cos(7*a)
x8 = r*cos(8*a)
x9 = r*cos(9*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)
y6 = r*sin(6*a)
y7 = r*sin(7*a)
y8 = r*sin(8*a)
y9 = r*sin(9*a)

x = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x1])
y = np.array([y1,y2,y3,y4,y5,y6,y7,y8,y9,y1])


print("""Las coordenadas del eneágono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
F = (%5.2f,%5.2f)
G = (%5.2f,%5.2f)
H = (%5.2f,%5.2f)
I = (%5.2f,%5.2f)
"""%(r, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9))

circulo = plt.Circle((0,0), radius=r, color='g')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='b')
ax.add_patch(circulo)

plt.legend()
plt.show()


r = 5
l = 8
a = 2*pi/l


x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)
x6 = r*cos(6*a)
x7 = r*cos(7*a)
x8 = r*cos(8*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)
y6 = r*sin(6*a)
y7 = r*sin(7*a)
y8 = r*sin(8*a)

x = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x1])
y = np.array([y1,y2,y3,y4,y5,y6,y7,y8,y1])


print("""Las coordenadas del octágono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
F = (%5.2f,%5.2f)
G = (%5.2f,%5.2f)
H = (%5.2f,%5.2f)
"""%(r, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8))

circulo = plt.Circle((0,0), radius=r, color='g')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='b')
ax.add_patch(circulo)

plt.legend()
plt.show()

r = 5
l = 7
a = 2*pi/l


x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)
x6 = r*cos(6*a)
x7 = r*cos(7*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)
y6 = r*sin(6*a)
y7 = r*sin(7*a)

x = np.array([x1,x2,x3,x4,x5,x6,x7,x1])
y = np.array([y1,y2,y3,y4,y5,y6,y7,y1])


print("""Las coordenadas del heptágono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
F = (%5.2f,%5.2f)
G = (%5.2f,%5.2f)
"""%(r, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7))

circulo = plt.Circle((0,0), radius=r, color='g')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='b')
ax.add_patch(circulo)

plt.legend()
plt.show()

r = 5
l = 6
a = 2*pi/l


x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)
x6 = r*cos(6*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)
y6 = r*sin(6*a)

x = np.array([x1,x2,x3,x4,x5,x6,x1])
y = np.array([y1,y2,y3,y4,y5,y6,y1])


print("""Las coordenadas del hexágono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
F = (%5.2f,%5.2f)
"""%(r, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))

circulo = plt.Circle((0,0), radius=r, color='g')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='b')
ax.add_patch(circulo)

plt.legend()
plt.show()

r = 5
l = 5
a = 2*pi/l


x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)

x = np.array([x1,x2,x3,x4,x5,x1])
y = np.array([y1,y2,y3,y4,y5,y1])


print("""Las coordenadas del pentagono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
"""%(r, x1, y2, x2, y2, x3, y3 ,x4 ,y4 ,x5 ,y5))

circulo = plt.Circle((0,0), radius=r, color='g')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='b')
ax.add_patch(circulo)

plt.legend()
plt.show()
