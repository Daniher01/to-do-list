from datetime import datetime

class Tarea():

    def __init__(self, titulo: str, descripcion: str, completado: bool) -> None:
        self.id = id(object)
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = datetime.now()
        self.completado = completado
        
        
    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def fecha(self):
        return self.__fecha 
    
    @property
    def completado(self):
        return self.__completado
    
    @id.setter
    def id(self, id:int):
        self.__id = id
    
    @titulo.setter
    def titulo(self, titulo:str):
        self.__titulo = titulo
        
    @descripcion.setter
    def descripcion(self, descripcion:str): 
        self.__descripcion = descripcion
    
    @fecha.setter
    def fecha(self, fecha: datetime):
        self.__fecha = fecha    
    
    @completado.setter 
    def completado(self, completado: bool):
        self.__completado = completado
 