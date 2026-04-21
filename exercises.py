"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""







# def check_is_balanced(text):
#     text = text.lower().replace(" ","")
#     count_J = 0
#     count_R = 0
#     for letter in text:
#         if(letter == "j"):
#             count_J+=1
#         elif(letter == "r"):
#             count_R+=1
#     return count_J == count_R

        
# text = input("Escribe un texto y determinare el balance de poder entre Reed y Jonny: \n")

# is_balance = check_is_balanced(text)

# print(is_balance)

"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

# def count_eggs_trex(list):
#     count_par=0
#     for num in list:
#         if num % 2 == 0:
#             count_par+=num
#     return count_par    

# list = [1,2,2,2,3,4,5,6,5,5,5,7,8]

# print(count_eggs_trex(list))

"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
# list = [4,6,5,2]
# goal = 8


# def find_first_sum(list,goal):
#     for index,num in enumerate(list):
#        for index_2,num_2 in enumerate(list):
#            if index == index_2 : continue
#            sum = num + num_2
#            if sum == goal: return (index,index_2)
#     return "None"

# print(find_first_sum(list, goal))  # [2, 3]


"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

# list_a = [4, 4, 4]
# list_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

# list_a = [4,3,3]
# list_b= [2,2,5]

# list_a = [4, 4, 4]
# list_b = [2, 8, 2]

list_a = [2, 4, 2]
list_b = [3, 3, 4]


def battle_royale(list_a,list_b):
    for index,num in enumerate(list_a):
        if index < ((len(list_a))-1):
            
            print(len(list_a))
            rest_battle = list_a[index] - list_b[index]
            if(rest_battle):
                list_a[index+1] += rest_battle
            else:
                rest_battle = -(rest_battle)
                list_b[index+1] += rest_battle
        else:
            rest_battle =  list_a[index] - list_b[index]
            if rest_battle >0: 
                return ("A"+str(rest_battle))
            elif rest_battle <0:
                rest_battle = -(rest_battle)
                return ("B"+str(rest_battle))
            else:
                return "X"
print(battle_royale(list_a,list_b))
