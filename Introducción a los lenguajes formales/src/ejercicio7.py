from Sarta import Sarta
from ReglaDeProduccion import ReglaDeProduccion
from Gramatica import Gramatica

MAX_ELEM = 20
G = Gramatica(
    "S",
    {"S"},
    {"a", "b", "c", "0", "1"},
    {
        ReglaDeProduccion("S", {Sarta("a"), Sarta("b"), Sarta("c"), Sarta("Sa"), Sarta("Sb"), Sarta("Sc"), Sarta("S0"), Sarta("S1")})
    }
)
L = G.generar_lenguaje(MAX_ELEM)

def resolver(sarta: Sarta) -> None:
    if L.__contains__(sarta):
        print(f"{sarta} pertenece al lenguaje.")
    else:
        print(f"{sarta} no pertenece al lenguaje.")

resolver(Sarta("a"))
resolver(Sarta("ab0"))
resolver(Sarta("a0c01"))
resolver(Sarta("0a"))
resolver(Sarta("11"))
resolver(Sarta("aaa"))