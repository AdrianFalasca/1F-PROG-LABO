import sqlite3

class Consultas:
    """
    Clase con tres métodos para crear tabla, agregar datos y traerlos.
    Inicializa con la propiedad con el nombre de la tabla y llamando
    al método para crearla.
    """
    def __init__(self):
        self.path = "tetris.db"
        self.crear_tabla()

    def crear_tabla(self):
        with sqlite3.connect(self.path) as conexion:
            try:
                sentencia = ''' create table score
                                (
                                        id integer primary key autoincrement,
                                        nombre text,
                                        score integer
                                )
                            '''
                conexion.execute(sentencia)
                print("Se creo la tabla score")                       
            except sqlite3.OperationalError:
                print("La tabla score ya existe") 
            finally:
                print("Ingresó en el método para crear tabla")

    def agregar_dato(self, nombre, score):
        with sqlite3.connect(self.path) as conexion:
            try:
                conexion.execute("insert into score(nombre,score) values (?,?)", (nombre, score))                                 
                conexion.commit()
                print("Dato agregado correctamente")
            except:
                print("Error")
            finally:
                print("Ingresó en el método para agregar datos")

    def traer_datos(self):
        with sqlite3.connect(self.path) as conexion:
            try:
                sentencia = "SELECT * FROM score ORDER BY score DESC LIMIT 5"
                cursor=conexion.execute(sentencia)
                return cursor
            except:
                print("Error")
    
                
            
