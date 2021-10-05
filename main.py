# Made with-in venv
# Solving a quadrativ equation

print("Hey, I can help you with solving your Quadratic Equations.")
print("Assuming the general Form of the a Quadratic Equation as Ax^2 + Bx +C = 0.")

A = int(input("Enter A : "))
B = int(input("Enter B : "))
C = int(input("Enter C : "))

type = [int, float]
D = (B ** 2 - 4 * A * C)
det = 0
D_str = str(D)
D_int = int(D)
root_types = ['equal', 'distinctive', 'Imaginary']

root_type = 0
summary = 0


def int_or_float(value):
    value_int = int(value)
    if value_int == value:
        return 0
    else:
        return 1


# For last, I'm import A Module(Math)
from math import gcd

if D == 0:
    root_type = root_types[0]
    summary = """The Roots For Your Quadratic Equation are Real and Equal.
    The Determinant Value of your Equation is equal to 'Zero'.
    Your Roots are """
    det = 0
    alpha = beta = (-B)/(2*A)
    i_f = int_or_float(alpha)
    if i_f == 0:
        set1 = (int(alpha), int(beta))
        pass
    elif i_f == 1:
        div = gcd(-B, 2*A)
        frac_num = -B/div
        frac_den = 2*A/div
        frac = str(int(frac_num))+"/"+str(int(frac_den))
        set1 = (frac, frac)
        pass
    print(summary)
    print(set1)
elif D > 0:
    root_type = root_types[1]
    summary = """The Roots For Your Quadratic Equation are Real and Distinctive.
    The Determinant Value of your Equation is Greater than 'Zero'.
    Your Roots are """
    det = (D_int)**0.5
    i_f = int_or_float(det)
    if i_f == 0:
        alpha = (-B + int(det))/(2*A)
        beta = (-B - int(det))/(2*A)
        if1 = int_or_float(alpha)
        if2 = int_or_float(beta)
        if if1 == 0:
            alpha = int(alpha)
            pass
        elif if1 == 1:
            div1 = gcd(-B + int(det), 2*A)
            frac_num = (-B + int(det)) / div1
            frac_den = 2 * A / div1
            frac = str(int(frac_num)) + "/" + str(int(frac_den))
            alpha = frac
            pass
        if if2 == 0:
            beta = int(beta)
            pass
        elif if1 == 1:
            div1 = gcd(-B - int(det), 2 * A)
            frac_num = (-B - int(det)) / div1
            frac_den = 2 * A / div1
            frac = str(int(frac_num)) + "/" + str(int(frac_den))
            beta = frac
            pass
        set1 = (alpha, beta)
        print(summary)
        print(set1)
        pass
    elif i_f == 1:
        det = "(" + D_str + ")^/2"
        alpha = "("+str(-B)+" + "+det+")/"+str(2*A)
        beta = "(" + str(-B) + " - " + det + ")/" + str(2 * A)
        set1 = (alpha, beta)
        print(summary)
        print(set1)
elif D < 0:
    root_type = root_types[2]
    summary = """The Roots For Your Quadratic Equation are Imaginary.
    Their Determinant Value is Lesser than 'Zero'.
    Your Roots are """
    if B == 0:
        det = "(" + D_str + ")^1/2"
        alpha = "(" + det + ")/" + str(2 * A)
        beta = "(" + det + ")/" + str(2 * A)
        set1 = (alpha, beta)
        print(summary)
        print(set1)
        pass
    else:
        det = "(" + D_str + ")^/2"
        alpha = "(" + str(-B) + " + " + det + ")/" + str(2 * A)
        beta = "(" + str(-B) + " - " + det + ")/" + str(2 * A)
        set1 = (alpha, beta)
        print(summary)
        print(set1)
        pass
    pass
