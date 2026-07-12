# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Integrantes:
# - Cevallos Mendoza Samantha Nikole
# - Laura Fernanda Guillén Vargas
# - Cristhian Isaac Estrella Espinoza
# - Evelyn Noemi Burbano Mora
# - Janeth Maria Verdezoto García



import sys

import pyodbc as bd


class Conexion:
    """
    Clase que permite abrir conexión a la BBDD ServicioGimnasio y abrir cursor.
    """
    _SERVIDOR = '192.168.18.63\\SQLCEVALLOSSAM'   # IP local de la máquina donde vive SQL Server
    _BBDD = 'ServicioGimnasio'
    _USUARIO = 'admin_SAP'
    _PASSWORD = '1234'
    _conexion = None
    _cursor = None

    @classmethod
    def obtener_conexion(cls):
        """
        Obtiene la conexión a la BBDD con los parámetros de conexión pasados como constantes.
        """
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                                           + ';TrustServerCertificate=yes')
                return cls._conexion
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtener_cursor(cls):
        """
        Obtiene el cursor de la conexión.
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtener_conexion().cursor()
                return cls._cursor
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._cursor


class ServicioDAO:
    """
    Clase de acceso a datos (DAO) para la tabla Servicio.
    Contiene las operaciones CRUD que usa la interfaz gráfica:
    guardar, buscar por cédula, actualizar, eliminar y listar todos.
    """

    @classmethod
    def guardar(cls, cedula, nombre, apellido, email, servicio, descripcion, precio):
        cursor = Conexion.obtener_cursor()
        cursor.execute(
            """
            INSERT INTO Servicio (cedula, nombre, apellido, email, servicio, descripcion, precio)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            cedula, nombre, apellido, email, servicio, descripcion, precio
        )
        Conexion.obtener_conexion().commit()

    @classmethod
    def buscar_por_cedula(cls, cedula):
        cursor = Conexion.obtener_cursor()
        cursor.execute(
            'SELECT cedula, nombre, apellido, email, servicio, descripcion, precio '
            'FROM Servicio WHERE cedula = ?',
            cedula
        )
        fila = cursor.fetchone()
        if fila is None:
            return None
        columnas = [columna[0] for columna in cursor.description]
        return dict(zip(columnas, fila))

    @classmethod
    def actualizar(cls, cedula, nombre, apellido, email, servicio, descripcion, precio):
        cursor = Conexion.obtener_cursor()
        cursor.execute(
            """
            UPDATE Servicio
            SET nombre = ?, apellido = ?, email = ?, servicio = ?, descripcion = ?, precio = ?
            WHERE cedula = ?
            """,
            nombre, apellido, email, servicio, descripcion, precio, cedula
        )
        Conexion.obtener_conexion().commit()
        return cursor.rowcount > 0

    @classmethod
    def eliminar(cls, cedula):
        cursor = Conexion.obtener_cursor()
        cursor.execute('DELETE FROM Servicio WHERE cedula = ?', cedula)
        Conexion.obtener_conexion().commit()
        return cursor.rowcount > 0

    @classmethod
    def listar_todos(cls):
        cursor = Conexion.obtener_cursor()
        cursor.execute(
            'SELECT cedula, nombre, apellido, email, servicio, descripcion, precio FROM Servicio'
        )
        filas = cursor.fetchall()
        columnas = [columna[0] for columna in cursor.description]
        return [dict(zip(columnas, fila)) for fila in filas]


if __name__ == '__main__':
    print(Conexion.obtener_conexion())
    print(Conexion.obtener_cursor())
