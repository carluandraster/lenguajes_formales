from Sarta import Sarta

class ReglaDeProduccion:
    __simboloNoTerminal: str
    __sartas_posibles: set[Sarta]
    
    def __init__(self, simboloNoTerminal: str, sartas_posibles: set[Sarta]):
        self.__simboloNoTerminal = simboloNoTerminal
        self.__sartas_posibles = sartas_posibles

    def __str__(self):
        return f"{self.__simboloNoTerminal} ::= {' | '.join(str(s) for s in self.__sartas_posibles)}"
    
    @property
    def simbolo_no_terminal(self):
        return self.__simboloNoTerminal
    
    @simbolo_no_terminal.setter
    def simbolo_no_terminal(self, simboloNoTerminal: str):
        self.__simboloNoTerminal = simboloNoTerminal
    
    @property
    def sartas_posibles(self):
        return self.__sartas_posibles
    
    def agregar_sarta_posible(self, sarta: Sarta):
        self.__sartas_posibles.add(sarta)
        
    def quitar_sarta_posible(self, sarta: Sarta):
        self.__sartas_posibles.discard(sarta)