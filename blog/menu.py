# blog/menu.py

def mostrar_menu_consola():
    """Muestra el menú principal solicitado por las consignas."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")
    return input("Seleccione una opción (1-7): ").strip()

def pedir_datos_nuevo_post(proximo_id):
    """
    Solicita al usuario los datos para una nueva publicación.
    Retorna los datos ingresados limpios de espacios vacíos.
    """
    print("\n--- CREAR NUEVO POST ---")
    titulo = input("Ingrese el título del post: ").strip()
    contenido = input("Ingrese el contenido del post: ").strip()
    
    print("\nEtiquetas recomendadas: Python, Django, Web, Backend, Listas")
    tags_input = input("Ingrese las etiquetas separadas por coma (ej: Python, Web): ")
    # Limpiamos los espacios de cada tag ingresado y armamos una lista
    tags = [t.strip() for t in tags_input.split(",") if t.strip()]
    
    print("\nEstados permitidos: borrador, publicado, archivado")
    estado = input("Ingrese el estado del post (por defecto 'borrador'): ").strip().lower()
    if not estado:
        estado = "borrador"
        
    return titulo, contenido, tags, estado
