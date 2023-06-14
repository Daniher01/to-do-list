from abc import ABC, abstractmethod
from ..Entidades.Tarea import Tarea
from ..Entidades.Usuario import Usuario

class TareaRepositorio(ABC):
    
    @abstractmethod
    def obtener(self, id:int) -> Tarea:
        pass
    
    @abstractmethod
    def guardar(self, tarea:Tarea, usuario:Usuario) -> None:
        pass
     
    @abstractmethod
    def actualizar(self, tarea:Tarea) -> None:
        pass
    
    @abstractmethod
    def eliminar(self, tarea:Tarea) -> None:
        pass 
