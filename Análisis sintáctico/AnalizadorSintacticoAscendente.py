from typing import override
from AnalizadorSintactico import AnalizadorSintactico
from Gramatica import Gramatica

class AnalizadorSintacticoAscendente(AnalizadorSintactico):
    def __init__(self, gramatica: Gramatica):
        super().__init__(gramatica)
    
    @override
    def analizar(self, cadena: str) -> bool:
        if cadena == self.gramatica.simbolo_inicial:
            return True
        reglas_de_produccion = self.gramatica.reglas_de_produccion
        for regla in reglas_de_produccion:
            for sarta in regla.sartas_posibles:
                if cadena.__contains__(str(sarta)):
                    resultado = self.analizar(cadena.replace(str(sarta), regla.simbolo_no_terminal))
                    if resultado:
                        return True
        return False