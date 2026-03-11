from Sarta import Sarta

class Lenguaje(set[Sarta]):
    def __mul__(self, other: object) -> 'Lenguaje':
        if not isinstance(other, Lenguaje):
            return NotImplemented
        result = Lenguaje()
        for sarta1 in self:
            for sarta2 in other:
                result.add(sarta1 * sarta2)
        return result
    
    def __pow__(self, exponent: int) -> 'Lenguaje':
        result = Lenguaje()
        if exponent < 0:
            for sarta in self:
                result.add(sarta**-1)  # Invertir la sarta para exponentes negativos
            result = result**-exponent  # Elevar al positivo para obtener el resultado correcto
        elif exponent == 0:
            result.add(Sarta(''))  # El lenguaje con la cadena vacía
        else:
            result = self
            for _ in range(1, exponent):
                result *= self
        return result
    
    def __str__(self) -> str:
        return "{" + ", ".join(str(sarta) for sarta in self) + "}"