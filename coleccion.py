import requests
from notion_client import Client
import json

# Configuración
DISCOGS_API_KEY = 'your_discogs_api_key_here'  # Reemplazar con tu token real
NOTION_API_TOKEN = 'your_notion_api_token_here'  # Reemplazar con tu token real
DATABASE_ID = 'your_notion_database_id_here'  # Reemplazar con tu database ID real

# Inicializar cliente de Notion
notion = Client(auth=NOTION_API_TOKEN)

# Función para buscar discos en Discogs
def search_discogs(query):
    url = f'https://api.discogs.com/database/search'
    params = {
        'q': query,
        'token': DISCOGS_API_KEY,
        'type': 'release'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en Discogs: {response.status_code}")
        return None

# Función para agregar un disco a Notion
def add_to_notion(title, artist, year, url, image_url, category):
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "Artist": {
                "rich_text": [
                    {
                        "text": {
                            "content": artist
                        }
                    }
                ]
            },
            "Year": {
                "number": year
            },
            "URL": {
                "url": url
            },
            "Category": {
                "select": {
                    "name": category
                }
            },
            "Cover": {
                "files": [
                    {
                        "name": f"{title}.jpg",
                        "external": {
                            "url": image_url
                        }
                    }
                ]
            }
        }
    )

# Función principal para buscar y agregar discos
def main():
    while True:  # Bucle para permitir múltiples búsquedas
        query = input("Introduce el nombre del álbum que deseas buscar (o escribe 'salir' para terminar): ")
        
        if query.lower() == 'salir':
            print("Programa terminado. ¡Hasta luego!")
            break

        results = search_discogs(query)

        if results and results.get('results'):
            # Ordenar por año de lanzamiento
            results_sorted = sorted(
                results['results'], 
                key=lambda x: int(x.get('year', 9999)) if x.get('year') and str(x.get('year')).isdigit() else 9999
            )
            # Seleccionar el disco más antiguo
            oldest = results_sorted[0]
            title_artist = oldest.get('title', 'Título no disponible')
            year = oldest.get('year', 'Año no disponible')
            url = "https://www.discogs.com" + oldest.get('uri', '')
            
            # Obtener URL de la imagen
            image_url = oldest.get('cover_image', '')

            # Separar título y artista por el guion
            if ' - ' in title_artist:
                artist, title = title_artist.split(' - ', 1)
            else:
                artist = 'Artista desconocido'
                title = title_artist
            
            print(f"\nDisco encontrado: {title} de {artist} ({year})")

            # Preguntar si el disco es correcto o no
            print("\nSelecciona una opción:")
            print("0. Disco incorrecto (volver a buscar otro disco)")
            print("1. En Colección")
            print("2. Lista de Deseos")
            print("3. Escuchar Más Tarde")
            category_option = input("Introduce el número de la categoría: ")

            # Si selecciona '0', vuelve a la búsqueda
            if category_option == '0':
                continue

            # Mapear la selección a nombres de categorías en español
            category_map = {
                "1": "En Colección",
                "2": "Lista de Deseos",
                "3": "Escuchar Más Tarde"
            }
            category = category_map.get(category_option, "Lista de Deseos")  # Por defecto: Lista de Deseos

            # Agregar a Notion
            add_to_notion(title, artist, int(year) if year.isdigit() else 0, url, image_url, category)
            print(f"Disco '{title}' agregado a la categoría '{category}' en tu base de datos de Notion.")
        
        else:
            print("No se encontraron discos.")

# Ejecutar el script
if __name__ == "__main__":
    main()
