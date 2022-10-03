bRecTotal=0
bNoRecTotal=0
datos=[]
for i in range(0,10):
    bandera=True
    d=str(input("Introduzca la dirección: "))
    while(bandera):
        try:
            f=int(input("Introduzca el número de personas en su domicilio: "))
            bandera=False
        except:
            print("Error, ingrese nuevamente")
    bandera=True
    while(bandera):
        try:
            rc=int(input("Introduzca el día de recolección 1-Lunes 2-Martes .... 7-domingo: "))
            if(rc>0 and rc<8):
                bandera=False
                print("Los dias deben estar entre 1 y 7")
        except:
            print("Error, ingrese nuevamente")
    bandera=True
    while(bandera):
        try:
            jo=str(input("Intoduzca la jornada M-mañana T-Tarde N-Noche: "))   
            print(jo)
            if(jo=='M' or jo=='T' or jo=='N'):
                bandera=False
            else:
                print("Los valores debes ser M, T o N")
        except:
            print("Error, ingrese nuevamente")
    bandera=True
    while(bandera):
        try:
            kr=int(input("Introduzca los kilogramos de basura reciclable: "))
            if(kr>=0):
                bandera=False
                print("La cantidad debe ser positiva")
        except:
            print("Error, ingrese nuevamente")
    bandera=True
    while(bandera):
        try:
            knr=int(input("Introduzca los kilogramos de basura no reciclable: "))
            if(knr>=0):
                bandera=False
                print("La cantidad debe ser positiva")
        except:
            print("Error, ingrese nuevamente")
    bandera=True
    while(bandera):
        try:
            sa=str(input("NN-sin sanción SS-Servicio social PP-Sanción pecunaria: "))
            if(sa=="NN" or sa=="SS" or sa=="PP"):
                bandera=False
            else:
                print("Los valores debes ser NN, SS o PP")
        except:
            print("Error, ingrese nuevamente")
    
    datos[i]=[d,f,rc,jo,kr,knr,sa]
    bRecTotal+=kr
    bNoRecTotal+=knr

print("Base de datos")
#imprimiendo base de datos
for i in datos:
    print("Dirección: ",i[0])
    print("Numero habitantes hogar: ",i[1])
    print("Dia de recolección: ",i[2])
    print("Jornada de recolección: ",i[3])
    print("Kilos basura reciclable: ",i[4])
    print("Kilos basura no reciclable: ",i[5])
    print("Sanción: ",i[6])
#imprimiendo estadísticas
print("Estadísticas")
print("Basura reciclable total: ",bRecTotal)
print("Basura orgánica total: ",bNoRecTotal)
print("Promedio basura por habitante: ",(bRecTotal+bNoRecTotal)/(len(datos)))
print("Porcentaje reciclable",bRecTotal/(bRecTotal+bNoRecTotal))
print("Porcentaje orgánica",bNoRecTotal/(bRecTotal+bNoRecTotal))