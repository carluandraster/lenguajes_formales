from abc import ABC, abstractmethod

class AutomataFinito(ABC):
    __q: list[str]
    __a: list[str]
    __q0: str
    __f: set[str]
    
    def __init__(self, Q: set[str], A: set[str], q0: str, F: set[str]):
        if not F.issubset(Q):
            raise ValueError("Los estados finales deben ser parte del conjunto de estados.")
        self.__q = list(Q)
        self.__a = list(A)
        self.__q0 = q0
        self.__f = F
    
    @abstractmethod
    def validar_cadena(self, cadena: str) -> bool:
        pass
    
    @property
    def Q(self) -> list[str]:
        return self.__q
    
    @property
    def A(self) -> list[str]:
        return self.__a
    
    @property
    def q0(self) -> str:
        return self.__q0
    
    @property
    def F(self) -> set[str]:
        return self.__f