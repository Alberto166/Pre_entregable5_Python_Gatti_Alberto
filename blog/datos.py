# blog/datos.py
import json
import os
from blog.modelos import Post, Autor

# Nombre del archivo donde se guardará todo
ARCHIVO_JSON = "posts.json"

# Constantes globales que ya estaban definidas
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Listas"}

# Perfil por defecto de la preentrega 5
perfil_autor_defecto = {
    "nombre": "Alberto Gatti",
    "bio": "Analista de Datos.",
    "especialidad": "Python y SQL",
    "redes_sociales": ["alberto@gmail.com", "@albertogatti@ag.com"]
}

def obtener_posts_preentrega_5():
    """Retorna la lista de datos iniciales basada exactamente en la pre_entrega anterior."""
    autor_obj = Autor.from_dict(perfil_autor_defecto)
    return [
        Post(1, "Primeros pasos con Python", "En este post veremos cómo empezar a programar con Python.", autor_obj, ["Python", "Principiantes"], "publicado"),
        Post(2, "Qué es Django", "Django es un framework web creado con Python.", autor_obj, ["Python", "Django", "Web"], "borrador"),
        Post(3, "Organizando datos con listas", "Las listas permiten guardar varios elementos en una sola variable.", autor_obj, ["Python", "Listas"], "archivado"),
        # Mantenemos el post con error intencional para las pruebas de validación
        Post(4, "", "Contenido de prueba con errores", Autor("Ana López", ""), ["Python"], "invalido")
    ]

def cargar_datos_json():
    """Lee el archivo posts.json. Si no existe, genera los datos iniciales de la Preentrega 5."""
    if not os.path.exists(ARCHIVO_JSON):
        print(f" El archivo '{ARCHIVO_JSON}' no existe. Cargando datos iniciales de la Preentrega 5...")
        posts_iniciales = obtener_posts_preentrega_5()
        # Guardamos inmediatamente para crear el archivo físico por primera vez
        guardar_datos_json(posts_iniciales)
        return posts_iniciales

    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            lista_dicts = json.load(f)
            
            if not isinstance(lista_dicts, list):
                print(" Error: Estructura interna del JSON inválida.")
                return []
                
            # Reconstrucción de diccionarios a Objetos reales (Deserialización)
            return [Post.from_dict(d) for d in lista_dicts]

    except (json.JSONDecodeError, FileNotFoundError):
        print(" Error al procesar posts.json. Iniciando con blog vacío.")
        return []

def guardar_datos_json(lista_objetos_posts):
    """Convierte los objetos Post a diccionarios y los escribe en posts.json."""
    try:
        # Conversión de Objetos a Diccionarios (Serialización)
        lista_dicts = [post.to_dict() for post in lista_objetos_posts]
        
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f" Error al guardar datos: {e}")
        return False
