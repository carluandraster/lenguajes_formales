from Sarta import Sarta
from Lenguaje import Lenguaje

L1 = Lenguaje({Sarta("")})
L2 = Lenguaje({Sarta("b"), Sarta("aa"), Sarta("ab"), Sarta("bb")})
L3 = Lenguaje({Sarta(""), Sarta("a"), Sarta("b"), Sarta("aa"), Sarta("bb")})
L4 = Lenguaje()

if __name__ == "__main__":
    print("a) L1 ∪ L2:", L1.union(L2))
    print("b) L1 ∪ L3:", L1.union(L3))
    print("c) L1 ∪ L4:", L1.union(L4))
    print("d) L1 ∩ L2:", L1.intersection(L2))
    print("e) L2 ∩ L3:", L2.intersection(L3))
    print("f) L3 ∩ L4:", L3.intersection(L4))
    print("g) L1 ∩ L4:", L1.intersection(L4))
    print("h) L1 - L3:", L1.difference(L3))
    print("k) L1^2 ∩ L3:", (L1**2).intersection(L3))
    print("l) L1 ∪ L2^2:", L1.union(L2**2))
