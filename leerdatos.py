import pandas as pd
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

def leerCsv():
    bDias=[]
    bJornada=[]
    bTotal=0
    df=pd.read_csv("Datos.csv",delimiter=';')
    print(df.iloc[0]["Direccion"])
    for i in range(0,len(df)):
        print()
        rc=df.iloc[i]["diaRecoleccion"]
        kr=df.iloc[i]["KilosReciclable"]
        knr=df.iloc[i]["KilosNoReciclables"]
        bTotal+=kr+knr
        jo=df.iloc[i]["Jornada"]
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
        return [[calcularPromedioPorDia(bDias,0),calcularPromedioPorDia(bDias,1),calcularPromedioPorDia(bDias,2),calcularPromedioPorDia(bDias,3),calcularPromedioPorDia(bDias,4),calcularPromedioPorDia(bDias,5),calcularPromedioPorDia(bDias,6)],[calcularPromedioPorJornada(bJornada,0),calcularPromedioPorJornada(bJornada,1),calcularPromedioPorJornada(bJornada,2)],bTotal/len(df)]
leerCsv()