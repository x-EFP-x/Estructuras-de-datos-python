from sympy import symbols, Eq, solve, sqrt

# Definir las variables
x, y, lambda_ = symbols('x y lambda')

# Definir las ecuaciones del sistema
eq1 = Eq(3*(x - sqrt(2 - x**2))**2 + 1 + 2*lambda_*x, 2*x)
eq2 = Eq(-3*(x - sqrt(2 - x*2))**2 - 1 + 2*lambda_*(sqrt(2 - x2)), 2*sqrt(2 - x*2))
eq3 = Eq(x*2 + y*2, 2)

# Resolver el sistema de ecuaciones
soluciones = solve((eq1, eq2, eq3), (x, y, lambda_), dict=True)

# Mostrar las soluciones
for solucion in soluciones:
   print(solucion)