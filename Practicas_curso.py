

""" #COMENTARIO MASIVO



### 00 - Ejemplo

print("\n\nEjercicio 00\n")
print("input")
algo = input("Dime algo...")
print("Mmm...", algo, "...¿En serio?")


### 01 - Forma incorrecta de jalar un número para operar con el INPUT)

#print("\n\nEjercicio 01\n")
#cualquierNumero = input("Inserta un número: ")
#algo = cualquierNumero ** 2.0
#print(cualquierNumero, "al cuadrado es", algo)


### 02 - Forma correcta de utilizar INPUT con alguna operación, se
print("\n\nEjercicio 02\n")
# convierte la entrada a un float o int

print("Uso correcto de INPUT para convertir de string a int o float")
algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)


### 03 - Convertir entrada numero a string

print("\nEjercicio 03\n")
print("convertir entrada numérica de input a string para concatenar con uso del +")
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))
print("")

### 04 - Otro ejemplo del uso correcto del INPUT con PRINT

print("\n\nEjercicio 04\n")
print("Otro ejemplo correcto de INPUT")
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)
# aquí se puede eliminar hipo y solo poner en print la formula


### 05 - Uso de concatenación con +, solo mismo tipo de variable

print("\n\nEjercicio 05\n")
print("Uso de concatenación con +, solo mismo tipo de variable")
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")


### 06 - El * en el print imprime la cantidad de veces específicada al string

print("\n\nEjercicio 06\n")
print("El * en el print imprime la cantidad de veces específicada al string")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


### 07 - PRÁTICA

print("\n\nEjercicio 07\n")
print("Práctica")
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))

print ("El resultado de sumar", num1, "+", num2, "es:", num1+num2)
print ("El resultado de restar " + str(num1) + " - " + str(num2) + " es: " + str(num1 - num2)) # Usando el convertidor de float a str
print ("El resultado de multiplicar", num1, "por", num2, "es:", num1*num2)
print ("El resultado de dividir " + str(num1) + " entre " + str(num2) + " es: " + str(num1/num2))

print("\n¡Eso es todo, amigos!")


### 08 - En caso de que quiera guardar una respuesta boolena con operadores en una variable

#print("Ejercicio 08\n")
#respuesta = numerodeLeones >= numerodeLeonas


### 09 - Utilizar comparadores para varios usos.

print("\n\nEjercicio 09\n")
n = int(input("Digita un número entero: ")) #recordar que python simpre ingresa string entonces se debe usar el int o el float
print(n <= 100)
print(n >= 100)


### IF-else anidado SOLO EJEMPLO DE SINTAXIS

#print("\n\nEjercicio 10\n")
#if climaBueno:
 #   iraCaminar()
#elif hayBoletosDisponibles:
 #   IralCine()
#elif mesasLibres:
 #   almorzar()
#else:
 #   jugarAjedrezEnCasa()


### 10 - Ejercicio con IF-else

#print("\n\nEjercicio 10\n")
#lee dos números
#numero1 = int (input("Ingresa el primer número:"))
#numero2 = int (input("Ingresa el segundo número:"))

##elegir el número más grande
#if numero1 > numero2:
#   nmasGrande = numero1
#else:
 #   nmasGrande = numero2

##imprimir el resultado
#print("El número más grande es:", nmasGrande)


### 11 -Practica con if-else y elif anidado

print("\n\nEjercicio 11\n")
planta = input("Ingrese el nombre de la planta que desea: ")
if planta == "Espatifilo":
    print("Sí, El Espatifilo es la mejor planta de todos los tiempos!")
elif planta == "espatifilo":
    print("No, quiero un gran Espatifilo!")
else:
    print("Espatifilo! No " + planta)

    
### Practica con if-else 

print("\n\nEjercicio 12\n")
ingreso=float(input("Ingrese el ingreso anual: "))

if ingreso < 85528:
    IPI = (ingreso*0.18) - 556.2
if IPI < 0: 
    IPI = 0.0
else:
    IPI = 14839.2 + (0.32 * (ingreso - 85528))

IPI=round(IPI, 0)
print("El impuesto es:",IPI, "pesos")


### 13 - Practica if-elif-else

print("\n\nEjercicio 13\n")
año = int(input("Introduzca un año: "))

if año <= 1581:
    print("Debe digitar un año del periodo del calendario Gregoriano (mayor o igual a 1582).")
elif año % 4 != 0 and año % 100 != 0:
    print("El año", año, "es común.")
else:
    print("El año", año, "es bisiesto.")


### 14 - Ejemplo de while

print("\n\nEjercicio 14\n")
# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

## lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))
if numero == 0:
        print("Usted ha salido del programa")
        exit()
## 0 termina la ejecución
while numero != 0:
    
   # verificar si el número es impar
   
    if numero % 2 == 1:
        # aumentar el contador de números impares
        numerosImpares += 1
    else:
       # aumentar el contador de números pares
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

## imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)


### 15 - Práctica de WHILE

print("\n\nEjercicio 15\n")
numeroSecreto = 777





print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")



num = int(input("Digita un numero: "))
while num != 777:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    num = int(input("Digitá un nuevo número: "))
print ("¡Bien hecho, muggle! Sos libre ahora\n") 


    
### 16 - FOR con rango

print("\n\nEjercicio 16\n")
for i in range (2, 8): # puede ser rango como este o por ejemplo un número (100)
    print("El valor de i es actualmente", i)


### 17 - FOR con aumento definido

print("\n\nEjercicio 17\n")
for i in range(2, 8, 3): # El 3 indica aumentar cada cuanto, es opcional
    print("El valor de i es actualmente", i)


### 18 - Práctica FOR

print("\n\nEjercicio 18\n")
import time

for i in range (1,6):
    print (i, "Mississippi") 
    time.sleep (1) #Esto sirve para atrasar 1s la impresión


### 19 - Ejemplo de BREAK y CONTINUE

print("\n\nEjercicio 19\n")
## break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 4:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

## continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")


### 20 - BREAK con WHILE

print("\n\nEjercicio 20\n")
numeroMayor = -99999999
contador = 0

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador = 1 #aqui el contador es para controlar si cierra o avanza en el siguiente if
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 

### 21 - CONTINUE con WHILE

print("\n\nEjercicio 21\n")
numeroMayor = -99999999
contador = 0

numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

while numero != -1:
    if numero == -1:
        continue
    contador = 1

    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

if contador:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número")


### 22 - Practica de BREAK y WHILE

print("\n\nEjercicio 22\n")
keyWord = "chupacabra"

while True:
    word = input("Ingrese una palabra. (Digite \"chupacabra\" para salir): ")
    if word == keyWord:
        break
print("\n¡Has dejado el ciclo con éxito!")


### 23 - Practica CONTINUE y FOR

print("\n\nEjercicio 23\n")
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.

userWord = input ("Ingrese una palabra: ")

for letra in userWord.upper():
    if letra == "A":
        continue
    if letra == "E":
        continue
    if letra == "I":
        continue
    if letra == "O":
        continue
    if letra == "U":
        continue
    else:
        print(letra.upper())


### 24 - Practica WHILE

print("\n\nEjercicio 24\n")
bloques = int(input("Ingrese el número de bloques: "))

altura = 0
 
utilizados = 1
 
while utilizados <= bloques:
 
    altura += 1
    bloques -= utilizados       
    utilizados += 1
print("La altura de la pirámide:", altura)


### 25 - Practica con WHILE

print("\n\nEjercicio 25\n")
contaPasos = 0
c0 = int(input("Digite un número natural: "))
while c0 < 0 or c0 == 0:
    
    print ("Debe digitar un número positivo y diferente a 0.")
    c0 = int(input("Digite un número natural: "))
    
while c0 != 1:
    
    if c0 % 2 == 0:
        c0 = c0 / 2
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
    contaPasos += 1
    print (int(c0))    
print ("Se realizaron", contaPasos, "pasos.")


### 26 - Ejemplo de RECORRER string con FOR

print("\n\nEjercicio 26\n")
palabra = "Python"
for letter in palabra:
    print(letter, end = "*")


### 27 - Otro ejemplo de BREAK

print("\n\nEjercicio 27\n")
texto = "OpenEDG Python Institute"
for letter in texto:
    if letter == "P":
        break
    print(letter, end= "")


### 28 - Otro Ejemplo para CONTINUE

print("\n\nEjercicio 28\n")
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end= "")


### 29 - Otro ejemplo para ELSE en FOR o WHILE

print("\n\nEjercicio 29\n")
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")


### 30 - Uso de varRight y de varLeft

#La computadora realiza el mismo tipo de operación,
#pero con una diferencia: como dos es la base para
#los números binarios (no 10), desplazar un valor un
#bit a la izquierda corresponde a multiplicarlo por
#dos ; respectivamente, desplazar un bit a la derecha
#es como dividir entre dos (observe que se pierde el
#bit más a la derecha).

print("\n\nEjercicio 30\n")
var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)


##### LISTAS ######


### 31 - LISTAS en Python, guardan varias variables y se puede modificar por
### índice además LEN cuenta la cantidad de variables. Y DEL elimina elementos

print("\n\nEjercicio 31\n")
numeros = [10, 5, 7, 2, 1] # esta es la LISTA

print("Contenido de la lista original:", numeros) # imprimiendo el contenido de la lista original

numeros [0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros [1] = numeros [4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

print("Ultimo valor de la lista:",(numeros[-1])) ### esto imprime el útlimo valor de la lista.


### 32 - Practica de LISTAS

print("\n\nEjercicio 32\n")
listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.
print("Lista Original:", listaSombrero)
## Paso 1: escribe una línea de código que solicite al usuario
## para reemplazar el número de en medio con un número entero ingresado por el usuario.
listaSombrero [2] = int(input("\nDigite el valor por el que quiera convertir el valor de en medio: "))

## Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del listaSombrero [-1]

## Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista es:", len(listaSombrero))
print("La lista contiene los valores:", listaSombrero)


### 33 - Usar METODOS en LISTAS, APPEND inserta al final e INSERT inserta donde quiera

print("\n\nEjercicio 33\n")
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)


### 34 - Llenar LISTA VACIA con APPEND y un FOR

print("\n\nEjercicio 34\n")
miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)


### 35 - SUMAR elementos de lista con SUMA

print("\n\nEjercicio 35\n")
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)): #aquí uso len para indicar al FOR el largo de la lista, por consecuencia el range
    suma += miLista[i]

print(suma)


### 36 - INTERCAMBIAR valores de una lista

print("\n\nEjercicio 36\n")
miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]
## al extremo el qie se quiere cambiar y al centro por el que se quiere cambiar

print(miLista) 

### 37 - Lo mismo pero con un FOR para listas grandes

print("\n\nEjercicio 37\n")
miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista) 


### 38 - PRACTICA con APPEND, INSERT, DEL y LEN

print("\n\nEjercicio 38\n")
## paso 1
beatles = []
print("Paso 1:", beatles)

## paso 2
beatles.append("John Lennon")
beatles.append("Paul Macrtney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

## paso 3
for musico in range(1):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
print("Paso 3:", beatles)

## etapa 4
del beatles [-1]
del beatles [-1]
print("Paso 4:", beatles)

## paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

## probando la longitud de la lista
print("Los Fab", len(beatles))

####### ORDENAMIENTOS #######

### 39 - ORDENAMIENTO BURBUJA básico

print("\n\nEjercicio 39\n")
miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)


### 40 - ORDENAMIENTO BURBUJA interactivo, haciendo lista el USUAIRO, También sirve con string

print("\n\nEjercicio 40\n")
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):  ## Intoducir elementos con el FOR en LISTA
    val = (input("Introduce un elemento de la lista: "))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)


### 41 - Ordenamiento con SORT y REVERSE

print("\n\nEjercicio 41\n")
lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort ()

print(lst) # salida: [1, 2, 3, 4, 5]

lst.reverse()
print (lst)


### 42 - CLONAR listas para no perderlas o modificarlas después

print("\n\nEjercicio 42\n")
##Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

## Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3] # El 1:3 indica el índice 1 al índice 3-1
                           # el primer índece se incluye al # en el otro no se incluye
nuevaLista = miLista[:3] # es igual a [0:3]
print("de 0 a 3",nuevaLista)                           
nuevaLista = miLista[3:]  # igual a [3:len(miLista)
print("de 3 a final",nuevaLista)                                 
nuevaLista = miLista[:]  # copia toda la lista
print("Toda",nuevaLista)      


### 43 - DEL en lista

#print("\n\nEjercicio 43\n")
#miLista = [10, 8, 6, 4, 2]
#del miLista[1:3] #Elimina parte de la lista
#print(miLista)
#del miLista # elimina lista entera
#print(miLista)





### 44 - IN y NOT IN para verificar si existe o no un elmento en lista

print("\n\nEjercicio 44\n")
miLista = [0, 3, 12, 8, 2]
if 5 in miLista: # Este if lo hice para usarlo con un aviso y no solo el true, en caso de que se deba mostrar
    print("El valor 5 está en la lista.") # Pero si es como valor bandera sirve la forma sencilla que sigue.
else:
    print("El valor 5 no está en la lista.")
print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)


## Encontrar el MAYOR en lista
miLista = [17, 33, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista:
    if i > mayor:
        mayor = i

print(mayor)

### 45 - BUSCAR un valor dado

print("\n\nEjercicio 45\n")
miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

### 46 - Otro ejemplo de BUSCAR usando el "in" 

print("\n\nEjercicio 46\n")
sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0
listnum = []
for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1
        listnum.append(numeros)

print("Ha tenido",aciertos, "aciertos.")
print("Los números acertados son:", listnum)

### 47 - Práctica LISTAS

print("\n\nEjercicio 47\n")
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in miLista:
    if i in miLista:
        del miLista[i]

print("La lista solo con elementos únicos:")
print(miLista)


### 48 - Formas de RELLENAR listas

print("\n\nEjercicio 48\n")
## cuadrados de 10 números desde cero
cuadrados = [x ** 2 for x in range(10)]
print("Cuadrados:", cuadrados)
## primeras 8 potencias del 2
dos = [2 ** i for i in range(8)]
print("dos:", dos)
## elementos impares de la lista cuadrados 
cuadrados = [x ** 2 for x in range(10)]
probabilidades = [x for x in cuadrados if x % 2 != 0] 
print(probabilidades)


### 49 - Listas de comprensión LISTAS ANIDADAS

print("\n\nEjercicio 49\n")
##crear lista
cubos = [num ** 3 for num in range (5)]
print(cubos) # salidas: [0, 1, 8, 27, 64]

# Cubo - un arreglo tridimensional (3x3x3)


### 50 - LSTAS TRIDIMENCIONALES

print("\n\nEjercicio 50\n")
cubo = [[[':(', 'x', 'x'],
        [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cubo)
print(cubo [0][0][0]) # salida: ':('
print(cubo [2][2][0]) # salida: ':)'


### FUNCIONES ###

### funciones aqui: https://docs.python.org/3/library/functions.html


### 51 - Ejemplo de Funciones

print("\n\nEjercicio 51\n")
def mensaje(): # Funcion debe estar antes de ser invocada
    print("Por favor, ingresá un valor: ")

mensaje()
a = int(input())

mensaje()
b = int(input())

mensaje()
c = int(input())

print("Los valores son:", a, "|", b, "|", c)


### 52 - Ejemplo de Funciones con parámetros

print("\n\nEjercicio 52\n")
def mensaje(que, numero):
    print("Ingresa", que, "número", numero)

mensaje("teléfono", 88)
mensaje("precio", 5)
mensaje("número", "número")


### 53 - Otro Ejemplo de Funciones con parámetros
##Es posible combinar ambos tipos si se desea, solo hay una regla inquebrantable: se deben colocar primero los
##argumentos posicionales y después los de palabras clave.

print("\n\nEjercicio 53\n")
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


### 54 - Otro Ejemplo de funciones con parámetros con palabra clave
## el toque de esto es que se puede usar la palbra clave para enviar el par[ametro, no importa el orden si est[a identificado
print("\n\nEjercicio 54\n")
def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("James", "Bond") # puede enviarse el parámetro sin el nombre de la variable o con el, como abajo
presentar(segundoNombre = "Skywalker", primerNombre = "Luke")

### 55 - Ejemplo Funciones con RETURN

print("\n\nEjercicio 55\n")
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    strangeList.reverse()  # esto sirve para darle vuelta ya que, la rellena de 4 a 0
    return strangeList 

print(strangeListFunction(5))


### 56 - Práctica con Funciones con RETUNR y NONE

print("\n\nEjercicio 56\n")
def isYearLeap(año):
   if año <= 1581:
       print("Debe digitar un año del periodo del calendario Gregoriano (mayor o igual a 1582).")
   elif año % 4 != 0 and año % 100 != 0:
       return False
   else:
       return True
        

def daysInMonth(año, month):

    diasPorMes = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(año):
        if diasPorMes[month - 1] == 28:
            return 29
        else:
            return diasPorMes[month - 1]
    else:
        return diasPorMes[month - 1]
    return None

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")


### 57 - Practica de funciones

print("\n\nEjercicio 57\n")
def l100kmtompg(liters):
    print(liters, "L/100km equivalea a:", round(235.21 / liters, 2), "mpg.")

def mpgtol100km(miles):
    print(miles, "mpg esquivale a:", round(235.21 / miles, 2), "L/100km.")


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

print("introduciendo datos el usuario.")
liters = float(input("Escriba la cantidad de L/100km para comvertir a mpg: "))
print(l100kmtompg(liters))

miles = float(input("Escriba la cantidad de mpg para comvertir a L/100km: "))
print(mpgtol100km(miles))


### 58 - Ejercicio de formula de IMC
## note como dentro de una funcion se llama a otra.

print("\n\nEjercicio 58\n")
def piespulgam(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254


def lbsakg(lb):
    return lb * 0.45359237


def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

print(imc(lbsakg(176),piespulgam(5, 7))) # nuevamente, se puede poner con o sin nombre de la variable
print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))


### 59 - Ejemplo de funciones utilizando listas como parametros

print("\n\nEjercicio 59\n")
def HolaaTodos(myList):
    for nombre in myList:
        print("Hola,", nombre)

HolaaTodos(["Adam", "John", "Lucy"])


### 60 Otro ejemplo de funciones usando lista o modificandola

print("\n\nEjercicio 60\n")
def listUpdater(lst):
    updList = []
    for elem in lst:
        elem **= 2
        updList.append(elem)
    return updList

l = [1, 2, 3, 4, 5]
print(listUpdater(l))


### 61 Uso de la plabra GLOBAL en las funciones

#El utilizar la palabra reservada dentro de una función con el nombre o nombres de las variables separados por comas,
#obliga a Python a abstenerse de crear una nueva variable dentro de la función; se empleará la que se puede acceder
#desde el exterior.

#En otras palabras, este nombre se convierte en global (tiene un alcance global, y no importa si se esta leyendo o
#asignando un valor).

print("\n\nEjercicio 61\n")

def miFuncion():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)

var = 1
miFuncion()
print(var)


### 62
#La conclusión es obvia - al cambiar el valor del parámetro este no se propaga fuera de la función
#(más específicamente, no cuando la variable es un valor escalar, como en el ejemplo).

#Esto también significa que una función recibe el valor del argumento, no el argumento en sí.
#Esto es cierto para los valores escalares.

print("\n\nEjercicio 62\n")

def miFuncion(n):
    print("Yo obtuve", n)
    n += 1
    print("Yo ahora tengo", n)

var = 1
miFuncion(var)
print(var)

## Pero en este otro caso si influye sobre la lista.
## Es esta no

def miFuncion(miLista1):
    print(miLista1)
    miLista1 = [0, 1]

miLista2 = [2, 3]
miFuncion(miLista2)
print(miLista2)

## En esta sí influye sobre la lista

def miFuncion(miLista1):
    print(miLista1)
    del miLista1[0]

miLista2 = [2, 3]
miFuncion(miLista2)
print(miLista2)


### 63 Ejemplo de barra \ Barra invertida

##Segundo, observa como el símbolo de
##diagonal invertida (\) es empleado. Si se termina una línea de código con el, Python entenderá que la línea continua en la siguiente.

print("\n\nEjercicio 63\n")
def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None  ## Si los datos son falsos o no corresponden retorna None
   
    return peso / altura ** 2

print(imc(352.5, 1.65))


## 64 Ejemplo de funciones simples con averiguar si es triángulo o no

print("\n\nEjercicio 64\n")
def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True ##si no se cumple ninguna es un triángulo, por eso returna True

print(esUnTriangulo (a=1, b=1, c=1))
print(esUnTriangulo (1, 1, 3))


## 65 Otro Ejemplo de funiciones simples con triángulo y pitágoras

print("\n\nEjercicio 65\n")
# Funciones
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b
    
def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

## Código
a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")
if esUnTrianguloRectangulo (a, b, c):
    print("Es un triángulo rectángulo")
else:
    print("No es un triángulo rectágulo.")


## 66 Otro ejemplo con funciones y Herón

print("\n\nEjercicio 66\n")

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b
    
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
    print("El campo del Triángulo corresponde a:", campoTriangulo(a, b, c))
else:
    print("Lo siento, no puede ser un triángulo.")


## 67 Ejemplo con función factorial

print("\n\nEjercicio 67\n")

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 6): # probando
    print(n, factorialFun(n))


## 68 Ejemplo con Fibonacci

print("\n\nEjercicio 68\n")

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # probando
    print(n, "->", fib(n))


## 69 Los anteriores; fibonacci y factorial pero recursivos

print("\n\nEjercicio 69\n")

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)
    
print("Factorial:", factorialFun(5))
print("Fionacci:", fib(5))


##  70   Tipos de secuencias y mutabilidad
#Antes de comenzar a hablar acerca de tuplas y diccionarios, se deben introducir dos conceptos importantes: tipos de secuencia
#y mutabilidad.

#Un tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar mas de un valor (o ninguno si la
#secuencia esta vacía), los cuales pueden ser secuencialmente (de ahí el nombre) examinados, elemento por elemento.

#Debido a que el bucle for es una herramienta especialmente diseñada para iterar a través de las secuencias, podemos
#definirlas de la siguiente manera: una secuencia es un tipo de dato que puede ser escaneado por el bucle for.

#Hasta ahora, has trabajado con una secuencia en Python, la lista. La lista es un clásico ejemplo de una secuencia de
#Python.
#Aunque existen otras secuencias dignas de mencionar, las cuales se presentaran a continuación.


#La segunda noción - la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su
#disponibilidad para poder cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos en Python: mutables e inmutables.

#Los datos mutables pueden ser actualizados libremente en cualquier momento, a esta operación se le denomina "in situ".

#Los datos inmutables no pueden ser modificados de esta manera.

#Imagina que una lista solo puede ser asignada y leída. No podrías adjuntar ni remover un elemento de la lista.
#Si se agrega un elemento al final de la lista provocaría que la lista se cree desde cero.

#Se tendría que crear una lista completamente nueva, la cual contenga los elementos ya existentes mas el nuevo
#elemento.

#El tipo de datos que se desea tratar ahora se llama tupla. Una tupla es una secuencia inmutable. Se puede
#comportar como una lista pero no puede ser modificada en el momento.

#¿Qué es una tupla?
#Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas. Las tuplas utilizan
#paréntesis, mientras que las listas usan corchetes, aunque también es posible crear una tupla tan solo separando
#los valores por comas.

#Observa el ejemplo:

#tupla1 = (1, 2, 4, 8)
#tupla2 = 1., .5, .25, .125

#Nota: cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, etc.).

## ¿Cómo crear una tupla?
#¿Es posible crear una tupla vacía? Si, solo se necesitan unos paréntesis:

#tuplaVacia = ()

#Si se desea crear una tupla de un solo elemento, se debe de considerar el hecho de que, debido a la sintaxis
#(una tupla debe de poder distinguirse de un valor entero ordinario), se debe de colocar una coma al final:

#tuplaUnElemento1 = (1, )
#tuplaUnElemento2 = 1., 

#El quitar las comas no arruinará el programa en el sentido sintáctico, pero serán variables no tuplas.


## 71 Escribir Tupla o elementos

print("\n\nEjercicio 71\n")

miTupla = (1, 10, 100, 1000)

print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)

###***Nota: Las similitudes pueden ser engañosas - no intentes modificar en contenido de la tupla ¡No es una lista!


## 72 ¿Qué más pueden hacer las tuplas?

# La función len() acepta tuplas, y regresa el numero de elementos contenidos dentro.
# El operador + puede unir tuplas (ya se ha mostrado esto antes).
# El operador * puede multiplicar las tuplas, así como las listas.
# Los operadores in y not in funcionan de la misma manera que en las listas.

print("\n\nEjercicio 72\n")

miTupla = (1, 10, 100)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3

print(len(t2))
print(t1)
print(t2)
print(10 in miTupla)
print(-10 not in miTupla)

#### adenda de TUPLAS

#También se puede crear una tupla utilizando la función integrada de Python tuple().
#Esto es particularmente útil cuando se desea convertir un iterable (por ejemplo, una lista,
#rango, cadena, etcétera) en una tupla:

print("Adenda de Tuplas leer el código")
miTup = tuple((1, 2, "cadena"))
print(miTup)

lst = [2, 4, 6]
print(lst)    # salida: [2, 4, 6]
print(type(lst))    # salida: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>

#De la misma manera, cuando se desea convertir un iterable en una liste, se puede emplear la función
#integrada de Python denominada list():

tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    # outputs: <class 'list'>

## 73 DICCIONARIOS

#En el mundo de Python, la palabra que se esta buscando se denomina clave(key). La palabra que se obtiene del
#diccionario es denominada valor.

#Esto significa que un diccionario es un conjunto de pares de claves y valores. Nota:

#Cada clave debe de ser única. No es posible tener una clave duplicada.
#Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número (entero o flotante), o incluso una cadena.
#Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario
#almacena pares de valores.
#La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.
#Un diccionario es una herramienta de un solo sentido. Si fuese un diccionario español-francés, podríamos buscar en
#español para encontrar su contraparte en francés mas no viceversa.

## Ejemplo

print("\n\nEjercicio 73\n")

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)  # Imprime el diccionario entero
print(numerosTelefono)
print(diccionarioVacio)

print(dict["gato"]) ## imprime el valor deseado
print("Suzy:",numerosTelefono['Suzy'])

## Otro Ejemplo con FOR

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")

## 74 Uso de KEYS en Diccionario para tener todas las claves con un FOR

print("\n\nEjercicio 74\n")

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys(): ##Se utiliza el Keys para obtener las claves
    print(key, "->", dict[key])      

## Para que sea ordenada con SORTED()
print("*" * 20)    
for key in sorted(dict.keys()):
    print(key, "->", dict[key])


## 75 Uso de ITEMS en DICCIONARIOS

#Otra manera de hacerlo es utilizar el método items(). Este método regresa
#una lista de tuplas (este es el primer ejemplo en el que las tuplas son
#mas que un ejemplo de si mismas) donde cada tupla es un par de cada clave con su valor.

print("\n\nEjercicio 75\n")

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dict.items():
    print(spanish, "->", french)


## 76 Uso de VALUES() con DICCIONARIO

print("\n\nEjercicio 76\n")

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dict.values():
    print(french)


## 77 Modificar una clave con un nuevo valor.

print("\n\nEjercicio 77\n")

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("Dic. Original:",dict)
dict['gato'] = 'minou'
print(dict)


## 78 Agregar elementos nuevos al DICCIONARIO (solo si el elemento no existe previamente)

print("\n\nEjercicio 78\n")

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)

## También se puede con UPDATE()
print("\n Usando UPDATE()\n")
dict.update({"pato" : "canard"})
print(dict)


## 79 Eliminando Claves con DEL

print("\n\nEjercicio 79\n")

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dict['perro']
print(dict)

dict.popitem() ## Elimina el último elemento de lista.
print(dict)    # outputs: {'gato' : 'chat', 'perro' : 'chien'}


## 80 Ejercicio de Tuplas y Diccionarios

print("\n\nEjercicio 80\n")
grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)

#Línea 1: crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave,
#mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor
#de un diccionario, esto no es un problema).
#Línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado).
#Línea 4: se lee el nombre del alumno.
#Línea 5-6: si el nombre es exit, nos salimos del bucle.
#Línea 8: se pide la calificación del alumno (un valor entero en el rango del 1-10).
#Línea 10-11: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con
#la nueva calificación (observa el operador +=).
#Línea 12-13: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva,
#su valor es una tupla de un solo elemento la cual contiene la calificación ingresada.
#Línea 15: se itera a través de los nombres ordenados de los estudiantes.
#Línea 16-17: inicializa los datos necesarios para calcular el promedio (sumador y contador).
#Línea 18-20: Se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma
#junto con el contador.
#Línea 21: se calcula e imprime el promedio del alumno junto con su nombre.


## Adenda de DICCIONARIOS

print("Adenda de DICCIONARIOS, leer código")

##1. Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas. (*En Python 3.6x los diccionarios
##están ordenados de manera predeterminada.

##Cada diccionario es un par de clave : valor. Se puede crear empleado la siguiente sintaxis:
#print("\nAdenda 1\n")
#miDictionario = {
 #   clave1 : valor1,
 #   clave2 : valor2,
 #   clave3 : valor3,
 #   }

##2. Si se desea acceder a un elemento del diccionario, se puede hacer haciendo referencia a su clave colocándola
##dentro de corchetes (ejemplo 1) o utilizando el método get() (ejemplo 2):

#print("\nAdenda 2\n")

#polEspDict = {
 #   "kwiat" : "flor",
 #   "woda"  : "agua",
 #   "gleba" : "tierra"
 #   }

#elemento1 = polEspDict["gleba"]    # ejemplo 1
#print(elmento1)    # salida: tierra

#elemento2 = polEspDict.get("woda")
#print(elemento2)    # salida: agua

##3. Si se desea cambiar el valor asociado a una clave especifica, se puede hacer haciendo referencia a la clave
##del elemento, a continuación se muestra un ejemplo:
#print("\nAdenda 3\n")

#polEspDict = {
 #   "zamek" : "castillo",
 #   "woda"  : "agua",
 #   "gleba" : "tierra"
 #   }

#polEspDict["zamek"] = "cerradura"
#item = polEspDict["zamek"]    # salida: cerradura 

##4. Para agregar o eliminar una clave (junto con su valor asociado), emplea la siguiente sintaxis:
#print("\nAdenda 4\n")

#miDirectorioTelefonico = {}    # un diccionario vacio

#miDirectorioTelefonico ["Adan"] = 3456783958    # crear o añadir un par clave-valor
#print(miDirectorioTelefonico)    # salida: {'Adan': 3456783958}

#del miDirectorioTelefonico ["Adan"]
#print(miDirectorioTelefonico)    # salida: {}

##Además, se puede insertar un elemento a un diccionario utilizando el método update(), y eliminar el ultimo elemento
##con el método popitem(), por ejemplo:

#polEspDict = {"kwiat" : "flor"}

#polEspDict = update("gleba" , "tierra")
#print(polEspDict)    # salida: {'kwiat' : 'flor', 'gleba' : 'tierra'}

#polEspDict.popitem()
#print(polEspDict)    # outputs: {'kwiat' : 'flor'}

##5. Se puede emplear el bucle for para iterar a través del diccionario, por ejemplo:
#print("\nAdenda 5\n")

#polEspDict = {
 #   "zamek" : "castillo",
 #   "woda"  : "agua",
 #   "gleba" : "tierra"
 #   }

#for item in polEspDict:
 #   print(item)    # salida: zamek
                   #          woda
                   #          gleba

##6. Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items() por ejemplo:
#print("\nAdenda 6\n")

#polEspDict = {
 #   "zamek" : "castillo",
 #   "woda"  : "agua",
 #   "gleba" : "tierra"
 #   }

#for clave, valor in polEspDict.items():
 #   print("Pol/Esp ->", clave, ":", valor)

##7. Para comprobar si una clave existe en un diccionario, se puede emplear la palabra reservada in:
#print("\nAdenda 7\n")

#polEspDict = {
 #   "zamek" : "castillo",
 #   "woda"  : "agua",
 #   "gleba" : "tierra"
 #   }

#if "zamek" in polEspDict:
 #   print("SI")
#else:
 #   print("NO")

##8. Se puede emplear la palabra reservada del para eliminar un elemento, o un diccionario entero. Para eliminar todos los elementos de un diccionario se debe emplear el método clear():
#print("\nAdenda 8\n")

#polEspDict = {
 #   "zamek" : "castillo",
 #   "woda"  : "agua",
 #   "gleba" : "tierra"
 #   }

#print(len(polEspDict))    # salida: 3
#del polEspDict["zamek"]    # elimina un elemento
#print(len(polEspDict))    # salida: 2

#polEspDict.clear()   # elimina todos los elementos
#print(len(polEspDict))    # salida: 0

#del polEspDict    # elimina el diccionario

##9. Para copiar un diccionario, emplea el método copy():
#print("\nAdenda 9\n")

#polEspDict = {
 #   "zamek" : "castillo",
 #   "woda"  : "agua",
 #   "gleba" : "tierra"
 #   }

#copyDict = polEspDict.copy()

## Otros ejercicio
print("\nOtros Ejercicios\n")
## Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
print("\nOtro Ejercicio 1\n")

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for elemento in (d1, d2):
    d3.update(elemento)

print(d3)

## Escribe un programa que convierta la lista l en una tupla.
print("\nOtro Ejercicio 2\n")

l = ["carro", "Ford", "flor", "Tulipán"]

t = tuple(l)
print(t)

## Escribe un programa que convierta la tupla colores en un diccionario.
#print("\nOtro Ejercicio 3\n")

#colores = (("verde", "#008000"), ("azul", "#0000FF"))

#colDict = dict(colores)
#print(colDict)

## Cuál es la salida del siguiente programa?
print("\nOtro Ejercicio 4\n")

colores = {
    "blanco" : (255, 255, 255),
    "gris"   : (128, 128, 128),
    "rojo"   : (255, 0, 0),
    "verde"  : (0, 128, 0)
    }

for col, rgb in colores.items():
    print(col, ":", rgb)


### Ejercicio 81
### Práctica larga de TIC TAC TOE

print("\n\nEjercicio 81\n")


def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

def player_input():
    player1 = input("Please pick a marker 'X' or 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("You've choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Please pick a marker 'X' or 'O' ")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def player_choice(board):
    choice = input("Please select an empty space between 1 and 9 : ")
    while not space_check(board, int(choice)):
        choice = input("This space isn't free. Please choose between 1 and 9 : ")
    return choice

def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    i = 1
    # Choose your side
    players=player_input()
    # Empty board init
    board = ['#'] * 10
    while True:
        # Set the game up here
        game_on=full_board_check(board)
        while not game_on:
            # Player to choose where to put the mark
            position = player_choice(board)
            # Who's playin ?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play !
            place_marker(board, marker, int(position))
            # Check the board
            display_board(board)
            i += 1
            if win_check(board, marker):
                print("You won !")
                break
            game_on=full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # Choose your side
            players=player_input()
            # Empty board init
            board = ['#'] * 10

 """#COMENTARIO MASIVO
