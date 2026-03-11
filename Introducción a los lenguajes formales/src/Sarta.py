class Sarta(str):
    def __mul__(self, other: object) -> 'Sarta':
        otro = str(other)
        if otro =="λ":
            otro = ""
        return Sarta(super().__add__(otro))
    
    def __imul__(self, other: 'Sarta') -> 'Sarta':
        self = self * other
        return self
    
    def __pow__(self, n: int) -> 'Sarta':
        sarta_vacia = Sarta("")
        if n < 0:
            return Sarta(self[::-1]) ** (-n)
        for _ in range(n):
            sarta_vacia *= self
        return sarta_vacia
    
    @property
    def longitud(self) -> int:
        return len(self)
    
    def __str__(self) -> str:
        if self != "":
            return super().__str__()
        else:
            return "λ"