# 🎵 GestionDeDiscos 🪩

Una herramienta Python para gestionar tu colección de discos utilizando las APIs de Discogs y Notion. Organiza tu música en categorías y mantén un registro profesional de tu colección.

## ✨ Características Principales
- 🔍 Búsqueda en tiempo real en la base de datos de Discogs
- 🗄️ Almacenamiento estructurado en Notion
- 📂 Categorización inteligente (Colección, Deseos, Escuchar más tarde)
- 🖼️ Inclusión automática de portadas de discos
- 📅 Detección del año de lanzamiento
- 🔄 Interfaz interactiva de línea de comandos (CLI)

## ⚙️ Configuración
### Requisitos previos
#### Discogs API Token:
- Crea una cuenta en [Discogs Developers](https://www.discogs.com/developers)
- Genera tu token personal en la sección de aplicaciones

#### Notion Integration:
- Crea una integración en [Notion Integrations](https://www.notion.so/my-integrations)
- Comparte tu base de datos con la integración

### Configuración del Entorno
Añade:
```
DISCOGS_API_KEY=tu_token_discogs
NOTION_API_TOKEN=tu_token_notion
DATABASE_ID=tu_id_base_datos
```

### Estructura de la base de datos en Notion:
**Propiedades requeridas:**
- **Title** (Título)
- **Artist** (Texto enriquecido)
- **Year** (Número)
- **URL** (URL)
- **Category** (Select)
- **Cover** (Archivos y medios)

## 🎮 Uso
Ejecuta el script:
```bash
python gestion_discos.py
```
### Flujo de trabajo:
1. Introduce el nombre del álbum
2. Selecciona entre los resultados
3. Elige categoría:
   - 1️⃣ En Colección
   - 2️⃣ Lista de Deseos
   - 3️⃣ Escuchar Más Tarde

### Ejemplo de uso:
```bash
> Introduce el nombre del álbum: The Dark Side of the Moon

Disco encontrado: The Dark Side of the Moon de Pink Floyd (1973)

Selecciona una opción:
0. Disco incorrecto
1. En Colección
2. Lista de Deseos
3. Escuchar Más Tarde
> 1
```
