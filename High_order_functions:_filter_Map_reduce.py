my_list = [1,2,3,4,5]

# list_comprehension

odd = [i for i in my_list if i % 2!= 0]
print("Odd List_comprehension:",odd)

# using Filter
oddF = list(filter(lambda x: x%2 != 0, my_list))
print("Odd Filter:",oddF)


# list_comprenhension
square_listcomp = [i**2 for i in my_list] # Para esa i en mi lista, coy a colocar esa i al cuadrado
print("Square List Comprehension:",square_listcomp) 

# using map
square_map = list(map(lambda x: x**2, my_list)) # esa x, que recibe de my_list, elevela al cuadrado
print("Square Map:",square_map)

# using reduce
# multiplica los elementos a un unico valor 

# with for
all_multiplied = 1

for i in my_list:
    all_multiplied = all_multiplied * i

print("Multiplicar digitos con FOR:",all_multiplied)

# using Reduce
from functools import reduce

all_multipliedR = reduce(lambda a, b: a * b, my_list) # a y b corresponden al primero y segundo numero y con cada iteracioncambia 

print("Multiplicar digitos con Reduce:",all_multipliedR)