from Interfaces.tarea_repositorio import TareaRepositorio
from Interfaces.auth_servicio_repositorio import AuthServicioRepositorio
from Entidades.Tarea import Tarea
from Entidades.Usuario import Usuario

class AgregarTarea():
    
    def __init__(self, auth_service: AuthServicioRepositorio, tarea_repositorio: TareaRepositorio) -> None:
        self.__auth_service = auth_service
        self.__tarea_repositorio = tarea_repositorio
        
    def agregar(self) -> bool:
        if not self.__auth_service.isAutenticado():
            return False
        self.__tarea_repositorio.guardar(Tarea, Usuario)
        return True