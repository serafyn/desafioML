# REST API: Mejores Series de TV por Género
# Versión de Python: 3.11.9

import requests
import re

genre = "Action"

def sanitize_input(input_str):
    # Elimina cualquier caracter no alfanumérico excepto espacios
    sanitized_str = re.sub(r'[^\w\s]', '', input_str)
    return sanitized_str

def bestInGenre(genre):
    # Valida y sanitiza la entrada del género
    if not isinstance(genre, str) or not genre.strip():
        raise ValueError("El género debe ser una cadena no vacía.")
    
    genre = sanitize_input(genre)
    
    url = "https://jsonmock.hackerrank.com/api/tvseries"
    page = 1
    best_show = None

    while True:
        try:
            response = requests.get(url, params={'page': page})
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Ocurrió un error al realizar la solicitud API: {e}")
            break
        
        data = response.json()
        
        # Valida la estructura de la respuesta API
        if not isinstance(data, dict) or 'data' not in data or 'total_pages' not in data:
            print("Estructura de respuesta inválida.")
            break
        
        shows = data['data']
        
        if not shows:
            break
        
        for show in shows:
            # Valida la estructura de cada serie
            if 'genre' not in show or 'imdb_rating' not in show or 'name' not in show:
                print("Datos de serie inválidos.")
                continue
            
            if genre.lower() in show['genre'].lower():
                if best_show is None or show['imdb_rating'] > best_show['imdb_rating'] or \
                   (show['imdb_rating'] == best_show['imdb_rating'] and show['name'] < best_show['name']):
                    best_show = show
        
        if page >= data['total_pages']:
            break
        
        page += 1
    
    return best_show['name'] if best_show else None

result = bestInGenre(genre)
print(f"La mejor serie en el género '{genre}' es: {result}")

# # Entradas de prueba para el script Mejores Series de TV por Género
# test_inputs = [
#     "Action",                   # Género válido
#     "Comedy",                  # Género válido
#     "Science Fiction",          # Género que podría no existir en el conjunto de datos
#     "DraMA",                    # Género con mayúsculas y minúsculas mezcladas
#     "<script>alert('XSS')</script>",  # Intento de XSS
#     "'; SELECT * FROM tvseries;--",   # Intento de inyección SQL
#     "Acción; SELECT * FROM users;",   # Inyección SQL con género válido
#     " ",                       # Género vacío
# ]

# def run_tests(inputs):
#     for genre in inputs:
#         print(f"Probando género: {genre}")
#         try:
#             result = bestInGenre(genre)
#             print(f"Resultado: {result}\n")
#         except ValueError as e:
#             print(f"Error: {e}\n")

# # Ejecutar las pruebas
# run_tests(test_inputs)

# # Fin de las pruebas
