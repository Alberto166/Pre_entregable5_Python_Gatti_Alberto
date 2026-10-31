# blog/operaciones.py

def mostrar_posts(lista_posts):
    """Muestra de manera formateada en consola una lista de objetos Post."""
    if not lista_posts:
        print("\n📭 No hay publicaciones para mostrar.")
        return

    print("\n" + "=" * 50)
    print(" LISTA DE POSTS DISPONIBLES")
    print("=" * 50)
    
    for post in lista_posts:
        # Accedemos a los atributos directos del objeto Post y al objeto Autor anidado
        print(f" ID: {post.id}")
        print(f" Título: {post.titulo if post.titulo else '[Sin Título]'}")
        print(f" Autor: {post.autor.nombre} ({post.autor.especialidad})")
        print(f" Tags: {', '.join(post.tags) if post.tags else 'Ninguno'}")
        print(f" Estado: {post.estado.upper()}")
        print("-" * 50)
