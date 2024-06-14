import random
##definimos verticesFalse

#_______________________________________________________________________Grafo_____________________________________________________

class Vertice:
    def __init__(self,i):
        self.id = i
        self.vecinos = []
        self.lleno = False
    def agregaVecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            if len(self.vecinos)==5:
                self.lleno=True

#_______________________________________________________________________Funciones________________________________________________

def agregarid(arr):
    ideses=[]
    for i in range(len(arr)):
        ideses.append(getattr(arr[i],"id"))
    return(ideses)

def castigados(obj, b, a):
    for i in range(len(a)):
        if obj==(getattr(a[i],"id")):
            b.append(a[i])
def p_universo(cast, a, universo):
    for i in range(len(a)):
        if universo==(getattr(a[i],"id")):
            for j in range(len(cast)):
                if a[i]==cast[j]:
                    return False
                else:
                    return True
def eliminar(a, e):
    for i in range(len(a)-1):
        vecitp = getattr(a[i],"vecinos")
        for j in range(len(vecitp)-1):
            if getattr(vecitp[j],"id") == e:
                vecitp.pop(j)
                setattr(a[i],"vecinos",vecitp)
            else:
                continue
        for i in range(len(a)):
            if(getattr(a[i], "id"))==e:
                print("Se eliminó el universo ", getattr(a[i], "id"))
                a.pop(i)
                hoa=[]
                for k in a:
                    hoa.append(getattr(k,"id"))
                print("Universos actualmente activos: ",hoa)
                break

#_______________________________________________________________________Ma________________________________________________

castigaditos=[1]
base_uni=random.randint(36,100)
print("Los universos actualmente son: ", base_uni)
num_univ=int(input("¿Cuantos universos quieres crear de más?: "))
print("Los universos actualmente son: ", base_uni + num_univ)
l= base_uni + num_univ
a=[]
for i in range(l):
    h=Vertice(i)
    a.append(h)
for j in range(len(a)):
    if getattr(a[j],"lleno")==True:
        agregarid(getattr(act,"vecinos"))
        continue
    else:
        k=5
        k-=len((getattr(a[j],"vecinos")))
        if j==0:
            act =(a[0])
            b=random.sample(a,k)
            for u in range (len(b)):
                act.agregaVecino(b[u])
                if getattr(b[u],"lleno")==True:
                    continue
                else:
                    b[u].agregaVecino(act)
            agregarid(getattr(act,"vecinos"))
        else:
            act =(a[j])
            b=random.sample(a,k)
            for u in range (len(b)):
                act.agregaVecino(b[u])
                if getattr(b[u],"lleno")==True:
                    continue
                else:
                    b[u].agregaVecino(act)
            agregarid(getattr(act,"vecinos"))

inicio = random.choice(a)
visitados=[]
while (True):
    init = getattr(inicio,"id")
    print("Estas en el universo:",init)
    cont=input("¿Deseas seguir?(Y/N): ")
    if(cont=="N" or cont =="n"):
        break
    vecis=agregarid(getattr(inicio,"vecinos"))
    print("Puedes viajar a los universos:", vecis)

    num = int(input("Elige un universo: "))
    for j in vecis:
        ciclo2 = False
        if j == num:
            ciclo2 = True
            break

    for i in vecis:
        if ciclo2 == True:
            seg = (p_universo(castigaditos, a, num))
            if (seg) == True:
                for j in range(len(a)):
                    if num==h:
                        print("No puedes volver al universo inmediatamente anterior")
                        break
                    if (num == (getattr(a[j], "id"))):
                        visitados.append(getattr(inicio,"id"))
                        h=visitados[len(visitados) - 2]
                        inicio = a[j]
                    
                break
        else:
            print("¡¡Ese universo no está conectado!!")
            break

    if len(a) > 36:
        kil=input("¿Quieres eliminar un universo?(Y/N): ")
        if kil== "Y" or kil=="y":
            joa=[]
            for i in a:
                joa.append(getattr(i,"id"))
            print("Universos actualmente activos: ",joa)
            el = int(input("Elige un universo a eliminar: "))
            eliminar(a,el)
    else:
        print("No se pueden eliminar mas universos")