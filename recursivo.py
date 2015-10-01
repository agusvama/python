#recursivo.py
Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
fac = lambda f: lambda n: (1 if n<2 else n*f(n-1))
print [ Y(fac)(i) for i in range(10) ]

fib = lambda f: lambda n: 0 if n == 0 else (1 if n == 1 else f(n-1) + f(n-2))
print [ Y(fib)(i) for i in range(20) ]
