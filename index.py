from flask import Flask, render_template
import sqlite3

app=Flask(__name__)
import pandas as pd
class RecoleccionRes:
    def __init__(self, direccion, habitantes,diaRecoleccion,jornada,kilosReciclable,kilosNoReciclables,sancion,timeStamp):
        if(isinstance(direccion, str) and isinstance(habitantes, int) and isinstance(diaRecoleccion, int) and isinstance(jornada, str) and isinstance(kilosReciclable, int) and isinstance(kilosNoReciclables, int) and isinstance(sancion, str)):    
            self.direccion = direccion
            self.habitantes = habitantes
            self.diaRecoleccion=diaRecoleccion
            self.jornada=jornada
            self.kilosReciclable=kilosReciclable
            self.kilosNoReciclable=kilosNoReciclables
            self.sancion=sancion
            self.timeStamp=timeStamp
            print("he sido creado")
        else:
            print("Uno de los atributos está mal")
    def setTimeStamp(self,timeStamp):
        if(isinstance(timeStamp, str)):
            self.timeStamp=timeStamp
            self.cambio()
        else:
            print("Debe ser un conjunto de caracteres")
    def getTimeStamp(self):
        return self.timeStamp
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
    def datos(self):
        return [self.timeStamp,self.direccion,self.habitantes,self.diaRecoleccion,self.jornada,self.kilosReciclable,self.kilosNoReciclable,self.sancion]
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
    conn = sqlite3.connect('database.db')
    registros=[]
    bDias=[]
    bJornada=[]
    bTotal=0
    df=pd.read_csv("Datos.csv",delimiter=';')
    print(df.iloc[0]["Direccion"])
    for i in range(0,len(df)):
        #consulta="INSERT INTO informacion (Direccion,NumHabitantes,DiaJornada,KilosReciclable,KilosOrganica,Sancion,tipoDireccion) \
      #VALUES ("+df.iloc[i]["Direccion"]+","+str(df.iloc[i]["Habitantes"])+","+str(df.iloc[i]["diaRecoleccion"])+str(df.iloc[i]["Jornada"])+","+str(df.iloc[i]["KilosReciclable"])+","+str(df.iloc[i]["KilosNoReciclables"])+","+df.iloc[i]["sancion"]+","+df.iloc[i]["Direccion"][0:2]+");"
        #print(consulta)
        #conn.execute(consulta)
        #conn.commit()
        registros.append(RecoleccionRes(str(df.iloc[i]["Direccion"]),int(df.iloc[i]["Habitantes"]),int(df.iloc[i]["diaRecoleccion"]),str(df.iloc[i]["Jornada"]),int(df.iloc[i]["KilosReciclable"]),int(df.iloc[i]["KilosNoReciclables"]),str(df.iloc[i]["sancion"]),str(df.iloc[i]["timestap"])))
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
    return [registros,[calcularPromedioPorDia(bDias,0),calcularPromedioPorDia(bDias,1),calcularPromedioPorDia(bDias,2),calcularPromedioPorDia(bDias,3),calcularPromedioPorDia(bDias,4),calcularPromedioPorDia(bDias,5),calcularPromedioPorDia(bDias,6)],[calcularPromedioPorJornada(bJornada,0),calcularPromedioPorJornada(bJornada,1),calcularPromedioPorJornada(bJornada,2)],bTotal/len(df)]

def myFunc(e):
  return e.getKilosNoReciclables()+e.getKilosReciclable()

@app.route("/")
def home():
    [registros,promedioDia,promedioJornada,promedioUser]=leerCsv()
    registros.sort(reverse=True,key=myFunc)
    listaMayor=[registros[0].datos(),registros[1].datos(),registros[2].datos(),registros[3].datos()]
    return render_template("index.html",ListaMayor=listaMayor)

@app.route("/about")
def ayuda():
    return render_template("about.html")
if __name__=="__main__":
    app.run(debug=True)
    
    