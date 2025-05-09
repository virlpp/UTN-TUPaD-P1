#-----------------------------------------------------------------------------------------------------------------------------


#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

numeros = list(range(4, 101, 4))   

print(numeros) #Para verificar que la lista se creó correctamente.
# 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100



#-----------------------------------------------------------------------------------------------------------------------------


#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten)
#  y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar 
# cómo funciona el indexing con números negativos!

instrumentos = ["chelo", "violín", "batería", "piano", "saxofón"]

print(instrumentos[-2]) #Para verificar que el penúltimo elemento se muestra correctamente.
# piano



#-----------------------------------------------------------------------------------------------------------------------------


#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista 
# resultante por pantalla. Pista: para crear una lista vacía debes colocar los 
# corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

lista_vacia = []

lista_vacia.append("azul")
lista_vacia.append("violeta")
lista_vacia.append("verde")

print(lista_vacia) #Para verificar que la lista se creó correctamente.
# ['azul', 'violeta', 'verde']


#-----------------------------------------------------------------------------------------------------------------------------


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#  respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se
#  muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
#  animales = ["perro", "gato", "conejo", "pez"]


animales = ["perro", "gato", "conejo", "pez"]

animales[1]= "loro" #Reemplaza el segundo elemento de la lista por "loro"
animales[-1]= "oso" #Reemplaza el último elemento de la lista por "oso"

print(animales) #Para verificar que la lista se creó correctamente.
# # ['perro', 'loro', 'conejo', 'oso']



#-----------------------------------------------------------------------------------------------------------------------------


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#  
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) #Elimina el número mayor de la lista

print(numeros) #Para verificar que el número mayor se eliminó correctamente.
#Imprime 8, 15, 3, 7.

#El programa crea una lista de números sde forma desordena, en la lúnea 7 con la función ´remove()´ podemos saber que se va a 
#eliminar uno de sus elementos, y on la función max() se encaerga de obtener el número mayor de la lista, se encuentre en la
#posición que se encuentre.

# Finalmente, imprime la lista actualizada sin el número mayor.


#-----------------------------------------------------------------------------------------------------------------------------


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

nums = list(range(10, 31, 5)) #Crea una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5.

print(nums[:2]) #Muestra por pantalla los dos primeros números de la lista.
# # [10, 15]



#-----------------------------------------------------------------------------------------------------------------------------


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos
#  valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "palio" #Reemplaza el segundo elemento de la lista por "palio"
autos[2] = "chevette" #Reemplaza el tercer elemento de la lista por "chevette"

print(autos) #Para verificar que la lista se modificó correctamente.



#-----------------------------------------------------------------------------------------------------------------------------


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
#  Imprimir la lista resultante por pantalla.

dobles = []

dobles.append(5*2) #Agrega el doble de 5 a la lista
dobles.append(10*2) #Agrega el doble de 10 a la lista
dobles.append(15*2) #Agrega el doble de 15 a la lista   

print(dobles) #Para verificar que la lista se creó correctamente.
# # [10, 20, 30]


#-----------------------------------------------------------------------------------------------------------------------------


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo") #Agrega "jugo" a la lista del tercer cliente usando append.

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines" #Reemplaza "fideos" por "tallarines" en la lista del segundo cliente.

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan") #Elimina "pan" de la lista del primer cliente.

# d) Imprimir la lista resultante por pantalla
print(compras) #Imprime la lista resultante por pantalla.


#-----------------------------------------------------------------------------------------------------------------------------


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False] #Crea una lista anidada con los elementos especificados.

print(lista_anidada) #Imprime la lista resultante por pantalla.
