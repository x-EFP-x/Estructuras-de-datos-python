def ConvertirEntrada (list):
    x = 1
    while x <= len(list):
        try:
            list[x-1] = int(list[x-1])
            x += 1
        except:
            list.pop(x-1)
    return(list)

inventario0 = [0,0,0]
inventario1 = [0,0,0]
inventario2 = [0,0,0]
inventario3 = [0,0,0]
lotes = []
i=1
entrada = (input()).split(' ')
entrada = ConvertirEntrada(entrada)

while i > 0:
    x = 0
    try:
        entrada2 = input()

        if entrada2 == "Imprimir":
            a= 0
            b= 0
            c= 0
            d= 0
            while a == 0 or b == 0 or c == 0 or d == 0:
                if (entrada[0] <= entrada[1] or b == 1) and (entrada[0] <= entrada[2] or d == 1) and (entrada[0] <= entrada[3] or c == 1) and (a == 0):
                    print("Ingenieria ",entrada[0]," - Computers ",inventario0[0]," Laptops ",inventario0[1]," Tablets ",inventario0[2])
                    a = 1
                if (entrada[1] <= entrada[0] or a == 1) and (entrada[1] <= entrada[2] or d == 1) and (entrada[1] <= entrada[3] or c == 1) and (b == 0):
                    print("Humanas ",entrada[1]," - Computers ",inventario1[0]," Laptops ",inventario1[1]," Tablets ",inventario1[2])
                    b= 1
                if (entrada[3] <= entrada[0] or a == 1) and (entrada[3] <= entrada[1] or b == 1) and (entrada[3] <= entrada[2] or d == 1) and (c == 0):
                    print("Medicina ",entrada[3]," - Computers ",inventario3[0]," Laptops ",inventario3[1]," Tablets ",inventario3[2])
                    c= 1
                if (entrada[2] <= entrada[0] or a == 1) and (entrada[2] <= entrada[1] or b == 1) and (entrada[2] <= entrada[3] or c == 1) and (d == 0):
                    print("Artes ",entrada[2]," - Computers ",inventario2[0]," Laptops ",inventario2[1]," Tablets ",inventario2[2])
                    d= 1
            inventario0 = [0,0,0]
            inventario1 = [0,0,0]
            inventario2 = [0,0,0]
            inventario3 = [0,0,0]

        elif entrada2 == "Distribuir lote":
            while (entrada[0] or entrada[1] or entrada[2] or entrada[3] >= 1) and (lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1:

                if (entrada[0] >= entrada[1]) and (entrada[0] >= entrada[2]) and (entrada[0] >= entrada[3]) and ((lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1):
                    while entrada[0] >= 1 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1:
                        if x == 3:
                            x=0
                        while x < 3 and entrada[0]>0 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) > 0:
                            if lotes[0][x] >= 1 and entrada[0] >= 1:
                                lotes[0][x] -= 1
                                entrada[0] -= 1
                                inventario0[x] += 1
                                x += 1
                            elif lotes[0][x] == 0:
                                x += 1

                elif (entrada[1] >= entrada[0]) and (entrada[1] >= entrada[2]) and (entrada[1] >= entrada[3]) and ((lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1):
                    while entrada[1] >= 1 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1:
                        if x == 3:
                            x=0
                        while x < 3 and entrada[1]>0 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) > 0:
                            if lotes[0][x] >= 1 and entrada[1] >= 1:
                                lotes[0][x] -= 1
                                entrada[1] -= 1
                                inventario1[x] += 1
                                x += 1
                            elif lotes[0][x] == 0:
                                x += 1

                elif (entrada[3] >= entrada[0]) and (entrada[3] >= entrada[1]) and (entrada[3] >= entrada[2]) and ((lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1):
                    while entrada[3] >= 1 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1:
                        if x == 3:
                            x=0
                        while x < 3 and entrada[3]>0 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) > 0:
                            if lotes[0][x] >= 1 and entrada[3] >= 1:
                                lotes[0][x] -= 1
                                entrada[3] -= 1
                                inventario3[x] += 1
                                x += 1
                            elif lotes[0][x] == 0:
                                x += 1

                elif (entrada[2] >= entrada[0]) and (entrada[2] >= entrada[1]) and (entrada[2] >= entrada[3]) and ((lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1):
                    while entrada[2] >= 1 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) >= 1:
                        if x == 3:
                            x=0
                        while x < 3 and entrada[2]>0 and (lotes[0][0] + lotes[0][1] + lotes[0][2]) > 0:
                            if lotes[0][x] >= 1 and entrada[2] >= 1:
                                lotes[0][x] -= 1
                                entrada[2] -= 1
                                inventario2[x] += 1
                                x += 1
                            elif lotes[0][x] == 0:
                                x += 1

            if (lotes[0][0] + lotes[0][1] + lotes[0][2]) == 0:
                lotes.pop(0)
            elif (lotes[0][0] + lotes[0][1] + lotes[0][2]) > 0:
                if len(lotes) > 1:
                    lotes[1][0] = lotes[1][0] + lotes[0][0]
                    lotes[1][1] = lotes[1][1] + lotes[0][1]
                    lotes[1][2] = lotes[1][2] + lotes[0][2]
                    lotes.pop(0)

        else:
            entrada2 = entrada2.split(' ')
            entrada2 = ConvertirEntrada(entrada2)
            lotes.append(entrada2)
    except:
        break
