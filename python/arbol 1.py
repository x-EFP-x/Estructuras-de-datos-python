class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
def ordenar(root,ins):
    if root:
        ordenar(root.left,ins)
        # print(root.val)
        ins.append(root.val)
        # print(ins)
        ordenar(root.right,ins)
    return(ins)
inp=input()
a=inp.replace(":"," ").replace("["," ").replace(","," ").replace("]"," ")
b=a.split()
c=[]
d = []

for i in range(len(b)):
    c.append(int(b[i]))
    
    
entr = input()

entr_ord=entr.replace(":"," ").replace("["," ").replace(","," ").replace("]"," ")
j=entr_ord.split()
for i in range(len(j)):
    d.append(int(j[i]))
    
f_node = Node(c[0])

for i in range(len(c)):
    f_node = insert(f_node, c[i])
ins = []
root_o=ordenar(f_node,ins)
cont=0
for i in range(len(root_o)):
    if root_o[i] >= d[0] and  root_o[i] <= d[1]:
        cont+=root_o[i]
print(cont)