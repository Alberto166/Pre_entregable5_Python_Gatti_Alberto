# blog/validaciones.py
from blog.datos import estados_post

def validar_post_objeto(post):
    """
    Valida las propiedades de un objeto Post.
    Retorna una tupla (bool, lista_de_errores).
    """
    errores = []

    # Validar que el título no esté vacío
    if not post.titulo or not post.titulo.strip():
        errores.append("El título no puede estar vacío.")

    # Validar que el contenido no esté vacío
    if not post.contenido or not post.contenido.strip():
        errores.append("El contenido no puede estar vacío.")

    # Validar que el estado sea uno de los permitidos en la tupla global de datos.py
    if post.estado not in estados_post:
        errores.append(f"El estado '{post.estado}' es inválido. Debe ser: {', '.join(estados_post)}.")

    # Si la lista de errores está vacía, el post es válido
    es_valido = len(errores) == 0
    return es_valido, errores
