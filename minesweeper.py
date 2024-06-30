# Buscaminas: Número de Minas Vecinas
# Versión de Python: 3.11.9

def contar_minas(tablero):
    """
    Función para contar el número de minas que rodean cada celda en un tablero de Buscaminas.

    Parámetros:
    tablero (lista de lista de int): Lista 2D que representa el tablero de Buscaminas.
                                     1 representa una mina, 0 representa una celda vacía.

    Retorna:
    lista de lista de int: Lista 2D con las mismas dimensiones que el tablero de entrada,
                           donde cada celda contiene el número de minas que la rodean.
                           Si la celda en sí es una mina, se marca como 9.
    """
    # Verificar si el tablero es None o está vacío
    if tablero is None or not tablero:
        raise ValueError("El tablero de entrada no debe estar vacío o ser None.")
    
    # Verificar si el tablero es una lista de listas
    if not isinstance(tablero, list) or not all(isinstance(row, list) for row in tablero):
        raise ValueError("La entrada debe ser una lista 2D.")
    
    # Verificar si el tablero contiene solo 0s y 1s
    for row in tablero:
        if not all(cell in [0, 1] for cell in row):
            raise ValueError("El tablero debe contener solo 0s y 1s.")
    
    # Número de filas y columnas en el tablero
    num_rows = len(tablero)
    num_cols = len(tablero[0])
    
    # Direcciones para las 8 celdas vecinas (posiciones relativas)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    # Crear un nuevo tablero para almacenar el resultado con las mismas dimensiones que el tablero de entrada
    result_tablero = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Iterar a través de cada celda en el tablero
    for row in range(num_rows):
        for col in range(num_cols):
            if tablero[row][col] == 1:
                # Si la celda es una mina, marcarla como 9 en el tablero de resultado
                result_tablero[row][col] = 9
            else:
                # Inicializar un contador para el número de minas vecinas
                mine_count = 0
                # Verificar las 8 celdas vecinas
                for direction_row, direction_col in directions:
                    new_row, new_col = row + direction_row, col + direction_col
                    # Asegurarse de que la celda vecina esté dentro de los límites del tablero
                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols and tablero[new_row][new_col] == 1:
                        mine_count += 1
                # Almacenar el conteo de minas vecinas en el tablero de resultado
                result_tablero[row][col] = mine_count
    
    return result_tablero

# Ejemplo de uso
input_tablero_valido = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]
# Resultado del Tablero de ejemplo
# [
# [1, 9, 2, 1],
# [2, 3, 9, 2],
# [3, 9, 4, 9],
# [9, 9, 3, 1]
# ]

input_tablero_valido_2 = [
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 0]
]

input_tablero_valido_3 = [
  [1, 0, 0, 1],
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [1, 0, 0, 1]
]

input_tablero_valido_4 = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0]
]



# Tableros validos de ejemplos
try:
    # Generar el tablero con el conteo de minas vecinas
    output_tablero = contar_minas(input_tablero_valido)
    
    # Imprimir el tablero resultante
    for row in output_tablero:
        print(row)
except ValueError as e:
    print(e)

# # Entradas de prueba para ver el correcto funcionamiento del script
# # Descomente la siguiente seccion de codigo para ejecutar las pruebas

# input_tablero_1 = [1, 2, 3]  # No es una matriz bidimensional
# input_tablero_2 = [[0, 1, 2], [0, 1, 'a']]  # Contiene valores diferentes de 0 y 1
# input_tablero_3 = [[0, 1, -1], [0, 1, 1]]  # Contiene un número negativo
# input_tablero_4 = None  # El tablero no existe
# input_tablero_5 = []  # El tablero está vacío
# # Probar tableros inválidos
# test_tableros = [input_tablero_valido, input_tablero_valido_2, input_tablero_valido_3, input_tablero_valido_4, input_tablero_1, input_tablero_2, input_tablero_3, input_tablero_4, input_tablero_5]

# for idx, test_tablero in enumerate(test_tableros, 1):
#     try:
#         print(f"\nProbando input_tablero_{idx}:")
#         output = contar_minas(test_tablero)
#         for row in output:
#             print(row)
#     except ValueError as e:
#         print(f"Error: {e}")

# # Fin de las pruebas