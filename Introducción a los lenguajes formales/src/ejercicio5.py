from Sarta import Sarta
from Lenguaje import Lenguaje

A = Lenguaje({Sarta("01"), Sarta("10")})
B = Lenguaje({Sarta("1"), Sarta("0"), Sarta("10")})

if __name__ == "__main__":
    print("A ∪ B:", A.union(B))
    print("A ∩ B:", A.intersection(B))
    print("A - B:", A.difference(B))
    print("A² = ", A**2)
    print("AB = ", A * B)