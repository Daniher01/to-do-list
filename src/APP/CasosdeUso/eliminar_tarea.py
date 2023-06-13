from Interfaces.tarea_repositorio import TareaRepositorio
from Interfaces.auth_servicio_repositorio import AuthServicioRepositorio
from Entidades.Tarea import Tarea

class EliminarTarea():
    
    def __init__(self, auth_service: AuthServicioRepositorio, tarea_repositorio: TareaRepositorio) -> None:
        self.__auth_service = auth_service
        self.__tarea_repositorio = tarea_repositorio
        
    def eliminar(self, tarea: Tarea):
        if not self.__auth_service.isAutenticado():
            return False
        self.__tarea_repositorio.eliminar(tarea)
        return True  