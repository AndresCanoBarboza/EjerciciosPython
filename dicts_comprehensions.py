def run():

    dict_Challege = {}

    for i in range(1,101):
        if i %3 != 0:
            dict_Challege[i] = i**3

    dict_challenge2 = {i: i**3 for i in range(1,101) if i %3 != 0}        

    print("Challege1:\n", dict_Challege)
    
    #VERSION con conprehensions
    dict_challenge2 = {i: i**3 for i in range(1,101) if i %3 != 0} 
    # Traduccion por cada elmento en el rango de 1 a 101, voy a guardar
    #a i como llave y a i**3 como valor, solo si se cumple el if
    print("Challenge2:\n", dict_challenge2)

    #Challenge 3 ESTE trata de hacer diccionario comprehensions con el valor 
    # = a raiz cuadrada de i
    import math
    dict_challenge3 = {i: math.sqrt(i) for i in range(1,101) if i %3 != 0} 
    
    print("Challenge3:\n", dict_challenge3)



if __name__ == '__main__':
    run() 