A={1,2,3}
B={"a","b","c","d"}
C={"a","b"}

if __name__ == "__main__":
    print("a) ",A.__contains__(1))
    print("b) ",not B.__contains__("c"))
    print("c) ", False)
    print("d) ", {"a"}<C)
    print("e) ", C <= B)
    print("f) ", {"a","b"} < C)
    print("g) ", set() <= C)
    print("h) ", C <= set())