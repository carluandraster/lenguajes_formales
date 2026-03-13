from Sarta import Sarta
from Lenguaje import Lenguaje
from ReglaDeProduccion import ReglaDeProduccion
from Gramatica import Gramatica

G = Gramatica(
    "S",
    Lenguaje({"S"}),
    Lenguaje({"a", "b", "c", "0", "1"}),
    {
        ReglaDeProduccion("S", {Sarta("a"), Sarta("b"), Sarta("c"), Sarta("Sa"), Sarta("Sb"), Sarta("Sc"), Sarta("S0"), Sarta("S1")})
    }
)