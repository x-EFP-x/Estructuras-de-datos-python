passw = input()
def evaluar_M(passw):
    cump=False
    for i in range(len(passw)):
        if(passw[i].isupper()):
            cump=True
            break
    return (cump)
def evaluar_minus(passw):
    cump=False
    for i in range(len(passw)):
        if(passw[i].isupper()==False):
            cump=True
            break
    return (cump)
def evaluar_tam(passw):
    Ti=len(passw)
    if (Ti>=6 and Ti<=20):
        return True
    else:
        return False
def no_reps(passw):
    rep=passw[0]
    cont=0
    for i in range(len(passw)):
        if i>=1:
            if passw[i]!=rep:
                rep=passw[i]
                cont=0
            else:
                cont+=1
        if(cont==3):
            break
    if (cont==3):
        return False
    else:
        return True      
def all_cond(passw):
    conds=4
    if evaluar_M(passw)==True:
        conds-=1
    if evaluar_minus(passw)(passw)==False:
        conds-=1
    if evaluar_tam(passw)(passw)==True:
        conds-=1
    if no_reps(passw)(passw)==True:
        conds-=1
    print(conds)
all_cond(passw)    