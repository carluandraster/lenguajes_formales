from Sarta import Sarta

class ReglaDeProduccion:
    """# Regla de Producción
    Una regla de producción es una relación entre un símbolo no terminal y un conjunto de sartas posibles.
    Se representa de la forma: A ::= α1 | α2 | ... | αn
    Donde A es el símbolo no terminal y α1, α2, ..., αn son las sartas posibles que pueden derivar de A.
    
    ## Atributos
    - `simboloNoTerminal: str`
    El símbolo no terminal que se está definiendo.
    - `sartas_posibles: set[Sarta]`
    Un conjunto de sartas posibles que pueden derivar del símbolo no terminal.
    
    ## Métodos
    - agregar_sarta_posible(sarta: Sarta)
    Agrega una sarta posible al conjunto de sartas posibles.
    - quitar_sarta_posible(sarta: Sarta)
    Quita una sarta posible del conjunto de sartas posibles."""
    __simboloNoTerminal: str
    __sartas_posibles: set[Sarta]
    
    def __init__(self, simboloNoTerminal: str, sartas_posibles: set[Sarta]):
        """Inicializa una regla de producción con un símbolo no terminal y un conjunto de sartas posibles.
        Args:
            simboloNoTerminal (str): El símbolo no terminal que se está definiendo.
            sartas_posibles (set[Sarta]): Un conjunto de sartas posibles que pueden derivar del símbolo no terminal.
        """
        self.__simboloNoTerminal = simboloNoTerminal
        self.__sartas_posibles = sartas_posibles

    def __str__(self):
        return f"{self.__simboloNoTerminal} ::= {' | '.join(str(s) for s in self.__sartas_posibles)}"
    
    def __repr__(self):
        return self.__str__()
    
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
        """Agrega una sarta posible al conjunto de sartas posibles.
        Args:
            sarta (Sarta): La sarta posible que se desea agregar.
        """
        self.__sartas_posibles.add(sarta)
        
    def quitar_sarta_posible(self, sarta: Sarta):
        """Quita una sarta posible del conjunto de sartas posibles.
        Args:
            sarta (Sarta): La sarta posible que se desea quitar.
        """
        self.__sartas_posibles.discard(sarta)