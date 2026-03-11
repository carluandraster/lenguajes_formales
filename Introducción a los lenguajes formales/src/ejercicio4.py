from Sarta import Sarta

x = Sarta("aa")
y = Sarta("b")
z = Sarta("cba")

if __name__ == "__main__":
    xx = x*x
    print("xx = ", xx)
    print("|xx| = ", xx.longitud)
    xy = x*y
    print("xy = ", xy)
    print("|xy| = ", xy.longitud)
    y2x3 = y**2 * x**3
    print("y^2 * x^3 = ", y2x3)
    print("|y^2 * x^3| = ", y2x3.longitud)
    z0_xz_2 = z**0 * (x * z)**2
    print("z^0 * (x * z)^2 = ", z0_xz_2)
    print("|z^0 * (x * z)^2| = ", z0_xz_2.longitud)