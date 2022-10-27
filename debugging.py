# Ejemplo, encontrar el erro con Debugging y ejemplo de manejo de excepciones.

def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Solo puede digitar valores positivos.")
        for i in range(1, num + 1):
            if num % i == 1:
                divisors.append(i)
    except ValueError as ve:
        print(ve)
        return False
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    except TypeError:
        print("Debés ingresar un número.")

if __name__ == '__main__':
    run()