from Sarta import Sarta
from Lenguaje import Lenguaje
from ReglaDeProduccion import ReglaDeProduccion

class Gramatica:
    __simbolo_inicial: str
    __simbolos_no_terminales: set[str]
    __simbolos_terminales: set[str]
    __reglas_de_produccion: set[ReglaDeProduccion]
    
    def __init__(self, simbolo_inicial: str, v_n: set[str], v_t: set[str], reglas_de_produccion: set[ReglaDeProduccion]):
        self.__simbolo_inicial = simbolo_inicial
        self.__simbolos_no_terminales = v_n
        self.__simbolos_terminales = v_t
        self.__reglas_de_produccion = reglas_de_produccion

    def __str__(self):
        reglas_str = '\n'.join(str(regla) for regla in self.__reglas_de_produccion)
        return f"Símbolo Inicial: {self.__simbolo_inicial}\nReglas de Producción:\n{reglas_str}"
    
    @property
    def simbolo_inicial(self):
        return self.__simbolo_inicial
    
    @simbolo_inicial.setter
    def simbolo_inicial(self, simbolo_inicial: str):
        self.__simbolo_inicial = simbolo_inicial
    
    @property
    def reglas_de_produccion(self):
        return self.__reglas_de_produccion
    
    def agregar_regla_de_produccion(self, regla: ReglaDeProduccion):
        self.__reglas_de_produccion.add(regla)
        
    def quitar_regla_de_produccion(self, regla: ReglaDeProduccion):
        self.__reglas_de_produccion.discard(regla)
    
    def generar_lenguaje(self, max_producciones: int) -> Lenguaje:
        lenguaje_generado = Lenguaje()
        self.__generar_lenguaje_recursivo(Sarta(self.__simbolo_inicial), lenguaje_generado, max_producciones)
        return lenguaje_generado
    
    def __generar_lenguaje_recursivo(self, sarta_actual: Sarta, lenguaje_generado: Lenguaje, max_producciones: int):
        tiene_variables = False
        if max_producciones > 0:
            for i, simbolo in enumerate(sarta_actual):
                if simbolo in self.__simbolos_no_terminales:
                    tiene_variables = True
                    for regla in self.__reglas_de_produccion:
                        if regla.simbolo_no_terminal == simbolo:
                            for sarta_posible in regla.sartas_posibles:
                                nueva_sarta = Sarta(sarta_actual[:i] + sarta_posible + sarta_actual[i+1:])
                                self.__generar_lenguaje_recursivo(nueva_sarta, lenguaje_generado, max_producciones - 1)
            if not tiene_variables:
                lenguaje_generado.add(sarta_actual)