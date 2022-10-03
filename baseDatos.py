import sqlite3
conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE sanciones (ID INTEGER PRIMARY KEY AUTOINCREMENT,TIPO CHAR(1) NOT NULL);''')
conn.execute("INSERT INTO sanciones (TIPO) VALUES ('NN');");
conn.execute("INSERT INTO sanciones (TIPO) VALUES ('SS');");
conn.execute("INSERT INTO sanciones (TIPO) VALUES ('PP');");
conn.commit()
conn.execute('''CREATE TABLE TIPODIRECCION (ID INTEGER PRIMARY KEY AUTOINCREMENT,TIPO CHAR(2) NOT NULL);''')
conn.execute("INSERT INTO TIPODIRECCION (TIPO) VALUES ('CL');");
conn.execute("INSERT INTO TIPODIRECCION (TIPO) VALUES ('CR');");
conn.execute("INSERT INTO TIPODIRECCION (TIPO) VALUES ('DG');");
conn.execute("INSERT INTO TIPODIRECCION (TIPO) VALUES ('TV');");
conn.commit()
conn.execute('''CREATE TABLE JORNADADIA (ID INTEGER PRIMARY KEY AUTOINCREMENT,JORNADA CHAR(2) NOT NULL);''')
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('1M');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('2M');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('3M');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('4M');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('5M');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('6M');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('7M');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('1T');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('2T');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('3T');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('4T');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('5T');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('6T');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('7T');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('1N');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('2N');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('3N');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('4N');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('5N');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('6N');");
conn.execute("INSERT INTO JORNADADIA (JORNADA) VALUES ('7N');");
conn.commit()

conn.execute('''CREATE TABLE informacion
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         Direccion CHAR(50)    NOT NULL,
         NumHabitantes INT NOT NULL,
         DiaJornada CHAR(2) NOT NULL,
         KilosReciclable INT NOT NULL,
         KilosOrganica INT NOT NULL,
         Sancion CHAR(2) NOT NULL,
         tipoDireccion CHAR(2) NOT NULL,
         FOREIGN KEY (DiaJornada) REFERENCES JORNADADIA(ID),
         FOREIGN KEY (Sancion) REFERENCES sanciones(ID),
         FOREIGN KEY (tipoDireccion) REFERENCES TIPODIRECCION(ID));''')
conn.commit()
#conn.execute("INSERT INTO datos (ID,Direccion,NumHabitantes,DiaJornada,KilosReciclable,KilosOrganica,Sancion,tipoDireccion) \
 #     VALUES (1, 'calle 1', 5, 2, 'M',20,20,'NN')");
#conn.commit()
conn.close()