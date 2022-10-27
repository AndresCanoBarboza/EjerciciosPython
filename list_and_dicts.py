def main():
    my_list = [1, "Hellow", True, 4.5]
    my_dict = {"firstname": "Andres", "lastname": "Cano-Barboza"}

    super_list = [
        {"firstname": "Andres", "lastname": "Cano-Barboza"},
        {"firstname": "Adriana", "lastname": "Acuna-Leiva"},
        {"firstname": "Kurama", "lastname": "Chiki"},
        {"firstname": "Mila", "lastname": "Osa-Polar"},
        {"firstname": "Hashirama", "lastname": "Popi"}    
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items(): # este FOR sirve para que recorra la llave y el valor
        print(key, "-", value)            # al mismo tiempo. Siempre para diccionarios.

    for values in super_list: # Se hace el for normal para listas y anidado el FOR de diccionarios
        for key, value in values.items():
            print(key, "-", value) 

if __name__ == '__main__':
    main()