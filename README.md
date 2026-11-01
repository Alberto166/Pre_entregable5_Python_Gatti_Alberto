# Blog de Consola - Preentrega 6 (POO & Persistencia JSON)

Este proyecto consiste en la refactorización de un sistema de Blog modular hacia el paradigma de **Programación Orientada a Objetos (POO)**, incorporando además la persistencia de datos mediante archivos **JSON**.

##  Cambios principales respecto al checkpoint anterior
- **Migración a POO:** Se abandonó el uso estructurado de diccionarios puros para modelar el sistema mediante clases interconectadas.
- **Persistencia Física:** Los datos ahora se cargan al iniciar y se guardan al finalizar en un archivo llamado `posts.json`.
- **Manejo de Errores Exhaustivo:** El sistema previene cierres inesperados si el archivo JSON está ausente, vacío o corrupto.

##  Clases del Sistema (`blog/modelos.py`)
1. **Autor:** Representa al creador de una publicación (atributos: nombre, bio, especialidad, redes sociales). Cuenta con métodos de serialización (`to_dict` y `from_dict`).
2. **Post:** Representa un artículo del blog. Aplica **composición**, ya que su atributo `autor` almacena una instancia de la clase `Autor`.
3. **Blog:** Centraliza la lógica operativa del sistema. Almacena la lista de objetos `Post` y provee métodos para buscar por título y filtrar por etiquetas (tags).

##  Flujo de Persistencia
- **Carga (Lectura):** Al ejecutar `main.py`, el módulo `datos.py` lee `posts.json`, decodifica el texto y reconstruye los diccionarios transformándolos en instancias de objetos `Post` y `Autor`.
- **Guardado (Escritura):** Al seleccionar la opción de guardado, los objetos se mapean recursivamente a diccionarios nativos para que el módulo `json` pueda escribirlos de forma segura en el disco.

##  Cómo ejecutar el programa
1. Active el entorno virtual:
   ```bash
   .venv\Scripts\Activate.ps1
   ```
2. Ejecute el archivo orquestador principal:
   ```bash
   python main.py
   ```
