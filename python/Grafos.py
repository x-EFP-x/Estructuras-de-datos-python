##definimos vertices
class Vertice:
    def __init__(self,i):
        self.id = iself.visitado = False
        self.nivl = -1
        self.vecinos = []
    def agregaVecino(self,v):
        if not v in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    def __init__(self):
        self.vertices = {}
    
    def agregaVertice(self, v):
        if not v in self.vertices:
            self.vertices[v] = Vertice(v)
    
    def agregararista(self, a, b):
        if a in self.vrtices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)

def main():
    
    g = Grafica()

    l = [0,1,2,3,4,5,6]
    for v in l:
        g.agregarVertice(v)