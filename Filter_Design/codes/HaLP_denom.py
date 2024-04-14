import sympy as sp
s = sp.symbols('s')
x = sp.symbols('x')
o = 0.5416 
B = 0.1020

s5 = -0.1621 + 1.0033j
s6 = -0.3913 + 0.4156j
s7 = -0.3916 - 0.4156j
s8 = -0.1621 - 1.0033j
Dr = sp.expand((s-s5)*(s-s6)*(s-s7)*(s-s8))
print(f"{Dr}")
s = (x**2 + o**2)/(B*x)
print('\n')
Dr_2 = sp.expand((s-s5)*(s-s6)*(s-s7)*(s-s8))
print(f"{Dr_2/9238.45426026515}") #coefficient of x^8 in order to normalize it.
print('\n')
print((0.3126*1.077)/(9238.45426026515))
