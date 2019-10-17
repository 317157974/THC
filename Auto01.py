C = [0]*43
C[21] = 1
E = []
n = len(C)
for i in range(n):
    if C[i] == 1:
        E.append(i)
print(E)
Y = [21]*len(E)

    
P = [0]*12
P[3] = 1
P[4] = 1
P[9] = 1
L = []
m = len(P)
for j in range(m):
    if P[j] == 1:
        L.append(j)
print(L)
M = [3]*len(L)
        
