from asyncio.windows_events import NULL
import random as rd
import pandas as pd
import time
from datetime import datetime
# current date and time
now = datetime.now()

class RecoleccionRes:
    def __init__(self, direccion, habitantes,diaRecoleccion,jornada,kilosReciclable,kilosNoReciclables,sancion):
        if(isinstance(direccion, str) and isinstance(habitantes, int) and isinstance(diaRecoleccion, int) and isinstance(jornada, str) and isinstance(kilosReciclable, int) and isinstance(kilosNoReciclables, int) and isinstance(sancion, str)):    
            self.direccion = direccion
            self.habitantes = habitantes
            self.diaRecoleccion=diaRecoleccion
            self.jornada=jornada
            self.kilosReciclable=kilosReciclable
            self.kilosNoReciclable=kilosNoReciclables
            self.sancion=sancion
            print("he sido creado")
        else:
            print("Uno de los atributos está mal")
    def setDireccion(self,direccion):
        if(isinstance(direccion, str)):
            self.direccion=direccion
            self.cambio()
        else:
            print("Debe ser un conjunto de caracteres")
    def getDireccion(self):
        return self.direccion
    def setHabitantes(self,habitantes):
        if(isinstance(habitantes, str)):
            self.habitantes=habitantes
            self.cambio()
        else:
            print("Debe ser un entero")
    def getHabitantes(self):
        return self.habitantes
    def setDiaRecoleccion(self,diaRecoleccion):
        if(isinstance(diaRecoleccion, int)):
            self.diaRecoleccion=diaRecoleccion
            self.cambio()
        else:
            print("Debe ser un entero")
    def getDiaRecoleccion(self):
        return self.diaRecoleccion
    def setJornada(self,jornada):
        self.jornada=jornada
        self.cambio()
    def getJornada(self):
        return self.jornada
    def setKilosReciclable(self,kilosReciclable):
        if(isinstance(kilosReciclable, int)):
            self.kilosReciclable=kilosReciclable
            self.cambio()
        else:
            print("Debe ser un entero")
    def getKilosReciclable(self):
        return self.kilosReciclable
    def setKilosNoReciclables(self,kilosNoReciclables):
        if(isinstance(kilosNoReciclables, int)):
            self.kilosNoReciclable=kilosNoReciclables
            self.cambio()
        else:
            print("Debe ser un entero")
    def getKilosNoReciclables(self):
        return self.kilosNoReciclable
    def setSancion(self,sancion):
        if(isinstance(sancion, str)):
            self.sancion=sancion
            self.cambio()
        else:
            print("Debe ser un caracter")
    def getSancion(self):
        return self.sancion
    def cambio(self):
        print("He sido cambiado!")
    def eliminar(self):
        self.direccion=NULL
        self.habitantes = NULL
        self.diaRecoleccion=NULL
        self.jornada=NULL
        self.kilosReciclable=NULL
        self.kilosNoReciclable=NULL
        self.sancion=NULL
        print("He sido eliminado")    
    def calcularTotal(self):
        return self.kilosNoReciclable+self.kilosReciclable
    def mostrarContenido(self):
        print(self.direccion+" "+str(self.habitantes)+"   "+str(self.diaRecoleccion)+"   "+self.jornada+"   "+str(self.kilosReciclable)+"  "+str(self.kilosNoReciclable)+"  "+self.sancion+" "+str(self.calcularTotal()))
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
def generarRegistros():
    registros=[]
    df = pd.DataFrame()
    for i in range(0,rd.randint(150,200)):
        registros.append(RecoleccionRes(generarDireccion(),rd.randint(1,7),rd.randint(1,7),generarJornada(),rd.randint(0,100),rd.randint(0,100),generarSancion()))
        if(i<10):
            c="00"+str(i)
        elif(i<100):
            c="0"+str(i)
        else:
            c=str(i)
        fila={'Direccion':registros[i].getDireccion(),'Habitantes':registros[i].getHabitantes(),'diaRecoleccion':registros[i].getDiaRecoleccion(),'Jornada':registros[i].getJornada(),'KilosReciclable':registros[i].getKilosReciclable(),'KilosNoReciclables':registros[i].getKilosNoReciclables(),'sancion':registros[i].getSancion(),'timestap':c+now.strftime("%Y%m%d%H%M")}
        df = df.append(fila, ignore_index=True)
    df.to_json("Datos.json",orient='records')
    df.to_csv("Datos.csv",index=False,sep=';')
    return registros


registros=generarRegistros()
def myFunc(e):
  return e.getKilosNoReciclables()+e.getKilosReciclable()

registros.sort(reverse=True,key=myFunc)
print("Registros con mayor consumo")
print("Dir         Hab Dia Jor Rec NoR San")
registros[0].mostrarContenido()
registros[1].mostrarContenido()
registros[2].mostrarContenido()
registros[3].mostrarContenido()
print("Registros medios")
print("Dir         Hab Dia Jor Rec NoR San")
registros[int(len(registros)/2)-2].mostrarContenido()
registros[int(len(registros)/2)-1].mostrarContenido()
registros[int(len(registros)/2)].mostrarContenido()
registros[int(len(registros)/2)+1].mostrarContenido()


print("Registros con menor consumo")
print("Dir         Hab Dia Jor Rec NoR San")
registros[len(registros)-4].mostrarContenido()
registros[len(registros)-3].mostrarContenido()
registros[len(registros)-2].mostrarContenido()
registros[len(registros)-1].mostrarContenido()
