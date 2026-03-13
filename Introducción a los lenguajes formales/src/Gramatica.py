from Sarta import Sarta
from Lenguaje import Lenguaje
from ReglaDeProduccion import ReglaDeProduccion

class Gramatica:
    __simbolo_inicial: Sarta
    __simbolos_no_terminales: Lenguaje
    __simbolos_terminales: Lenguaje
    __reglas_de_produccion: set[ReglaDeProduccion]
    
    def __init__(self, simbolo_inicial: Sarta, v_n: Lenguaje, v_t: Lenguaje, reglas_de_produccion: set[ReglaDeProduccion]):
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
    def simbolo_inicial(self, simbolo_inicial: Sarta):
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
        self.__generar_lenguaje_recursivo(self.__simbolo_inicial, Sarta(''), lenguaje_generado, max_producciones)
        return lenguaje_generado
    
    def __generar_lenguaje_recursivo(self, simbolo_actual: Sarta, cadena_actual: Sarta, lenguaje_generado: Lenguaje, max_producciones: int):
        if max_producciones >=0:
            if simbolo_actual not in self.__simbolos_no_terminales:
                lenguaje_generado.add(cadena_actual*simbolo_actual)
            else:
                for regla in self.__reglas_de_produccion:
                    if regla.simbolo_no_terminal == simbolo_actual:
                        for sarta in regla.sartas_posibles:
                            self.__generar_lenguaje_recursivo(sarta, cadena_actual, lenguaje_generado, max_producciones - 1)