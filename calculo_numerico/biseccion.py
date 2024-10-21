def funcion(x):
    #función para encontrar la raiz
    return x**3 - x - 2  # Ejemplo: x^3 - x - 2

def biseccion(a, b, tol):
    # Verificar que la función tenga signos opuestos en los extremos
    if funcion(a) * funcion(b) >= 0:
        print("La función no tiene un cambio de signo en el intervalo dado.")
        return None
    
    iteraciones = 0
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0  # Punto medio
        if funcion(c) == 0:  # Si c es la raíz
            return c
        elif funcion(c) * funcion(a) < 0:  # La raíz está en [a, c]
            b = c
        else:  # La raíz está en [c, b]
            a = c
        iteraciones += 1
        print(f"Iteración {iteraciones}: a = {a}, b = {b}, c = {c}, f(c) = {funcion(c)}")
    
    return (a + b) / 2.0  # Retornar la aproximación de la raíz

# Solicitar datos al usuario
a = float(input("Introduce el límite inferior del intervalo (a): "))
b = float(input("Introduce el límite superior del intervalo (b): "))
tol = float(input("Introduce la tolerancia deseada: "))

# Llamar a la función de bisección
raiz = biseccion(a, b, tol)

if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")
