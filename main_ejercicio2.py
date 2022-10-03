import random as rd
import time
start=time.time()
bRecTotal=0
bNoRecTotal=0
datos=[]
def generarDireccion():
    vectorCadena1=["CL","CR","DG","TV"]
    c1=vectorCadena1[rd.randint(0,3)]
    c2=""
    c2_aux=rd.randint(1,95)
    if(c2_aux<10):
        c2="0"+str(c2_aux)
    else:
        c2=str(c2_aux)
    c3=""
    c3_aux=rd.randint(1,95)
    if(c3_aux<10):
        c3="0"+str(c3_aux)
    else:
        c3=str(c3_aux)
    c4=""
    c4_aux=rd.randint(1,95)
    if(c4_aux<10):
        c4="0"+str(c4_aux)
    else:
        c4=str(c4_aux)
    direccion=c1+" "+c2+" "+c3+"-"+c4
    return direccion
def generarJornada():
    vectorCadena1=["M","T","N"]
    return vectorCadena1[rd.randint(0,2)]
def generarSancion():
    vectorCadena1=["NN","SS","PP"]
    return vectorCadena1[rd.randint(0,2)]
def calcularSancion(kr,knr):
    return 60000*(kr+knr)
def calcularPromedioPorDia(datos,dia):
    acum=0
    for i in datos:
        acum+=i[dia]
    return acum/len(datos)
def calcularPromedioPorJornada(datos,dia):
    acum=0
    for i in datos:
        acum+=i[dia]
    return acum/len(datos)
bDias=[]
bJornada=[]
print("Dir         Hab Dia Jor Rec NoR San")
for i in range(0,10):
    d=generarDireccion()
    f=rd.randint(1,7)
    rc=rd.randint(1,7)
    jo=generarJornada()
    kr=rd.randint(0,100)
    knr=rd.randint(0,100)
    sa=generarSancion()
    datos.append([d,f,rc,jo,kr,knr,sa])
    bRecTotal+=kr
    bNoRecTotal+=knr
    if(rc==1):
        bDias.append([kr+knr,0,0,0,0,0,0])
    elif(rc==2):
        bDias.append([0,kr+knr,0,0,0,0,0])
    elif(rc==3):
        bDias.append([0,0,kr+knr,0,0,0,0])
    elif(rc==4):
        bDias.append([0,0,0,kr+knr,0,0,0])
    elif(rc==5):
        bDias.append([0,0,0,0,kr+knr,0,0])
    elif(rc==6):
        bDias.append([0,0,0,0,0,kr+knr,0])
    elif(rc==7):
        bDias.append([0,0,0,0,0,0,kr+knr])
    if(jo=="M"):
        bJornada.append([kr+knr,0,0])
    elif(jo=="T"):
        bJornada.append([0,kr+knr,0])
    elif(jo=="N"):
        bJornada.append([0,0,kr+knr])
 #   if(sa=="NN"):
 #       print("No hay sanción")
  #  elif(sa=="SS"):
  #      print("Sanción social")
  #  elif(sa=="PP"):
  #      print("Sanción pecuniaria con valor de: ",calcularSancion(kr,knr))
    print(datos[i][0]+" "+str(datos[i][1])+"   "+str(datos[i][2])+"   "+datos[i][3]+"   "+str(datos[i][4])+"  "+str(datos[i][5])+"  "+datos[i][6])

print("promedio de basura por familia ",(bRecTotal+bNoRecTotal)/len(datos))
print("promedio de basura del dia Lunes: ",calcularPromedioPorDia(bDias,0))
print("promedio de basura del dia Martes: ",calcularPromedioPorDia(bDias,1))
print("promedio de basura del dia Miercoles: ",calcularPromedioPorDia(bDias,2))
print("promedio de basura del dia Jueves: ",calcularPromedioPorDia(bDias,3))
print("promedio de basura del dia Viernes: ",calcularPromedioPorDia(bDias,4))
print("promedio de basura del dia Sábado: ",calcularPromedioPorDia(bDias,5))
print("promedio de basura del dia Domingo: ",calcularPromedioPorDia(bDias,6))
print("promedio de basura de la jornada de la mañana: ",calcularPromedioPorJornada(bJornada,0))
print("promedio de basura de la jornada de la tarde:",calcularPromedioPorJornada(bJornada,1))
print("promedio de basura de la jornada de la noche: ",calcularPromedioPorJornada(bJornada,2))
end=time.time()

print(end-start)