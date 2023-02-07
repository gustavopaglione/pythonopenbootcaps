import sqlite3

def crear_tabla():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    tablas = [
		"""
			CREATE TABLE IF NOT EXISTS alumnos(
				 id INTEGER PRIMARY KEY,
                 nombre TEXT,
                 apellido TEXT
			);
		"""
	]
    for tabla in tablas:
        cursor.execute(tabla)
    
    print("Tablas creadas correctamente")

    conn.close

def insertar_tabla():
    conn = sqlite3.connect('alumnos.db')
    # Crear un cursor
    cursor = conn.cursor()

    alumnos= [
        """
        INSERT INTO alumnos
        (id, nombre, apellido)
        VALUES
         (1, 'Juan', 'Pérez'),
       (2, 'María', 'García'),
       (3, 'Pedro', 'Martínez'),
       (4, 'Ana', 'Rodríguez'),
       (5, 'José', 'González'),
       (6, 'Laura', 'Ruiz'),
       (7, 'David', 'Hernández'),
       (8, 'Sara', 'Díaz');

        """
    ]

    for sentencia in alumnos:
            cursor.execute(sentencia)
    
    conn.commit() #Guardamos los cambios al terminar el ciclo
	
    print("Alumnos insertados correctamente")

    conn.close

def leer_tabla():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    sentencia = "SELECT * FROM alumnos;"
 
    cursor.execute(sentencia)
	
    alumnos = cursor.fetchall()
	
    print(alumnos)
    
    conn.close

def buscar_alumno():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
 
    busqueda = input("Escribe tu búsqueda: ")
    if not busqueda:
        print("Búsqueda inválida")
        exit()
 
    sentencia = "SELECT * FROM alumnos WHERE nombre LIKE ?;"
 
    cursor.execute(sentencia, [ "%{}%".format(busqueda) ])
	
    alumnos = cursor.fetchall()
    print("+{:-<10}+{:-<20}+{:-<20}".format("", "", ""))
    print("|{:^10}|{:^20}|{:^20}|".format("id", "Nombre", "Apellido"))
    print("+{:-<10}+{:-<20}+{:-<20}".format("", "", ""))
 
 
    for id, nombre, apellido in alumnos:
    	print("|{:^20}|{:^20}|{:^10}|".format(id, nombre, apellido))

        
#    print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))

#    conn.close()

def main():

    crear_tabla()
    insertar_tabla()
    leer_tabla()
    buscar_alumno()

if __name__=='__main__':
    main()