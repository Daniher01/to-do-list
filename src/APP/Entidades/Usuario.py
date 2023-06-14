#from Tarea import Tarea

class Usuario():
    
    def __init__(self, nombre:str) -> None:
        self.id = id(object)
        self.nombre = nombre
        self.__tareas = []
    
    @property
    def id(self):
        return self.__id 
    
    @property
    def nombre(self):
        return self.__nombre 
    
    def get_tareas(self):
        return self.__tareas
    
    @id.setter
    def id(self, id:int):
        self.__id = id 
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre       
    
    def agregar_tarea(self, tarea):
        self.__tareas.append(tarea)
        return True