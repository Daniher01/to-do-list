from abc import ABC, abstractmethod

class AuthServicioRepositorio(ABC):
    
    @abstractmethod
    def isAutenticado() -> bool:
        pass