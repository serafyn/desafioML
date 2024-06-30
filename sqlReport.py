import mysql.connector

def get_failures_report():
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="hackad"
        )
        
        # Crear un cursor para ejecutar la consulta
        cursor = conexion.cursor(prepared=True)
        
        # Consulta SQL
        query = """
        SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer, 
               COUNT(e.status) AS failures
        FROM customers c
        JOIN campaigns ca ON c.id = ca.customer_id
        JOIN events e ON ca.id = e.campaign_id
        WHERE e.status = ?
        GROUP BY c.id
        HAVING COUNT(e.status) > 3;
        """
        
        # Ejecutar la consulta con parámetros
        cursor.execute(query, ('failure',))
        
        # Obtener los resultados
        results = cursor.fetchall()
        
        # Imprimir los resultados
        if results:
            for result in results:
                # Convertir bytearray a cadena de texto si es necesario
                customer = result[0].decode() if isinstance(result[0], bytearray) else result[0]
                print(f"Cliente: {customer}, Fallos: {result[1]}")
        else:
            print("No se encontraron fallos que cumplan con los criterios.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

# Ejecución de pruebas ante diferentes posibles escenarios de error
# Descomente las siguientes funciones para ejecutar las pruebas

# def test_invalid_credentials():
#     try:
#         conexion = mysql.connector.connect(
#             host="localhost", 
#             user="wrong_user", 
#             passwd="wrong_password", 
#             database="hackad"
#         )
#     except mysql.connector.Error as err:
#         print(f"Error al conectar con credenciales incorrectas: {err}")

# def test_empty_database():
#     conexion = None
#     try:
#         conexion = mysql.connector.connect(
#             host="localhost", 
#             user="root", 
#             passwd="", 
#             database="empty_database"  # Base de datos vacía
#         )
#         cursor = conexion.cursor(prepared=True)
#         cursor.execute("SHOW TABLES;")
#         tables = cursor.fetchall()
#         if not tables:
#             print("Base de datos vacía: No se encontraron tablas.")
#         else:
#             print("La base de datos no está vacía.")
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")

#     finally:
#         if conexion and conexion.is_connected():
#             cursor.close()
#             conexion.close()

# # Ejecutar pruebas
# print("Ejecutando prueba de credenciales incorrectas:")
# test_invalid_credentials()

# print("\nEjecutando prueba de base de datos vacía:")
# test_empty_database()

# # Fin de las pruebas

# Ejecutar la función para obtener el reporte de fallos
print("\nObteniendo el reporte de fallos:")
get_failures_report()
