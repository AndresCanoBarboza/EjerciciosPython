# Menejo de excepsiones con assert

def divisors(num):
    divisors = []
    assert int(num) > 0, "Debe digitar un numero positivo."
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ') # adiferencia de las otras excepsiones, aqui se dwebe eliminar el int(imput)
    assert num.isnumeric() and int(num) > 0, "Debe ingresar un número positivo" # ya que el isnumeric ya es un metodo del Int
    #assert num.isnumeric() and int(num) > 0, "Debe ingresar un número positivo" # Tambien puede usarse esta linea y quitar el assert en la funcion
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()