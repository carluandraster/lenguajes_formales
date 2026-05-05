from AutomataFinito import AutomataFinito
from numpy import str_
from numpy.typing import NDArray
from typing import override

class AutomataFinitoDeterministico(AutomataFinito):
    __delta: NDArray[str_]
    
    def __init__(self, Q: set[str], A: set[str], q0: str, F: set[str], delta: NDArray[str_]):
        super().__init__(Q, A, q0, F)
        if any(q not in Q for q in delta.flatten()):
            raise ValueError("Todas las transiciones deben ser entre estados del conjunto Q.")
        self.__delta = delta
    
    @override
    def validar_cadena(self, cadena: str) -> bool:
        estado_actual = self.q0
        for simbolo in cadena:
            if simbolo not in self.A:
                raise ValueError(f"El símbolo '{simbolo}' no pertenece al alfabeto.")
            estado_actual = self.__delta[self.Q.index(estado_actual), self.A.index(simbolo)]
        return estado_actual in self.F
    
    @property
    def delta(self) -> NDArray[str_]:
        return self.__delta