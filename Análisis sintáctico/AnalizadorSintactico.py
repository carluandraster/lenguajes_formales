from abc import ABC, abstractmethod
from Gramatica import Gramatica

class AnalizadorSintactico(ABC):
    """# Analizador sintáctico abstracto
    Esta clase define la interfaz para los analizadores sintácticos. Cualquier analizador sintáctico concreto debe heredar de esta clase e implementar el método `analizar`.
    
    ## Atributos:
        gramatica (Gramatica): La gramática que se utilizará para el análisis sintáctico.
    ## Métodos:
        analizar(cadena: str) -> bool: Método abstracto que debe ser implementado por las clases concretas. Este método toma una cadena de entrada y devuelve un booleano indicando si la cadena es válida según la gramática.
    """
    __gramatica: Gramatica
    
    def __init__(self, gramatica: Gramatica):
        self.__gramatica = gramatica
    
    @abstractmethod
    def analizar(self, cadena: str) -> bool:
        pass
    
    @property
    def gramatica(self):
        return self.__gramatica