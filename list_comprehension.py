def run():
    
    # Solucion sin list comprehensions
    # squares = []
    # for i in range(1,101):
    #     if i %3 != 0:
    #         squares.append(i**2)
        
    # print(squares)
    # Hasta aqui solucion sin comprehensions
    
    #Comprehensions: (element for element in iterable if condition) tradcuion: 
    #                 para cada elemento en mi iterable guardo ese elemento si se cumple condicion                  

    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    print(squares)

    challenge = [i for i in range(1,10000) if i %4 == 0 
    and i %6 == 0 and i %9 == 0]

    print("This is the Challenge:\n", challenge)

    # OTRA forma muy chiva con MCM
    #number = [i for i in range(1, 100000) if i % 36 == 0]
    #print("Otra forma encontrada en los aportes:\n", number)

    
if __name__ == '__main__':
    run() 