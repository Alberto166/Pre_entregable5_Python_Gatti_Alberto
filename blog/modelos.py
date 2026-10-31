# blog/modelos.py

class Autor:
    def __init__(self, nombre, bio, especialidad=None, redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad if especialidad else "No especificada"
        self.redes_sociales = redes_sociales if redes_sociales else []

    def to_dict(self):
        """Convierte la instancia de Autor a un diccionario para JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def from_dict(cls, data):
        """Crea una instancia de Autor a partir de un diccionario."""
        if not data:
            return None
        return cls(
            nombre=data.get("nombre", "Anónimo"),
            bio=data.get("bio", ""),
            especialidad=data.get("especialidad"),
            redes_sociales=data.get("redes_sociales")
        )


class Post:
    def __init__(self, id_post, titulo, contenido, autor, tags=None, estado="borrador"):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # Instancia de la clase Autor (Composición)
        self.tags = tags if tags else []
        self.estado = estado

    def to_dict(self):
        """Convierte la instancia de Post a un diccionario para guardar en JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict() if isinstance(self.autor, Autor) else self.autor,
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, data):
        """Reconstruye un objeto Post a partir del diccionario de JSON."""
        autor_data = data.get("autor")
        if isinstance(autor_data, dict):
            autor_obj = Autor.from_dict(autor_data)
        else:
            autor_obj = Autor(nombre=str(autor_data), bio="")

        return cls(
            id_post=data.get("id"),
            titulo=data.get("titulo", ""),
            contenido=data.get("contenido", ""),
            autor=autor_obj,
            tags=data.get("tags", []),
            estado=data.get("estado", "borrador")
        )


class Blog:
    def __init__(self):
        # Atributo principal: lista de objetos Post
        self.posts = []

    def agregar_post(self, post):
        """Agrega un objeto Post a la lista."""
        self.posts.append(post)

    def obtener_todos(self):
        """Retorna todos los posts cargados."""
        return self.posts

    def buscar_por_titulo(self, termino):
        """Busca posts cuyo título contenga el término (case-insensitive)."""
        termino_clean = termino.strip().lower()
        if not termino_clean:
            return []
        return [p for p in self.posts if termino_clean in p.titulo.lower()]

    def filtrar_por_tag(self, tag):
        """Filtra posts que tengan el tag especificado (case-insensitive)."""
        tag_clean = tag.strip().lower()
        if not tag_clean:
            return []
        return [p for p in self.posts if tag_clean in [t.lower() for t in p.tags]]
