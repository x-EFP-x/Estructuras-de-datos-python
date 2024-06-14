def root(tree):
    pos_tree=tree[0].replace("[","")
    return pos_tree

def even(level,val):
    if (level % 2 == 0):
        if (val % 2 == 0): 
            return False            

def even_lv(level,val,p_val):
    if (level % 2 == 0):
        if (val % 2 == 0): 
            return False
        if int(val) <= int(p_val):
                return False   

def odd_lv(level,val,p_val):
    if (level % 2 == 1):
        if (val % 2 == 1): 
            return False
        if int(val) >= int(p_val):
                return False                                    

def odd(level,val):
    if (level % 2 == 1):
        if (val % 2 == 1):           
            return False 

def comp(level,p_val_data):
    for i in range (len(p_val_data)): 
        if i == 0:
            if (even(level,int(p_val_data[i]))==False):
                return False  
            elif (odd(level,int(p_val_data[i]))==False):
                return False               
        else:
            if (even_lv(level,int(p_val_data[i]),int(p_val_data[i-1]))==False):
                return False 
            elif (odd_lv(level,int(p_val_data[i]),int(p_val_data[i-1]))==False):
                return False               

def verf_arbol(tree):
    for i in range(len(tree)):
        level=i
        if "," in tree[i]:
            p_val_data=tree[i].split(",")
            if(comp(level,p_val_data)==False):
                return False   
        elif(len(tree[i])==1):
            if (even(level,int(tree[i]))==False):
                return False                
            elif (odd(level,int(tree[i]))==False):
                return False       
    return True                    
# _______________________________main_____________________________-
tree=input()
tree = tree.split(":")
n_arbol=[]
n_arbol.append(root(tree))
tree.pop(0)
nv_arbol=0

bandera=False
ub=[]
while bandera == False:
    s_ub=[]
    for i in range (len(tree)):
        if "," in tree[i]:
            arb_datos=tree[i].split(",")
            for j in range(len(arb_datos)):
                if "[" in arb_datos[j]:
                    nv_arbol+=1
                    n_arbol.append(arb_datos[j].replace("[","")) 
                if "]" in arb_datos[j]:
                    cant=0
                    for m in range(len(arb_datos[j])):
                        if arb_datos[j][m] == "]":
                            cant+=1
                    n_arbol[nv_arbol]= n_arbol[nv_arbol]+","+(arb_datos[j].replace("]",""))
                    s_ub.append(j)
                    nv_arbol-=cant
                    bandera=True
            for p in range(len(s_ub)):
                n_ub=0
                arb_datos.pop(n_ub)
                n_ub=s_ub[p]-1
            strd=""    
            for data in arb_datos:
                strd=strd+data
            tree[i]=data        
            break

        if "[" in tree[i]:
            nv_arbol+=1
            n_arbol.append(tree[i].replace("[",""))         
            ub.append(i)

for i in range (len(ub)):
    n_ub=0
    tree.pop(ub[n_ub])
    n_ub=ub[i]-1    
    

for i in range (len(tree)):
    if "," in tree[i]:
        arb_datos=tree[i].split(",")
        for j in range (len(arb_datos)):
            if "[" in arb_datos[j]:
                arb_datos[j]=arb_datos[j].replace("[","")
                nv_arbol+=1
                cant=0
                if "]" in arb_datos[j]:
                    for m in range(len(arb_datos[j])):
                        if arb_datos[j][m] == "]":
                            cant+=1
                    arb_datos[j]=arb_datos[j].replace("]","")    
                n_arbol[nv_arbol]= n_arbol[nv_arbol]+","+(arb_datos[j])
                nv_arbol-=cant
                continue
            n_arbol[nv_arbol]= n_arbol[nv_arbol]+","+(arb_datos[j])        
        continue
                
                    
    if "[" in tree[i]:
        tree[i]=tree[i].replace("[","")
        nv_arbol+=1
        cant=0
        if "]" in tree[i]:
            tree[i]=tree[i].replace("]","") 
            for m in range(len(tree[i])):
                if tree[i][m] == "]":
                    cant+=1
        n_arbol[nv_arbol]= n_arbol[nv_arbol]+","+(tree[i])
        nv_arbol-=cant        
        continue

    n_arbol[nv_arbol]= n_arbol[nv_arbol]+","+(tree[i])    
    if(nv_arbol==0):
        break

if (verf_arbol(n_arbol)):
    print("Si")
else:
    print("No")

