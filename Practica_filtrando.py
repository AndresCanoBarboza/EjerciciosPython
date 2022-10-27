DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]



def run():
    pass

# Filtrado de lenguaje Python
# list_comprehension
# Practica equenna para utilizar disitntas formas de flitrar algunos datos de la lista DATA

    print("\nDIFERENTES FILTRADOS:\n")

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print('\nSaben Python por List:\n', all_python_devs)

    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print("\nTrabajadores de Platzipor List:\n", all_Platzi_workers)
 
    # python devs y platzi workers con filter y map
    python_devs1 = list(filter(lambda worker: worker["language"] == "python", DATA)) #primero se construye el filtro
    python_devs1 = list(map(lambda worker: worker["name"], python_devs1))    
    print("\nLenguaje con filter y Map:\n")
    
    for worker in python_devs1:
        print(worker)
 
    # Filter y Map
    adults = list(filter(lambda worker: worker["age"] > 18, DATA)) #primero se construye el filtro
    adults = list(map(lambda worker: worker["name"], adults)) # con el filtro construido se mapea solo el nombre para que solo este salga en pantalla.
    print("\nSolo adultos con filter y map:\n") # asi tira la lista como en ese formato
    for worker in adults: #con el FOR tira nombre separados por reglon.
        print(worker)

    # adultos y old_people con List_Comprehensions
    adults1 = [worker["name"] for worker in DATA if worker["age"] > 18]
    print("\nAdultos con List:\n")
    for worker in adults1:
        print(worker)

    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]
    print("\nOld_people Filtrado por List:\n")
    for worker in old_people:
        print(worker)

    # solucion para el filtrado por List y creando diccionario
    old_people3 = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    print("\nSegun aporte de Platzi con List y creando el dic:\n", old_people3)

    #Crear nueva lista de diccionarios si la persona es mayor a 70 con true or false
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    print("\nOld people con map:\n")
    for worker in old_people:
        print(worker)
    # para cada uno de los trabajadores que estan dentro de data voy a guardar un diccionario nuevo con la llave old y la clave worker mayor a 70
    # el palito es un operador para sumar diccionarios.

    
     

if __name__ == '__main__':
    run()
