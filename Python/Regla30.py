n = 43
celulas = [0]*n
celulas[n//2] = 1

def Regla30(a,i,s):
    if [a,i,s] == [1,0,0] or [a,i,s] == [0,1,0] or [a,i,s] == [0,1,1] or [a,i,s] == [0,0,1]:
        resultado = 1
    else:
        resultado = 0
    return(resultado)
print(celulas)

ne = []
for i in range(43):
    ne.append(Regla30(celulas[i-1],celulas[i],celulas[(i+1)%43]))


celulas = ne.copy()
print(celulas)
for j in range(22):
    ne = []
    for i in range(43):
        ne.append(Regla30(celulas[i-1],celulas[i],celulas[(i+1)%43]))
    celulas = ne.copy()
    print(celulas)
        
