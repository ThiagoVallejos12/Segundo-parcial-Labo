import sqlite3

def crear_tabla(ruta):
    """
    Crea una tabla llamada jugadores en la ruta que se especifique.
    parametro:
    ruta: la ruta de la base de datos.
    """
    with sqlite3.connect(ruta) as conexion:
        try:
            sentencia =('''CREATE TABLE IF NOT EXISTS jugadores
                (
                    id integer primary key autoincrement,
                    nombre text,
                    puntuacion integer
                )
                ''')
            conexion.execute(sentencia)
            conexion.commit() #confirma los cambios en la base de datos
        except sqlite3.OperationalError:
            print("La tabla personajes ya existe")   

def guardar_puntuacion(nombre, puntuacion, ruta):
    """
    Guarda la puntuacion en la tabla jugadores de la base de datos.
    parametros:
    nombre: el nombre del jugador.
    puntuacion: la puntuacion a guardar.
    ruta: la ruta de la base de datos.
    """
    with sqlite3.connect(ruta) as conexion:
        cursor = conexion.execute("SELECT puntuacion FROM jugadores WHERE nombre = ?", (nombre,))
        resultado = cursor.fetchone()
        if resultado is None:
            conexion.execute('INSERT INTO jugadores (nombre, puntuacion) VALUES (?,?)', (nombre, puntuacion)) #Si no existe una puntuación guardada para el jugador, se inserta un nuevo registro en la tabla
        else:
            puntuacion_existente = resultado[0]
            if puntuacion > puntuacion_existente:
                #Si la nueva puntuación es mayor que la existente, se actualiza el registro en la tabla
                conexion.execute('UPDATE jugadores SET puntuacion = ? WHERE nombre = ?', (puntuacion, nombre))
        conexion.commit()