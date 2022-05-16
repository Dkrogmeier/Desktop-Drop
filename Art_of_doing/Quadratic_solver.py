import cmath

print("Welcome to the Quadratic Solver App")
print("\nA quadratic solution is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj\nWhere a is the real portion and bj is the imaginary portion.\n\n")
num_equations = int(input("How many equations would you like to solve today: "))

for i in range(num_equations):
    print("\nSolving Equation #" + str(i) + "\n-------------------------\n")
    A = int(input("Please enter your value of A (coefficient of x^2): "))
    B = int(input("Please enter your value of B (coefficient of x): "))
    C = int(input("Please enter your value of C (coefficient): "))

    print("\nThe solutions to " + str(float(A)) + "^2 + " + str(float(B)) + " + " + str(float(C)) + " are:")

    x1 = (-B + cmath.sqrt(B**2 - 4*A*C))/(2*A)
    x2 =(-B + cmath.sqrt(B**2 - 4*A*C))/(2*A)

    print("\n\tx1 = " + str(x1))
    print("\n\tx2 = " + str(x2))

