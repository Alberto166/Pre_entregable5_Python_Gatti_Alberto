# main.py
from blog.modelos import Blog, Post, Autor
from blog.datos import cargar_datos_json, guardar_datos_json, perfil_autor_defecto
from blog.menu import mostrar_menu_consola, pedir_datos_nuevo_post
from blog.operaciones import mostrar_posts
from blog.validaciones import validar_post_objeto

def iniciar_programa():
    # 1. Instanciamos la clase central Blog
    mi_blog = Blog()
    
    # 2. Cargamos los datos desde posts.json al arrancar el sistema
    posts_cargados = cargar_datos_json()
    for post in posts_cargados:
        mi_blog.agregar_post(post)
        
    while True:
        opcion = mostrar_menu_consola()
        
        if opcion == "1":
            # Opción 1: Ver todos los posts
            mostrar_posts(mi_blog.obtener_todos())
            
        elif opcion == "2":
            # Opción 2: Buscar por título (método de Blog)
            termino = input("\n Ingrese el título o palabra a buscar: ")
            resultados = mi_blog.buscar_por_titulo(termino)
            mostrar_posts(resultados)
            
        elif opcion == "3":
            # Opción 3: Filtrar por tag (método de Blog)
            tag = input("\n Ingrese la etiqueta para filtrar: ")
            resultados = mi_blog.filtrar_por_tag(tag)
            mostrar_posts(resultados)
            
        elif opcion == "4":
            # Opción 4: Crear nuevo post
            # Calculamos el próximo ID numérico de forma segura
            posts_actuales = mi_blog.obtener_todos()
            proximo_id = max([p.id for p in posts_actuales], default=0) + 1
            
            titulo, contenido, tags, estado = pedir_datos_nuevo_post(proximo_id)
            
            # Usamos el perfil de autor por defecto que venías usando
            autor_obj = Autor.from_dict(perfil_autor_defecto)
            
            # Instanciamos el objeto de la clase Post
            nuevo_post = Post(proximo_id, titulo, contenido, autor_obj, tags, estado)
            
            # Lo incorporamos a la instancia de Blog
            mi_blog.agregar_post(nuevo_post)
            print(f"\n ¡Post '{titulo}' creado localmente y agregado al Blog con ID {proximo_id}!")
            print(" Recuerde seleccionar la opción 6 si desea guardarlo en el archivo JSON.")
            
        elif opcion == "5":
            # Opción 5: Validar posts
            print("\n--- VALIDACIÓN DE PUBLICACIONES ---")
            posts_actuales = mi_blog.obtener_todos()
            hay_errores_globales = False
            
            for post in posts_actuales:
                es_valido, lista_errores = validar_post_objeto(post)
                if not es_valido:
                    hay_errores_globales = True
                    print(f" Post ID {post.id} ('{post.titulo if post.titulo else 'SIN TITULO'}') tiene errores:")
                    for err in lista_errores:
                        print(f"   • {err}")
            
            if not hay_errores_globales:
                print(" ¡Todos los posts cargados en el sistema son válidos!")
                
        elif opcion == "6":
            # Opción 6: Guardar posts en JSON
            exito = guardar_datos_json(mi_blog.obtener_todos())
            if exito:
                print(" ¡Persistencia JSON completada con éxito!")
                
        elif opcion == "7":
            # Opción 7: Salir
            print("\n ¡Gracias por usar el Blog de Consola POO! Hasta luego.")
            break
            
        else:
            print("\n Opción incorrecta. Por favor, ingrese un número del 1 al 7.")

# Proteger la ejecución principal solicitado por los requerimientos técnicos
if __name__ == "__main__":
    iniciar_programa()
