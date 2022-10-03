import sqlite3
conn = sqlite3.connect('datos.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE sanciones
         (ID INT PRIMARY KEY AUTO_INCREMENT,
            TIPO CHAR(1) NOT NULL;''')
conn.execute("INSERT INTO sanciones (TIPO) VALUES ('NN')");
conn.execute("INSERT INTO sanciones (TIPO) VALUES ('SS')");
conn.execute("INSERT INTO sanciones (TIPO) VALUES ('PP')");
conn.commit()

#conn.execute('''CREATE TABLE datos
#         (ID INT PRIMARY KEY     NOT NULL,
#         Direccion      CHAR(50)    NOT NULL,
#         NumHabitantes INT NOT NULL,
#         Dia INT NOT NULL,
#         Jornada CHAR(1) NOT NULL,
#         KilosReciclable INT NOT NULL,
#         KilosOrganica INT NOT NULL,
#         Sancion CHAR(2) NOT NULL),
#         FOREIGN KEY (sancion) REFERENCES Persons(PersonID);''')

#conn.execute("INSERT INTO datos (ID,Direccion,NumHabitantes,Dia,Jornada,KilosReciclable,KilosOrganica,Sancion) \
#      VALUES (1, 'calle 1', 5, 2, 'M',20,20,'NN')");
#conn.commit()
conn.close()