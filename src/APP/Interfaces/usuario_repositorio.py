from abc import ABC, abstractmethod
from Entidades.Usuario import Usuario

class UsuarioRepositorio(ABC):
    
    @abstractmethod
    def obtener(self, nombre: str) -> Usuario:
        pass
    
    @abstractmethod
    def guardar(self) -> None:
        pass
            