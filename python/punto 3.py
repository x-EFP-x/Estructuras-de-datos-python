class facus:
    def _init_(self, nombre, prioridad, cant_comp, cant_lap, cant_tab):
        self.nombre = nombre
        self.prioridad = prioridad
        self.estd_pobres = parametroestd(totaltoken, self.nombre)
        self.cant_comp =  cant_comp
        self.cant_lap =  cant_lap
        self.cant_tab =  cant_tab
        
class cantidades:
    def _init_(self, nombre):
        self.nombre = nombre
        self.cantidad = parameter(totaltoken, self.nombre)
    
def parameter(array, parameter):
    lon=len(array)
    cantidad=[]
    for i in range(lon):
        if (array[i]==parameter):
            a=int(array[i+1])
            cantidad.append(a)
    return cantidad
    
def parametroestd(array, parameter):
    lon=len(array)
    cantidad=0
    for i in range(lon):
        if (array[i]==parameter):
            a=int(array[i+1])
            cantidad+=a
    return(cantidad)

def ordenar_arr(fac_array):
    #ordena el arreglo de las facus de mayor a menor
    for i in range(len(fac_array) - 1):
        for j in range(len(fac_array) - 1 - i):
            num1 = fac_array[j][2]
            num2 = fac_array[j + 1][2]
            if num2 > num1:
                fac_array[j], fac_array[j + 1] = fac_array[j + 1], fac_array[j]    
    return fac_array

def order_array_des(fac_array):
    for i in range(len(fac_array) - 1):
        for j in range(len(fac_array) - 1 - i):
            num1 = fac_array[j][2]
            num2 = fac_array[j + 1][2]
            if num1 > num2:
                fac_array[j], fac_array[j + 1] = fac_array[j+1] , fac_array[j]    
    return(fac_array)
    
def prioridad_arr(fac_array):
    for l in range (len(fac_array)-1):
        if fac_array[l][2] == fac_array[l+1][2]:
            for m in range(len(fac_array) - 1 - l):
                    num1 = fac_array[m][1]
                    num2 = fac_array[m + 1][1]
                    if num2 > num1:
                        fac_array[m], fac_array[m + 1] = fac_array[m+1], fac_array[m] 
                        fac_array=order_array_des(fac_array) 
                        continue
    return fac_array                        
    
def distribuir_facu(fac_array,lote_arr,fac,p_entrada):
    
    continu=True
    
    if fac_array[fac][2]==0:
        return 0
        
    while(continu):
        
        if lote_arr[0]==0 and lote_arr[1]==0 and lote_arr[2]==0:
            continu=False
            break
        
        if p_entrada == 1:
            p_entrada+=1
            if lote_arr[0]!=0:
                lote_arr[0]-=1
                fac_array[fac][3]+=1
                fac_array[fac][2]-=1
                if(fac_array[fac][2]==0):
                    continu=False
                    break
        
        if p_entrada == 2:
            p_entrada+=1
            if lote_arr[1]!=0:
                lote_arr[1]-=1
                fac_array[fac][4]+=1
                fac_array[fac][2]-=1
                if(fac_array[fac][2]==0):
                    continu=False
                    break

        
        if p_entrada== 3:
            p_entrada+=1
            if lote_arr[2]!=0:
                lote_arr[2]-=1
                fac_array[fac][5]+=1
                fac_array[fac][2]-=1
                if fac_array[fac][2]==0:
                    continu=False
                    break
        p_entrada=1
        
    return p_entrada
   
def distribuir(fac_array,lote_arr):
    pos = 1
    pos = distribuir_facu(fac_array,lote_arr,0,pos)
    pos = distribuir_facu(fac_array,lote_arr,1,pos)
    pos = distribuir_facu(fac_array,lote_arr,2,pos)
    distribuir_facu(fac_array,lote_arr,3,pos)

cont = 0
total1=[]

while True:
    try:
        entrada=input()
        total1.append(entrada)
        if entrada:
            cont = cont + 1
    except:
        break

c, lotes_arr, estd_arr, prio =[],[],[],[]
cont_lote=0        
cont_dist=0

for i in range(len(total1)):
    
    if "Ingenieria" in total1[i] :
        
        totaltoken=total1[i].split()
        
        fac1, fac2, fac3, fac4 = facus("Ingenieria", 4,0,0,0), facus("Humanas", 3,0,0,0), facus("Medicina", 2,0,0,0), facus("Artes", 1,0,0,0)
        
        fac_array, fac= [] , []
        fac.append(fac1)
        fac.append(fac2)
        fac.append(fac3)
        fac.append(fac4)
        
        for i in range (len(fac)):
            fac_=[]
            fac_.append(getattr(fac[i], "nombre"))
            fac_.append(getattr(fac[i], "prioridad"))
            fac_.append(getattr(fac[i], "estd_pobres"))
            fac_.append(getattr(fac[i], "cant_comp"))
            fac_.append(getattr(fac[i], "cant_lap"))
            fac_.append(getattr(fac[i], "cant_tab"))
            fac_array.append(fac_)
        continue    
                
    if "Lote" in total1[i] :
        cont_lote+=1
        totaltoken=total1[i].split()
        
        comp, lap, tab =cantidades("Computers"), cantidades("Laptops"), cantidades("Tablets")
        
        equipos_arr=[]
        equipos_arr.append(comp)
        equipos_arr.append(lap)
        equipos_arr.append(tab)

        lote=[]
        for i in range(len(equipos_arr)):
            lote.append(getattr(equipos_arr[i], "cantidad"))
        
        for i in range (len(lote)):
            lote[i]= int(lote[i][0])
        
        lotes_arr.append(lote)
        continue 
        
    if "Distribuir" in total1[i] :
        lote1, lote2 = [],[]
        cont_dist+=1
        if cont_lote == 1:
            lote1=lotes_arr[0]
        if cont_lote == 2:
            lote1=lotes_arr[0]
            lote2=lotes_arr[1]
            
        if cont_dist==1:
            fac_array=ordenar_arr(fac_array)
            distribuir(fac_array,lote1)
            
        if cont_dist==2:
            fac_array=ordenar_arr(fac_array)
            distribuir(fac_array,lote2)
        continue     
            
    if "Imprimir" in total1[i] :
        fac_array=order_array_des(fac_array)
        fac_array=prioridad_arr(fac_array)    

        for i in range(len(fac_array)):
            print(fac_array[i][0]," ",fac_array[i][2]," - Computers ",fac_array[i][3]," Laptops ",fac_array[i][4]," Tablets ",fac_array[i][5])
            
        for i in range(len(fac_array)):
            fac_array[i][3],fac_array[i][4],fac_array[i][5]=0,0,0
        continue