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
    
    def __cantidad_variables_en_sarta(self, sarta: Sarta) -> int:
        cantidad = 0
        for simbolo in sarta:
            if simbolo in self.__simbolos_no_terminales:
                cantidad += 1
        return cantidad
    
    def __generar_lenguaje_recursivo(self, sarta_actual: Sarta, lenguaje_generado: Lenguaje, limite_palabras: int): 
        # 1. Chequeamos si YA llegamos al límite deseado en toda la ejecución global.
        # Si es así, abortamos inmediatamente cualquier procesamiento extra.
        if len(lenguaje_generado) >= limite_palabras:
            return

        tiene_variables = False 

        for i, simbolo in enumerate(sarta_actual):
            if simbolo in self.__simbolos_no_terminales:
                tiene_variables = True
                for regla in self.__reglas_de_produccion:
                    if regla.simbolo_no_terminal == simbolo:
                        producciones_ordenadas = sorted(regla.sartas_posibles, key=lambda r: self.__cantidad_variables_en_sarta(r))

                        for sarta_posible in producciones_ordenadas:
                            # Un chequeo extra por si en el medio de este bucle otra rama ya llenó el cupo
                            if len(lenguaje_generado) >= limite_palabras:
                                return 

                            nueva_sarta = Sarta(sarta_actual[:i]) * sarta_posible * Sarta(sarta_actual[i+1:])
                            self.__generar_lenguaje_recursivo(nueva_sarta, lenguaje_generado, limite_palabras)
                
                # Acordate de nuestro break de antes para derivar por la izquierda
                break
                
        # 2. Si no tiene variables, es una sarta válida.
        if not tiene_variables:
            lenguaje_generado.add(sarta_actual)

# Prueba
if __name__ == "__main__":
    G = Gramatica(
        "S",
        {"A", "B", "S"},
        {"a", "b"},
        {
            ReglaDeProduccion("S", {Sarta("abA"), Sarta("bB")}),
            ReglaDeProduccion("A", {Sarta("aB"), Sarta("")}),
            ReglaDeProduccion("B", {Sarta("bab"), Sarta("b")})
        }
    )
    L = G.generar_lenguaje(20)
    print(L)