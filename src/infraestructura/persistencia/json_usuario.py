from app.Entidades.Usuario import Usuario
from app.Interfaces.usuario_repositorio import UsuarioRepositorio
import json

class JsonUsuario(UsuarioRepositorio):
    def __init__(self, archivo, usuario: Usuario) -> None:
        super().__init__()
        self.archivo = archivo
        self.usuario = usuario
        
    def to_dict(self):
        return {
            'nombre': self.usuario.nombre
        }    
        
    def cargar_datos(self):
        with open(self.archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos     
    
    def guardar(self):
        with open(self.archivo, "w") as archivo:
            json.dump(self.to_dict(), archivo, indent=4)
            archivo.close()
    
    def obtener(self, nombre):
        pass
    
usuario = Usuario('daniel')
enjson = JsonUsuario('datos.json', usuario)
enjson.guardar()    
enjson.cargar_datos()