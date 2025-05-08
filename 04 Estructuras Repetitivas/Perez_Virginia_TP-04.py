#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Defino un bucle for para repetir el código una cantidad finita de veces desde 1 hasta 100 (incluyendo ambos extremos).
for x in range (1, 101):
    print(x)   #Imprimo el número entero en la pantalla hasta llegar al 100.

#-----------------------------------------------------------------------------------------------------------------------------

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# Defino la variable num_ent para almacenar el número entero ingresado por el usuario.
num_ent = int(input("Ingrese un número entero: "))

# Inicializamos la variable num_dig a 0 para contar los dígitos.
num_dig = 0

num_ent = abs(num_ent) # Tomamos el valor absoluto del número ingresado para considerar los números negativos.
# Verificamos si el número es cero, en cuyo caso tiene un dígito.
if num_ent == 0:
    num_dig = 1 # Si el número es cero tendría un dígito.

# Si el número es diferente de cero, contamos los dígitos dividiendo el número entre 10.

while num_ent > 0: #Repite mientras el número sea mayor que 0.
     # Dividimos el número entre 10 para eliminar el último dígito.
    num_ent = num_ent // 10
    # Incrementamos el contador de dígitos.
    num_dig += 1

#Imprime la can tidad de dígitos.
print(f"El número tiene {num_dig} dígitos.")



#-----------------------------------------------------------------------------------------------------------------------------


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

#Defino la variable num_uno y num_dos para almacenar los números enteros ingresados por el usuario.
num_uno = int(input("Ingrese el primer número entero: ")) #Solicito el primer número entero al usuario.
num_dos = int(input("Ingrese un segundo número entero mayor al primero: ")) #Solicito el segundo número entero al usuario.

#Defino un bucle while para repetir el código una cantidad finita de veces desde 
# el primer número ingresado hasta el segundo número ingresado.

dif = num_dos - num_uno - 1 #Calculo la diferencia entre los dos números ingresados por el usuario.
cont = 0
suma = 0 #Inicializo la variable suma en 0 para almacenar la suma de los números enteros.
x = 0 #Inicializo la variable x en 0 para almacenar el número entero ingresado por el usuario.


while cont != dif: #Repite mientras el contador sea menor que la diferencia entre los dos números más uno.

    cont += 1 #Incremento el contador en 1.
    x = num_uno + cont
    suma = suma + x #Suma el primer número ingresado por el usuario más el contador.


#Imprime la suma de los números enteros entre los dos números ingresados por el usuario.
print(f"La suma de los números enteros entre {num_uno} y {num_dos} es: {suma}") 

#Utilizo el print de las variables que condicionan la candena para verificar que el código funciona correctamente.
# print(dif)
# print(cont)


#-----------------------------------------------------------------------------------------------------------------------------


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num_secuencua = 1 #Inicializo la variable num_secuencua en 1 para entrar al bucle while.
suma = 0 #Inicializo la variable suma en 0 para almacenar la suma de los números enteros.

while num_secuencua != 0: #Repite mientras el número ingresado por el usuario sea diferente de 0.

    num_secuencua = int(input("Ingrese un número entero (0 para salir): ")) #Solicito al usuario que ingrese un número entero.
    suma = suma + num_secuencua #Suma el número ingresado por el usuario a la variable suma.

    # print(f"La suma acumulada es: {suma}") #Imprime la suma acumulada de los números enteros ingresados por el usuario.
    # Este print se encuentra dentro del bucle while, por lo que se ejecuta cada vez que el usuario ingresa un número entero
    # y se utiliza para verificación.   

print(f"La suma acumulada es: {suma}") #Imprime la suma acumulada de los números enteros ingresados por el usuario.



#-----------------------------------------------------------------------------------------------------------------------------


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random #Importo la librería random para generar un número aleatorio.

 #El número aleatorio se almacena en la variable num_aleatorio.
num_aleatorio = random.randint(0, 9) #Genera un número aleatorio entre 0 y 9.
intentos = 0 #Inicializo la variable intentos en 0 para contar los intentos del usuario.
num_usuario = 0 #Inicializo la variable num_usuario en 0 para entrar al bucle while.

while num_usuario != num_aleatorio: #Repite mientras el número ingresado por el usuario sea diferente al número aleatorio.
    num_usuario = int(input("Adivina un número entre 0 y 9: ")) #Solicita alusuario que ingrese un número entre 0 y 9.
    intentos += 1 #Incrementa el contador de intentos en 1.

print(f"Intento número: {intentos}") #Imprime el número de intentos realizados por el usuario.



#-----------------------------------------------------------------------------------------------------------------------------


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for x in range(100, -1, -2): #Defino un bucle for para repetir el código una cantidad finita de veces desde 100 hasta 0 (incluyendo ambos extremos).
    print(x) #Imprimo el número entero en la pantalla hasta llegar al 0.


#-----------------------------------------------------------------------------------------------------------------------------


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


#Defino la variable num_ent_usuario para almacenar el número entero ingresado por el usuario.

num_ent_usuario = int(input("Ingrese un número entero: ")) #Solicito al usuario que ingrese un número entero.
num_ent_usuario = abs(num_ent_usuario) #Convierte el número ingresado por el usuario a su valor absoluto.

#Defino la variable suma para almacenar la suma de los números enteros.
suma = 0 #Inicializo la variable suma en 0 para almacenar la suma de los números enteros.
cont = 0 #Inicializo la variable cont en 0 para almacenar el número entero ingresado por el usuario.

while cont != num_ent_usuario: #Repite mientras el contador sea diferente al número ingresado por el usuario.
    cont += 1 #Incremento el contador en 1.
    suma = suma + cont #Suma el primer número ingresado por el usuario más el contador.

#Imprime la suma de los números enteros entre 0 y el número ingresado por el usuario.
print(f"La suma de los números enteros entre 0 y {num_ent_usuario} es: {suma}") 


#-----------------------------------------------------------------------------------------------------------------------------


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador = 0 #Inicializo la variable contador en 0 para contar los números ingresados por el usuario.
contador_pares = 0 #Inicializo la variable contador_pares en 0 para contar los números pares ingresados por el usuario.
contador_impares = 0 #Inicializo la variable contador_impares en 0 para contar los números impares ingresados por el usuario.
contador_negativos = 0 #Inicializo la variable contador_negativos en 0 para contar los números negativos ingresados por el usuario.
contador_positivos = 0 #Inicializo la variable contador_positivos en 0 para contar los números positivos ingresados por el usuario. 

while contador != 10: #Repite mientras el contador sea menor que 100.
    
        num = int(input("Ingrese un número entero: ")) #Solicito al usuario que ingrese un número entero.
        contador += 1 #Incremento el contador en 1.

        if num % 2 == 0: #Si el número ingresado por el usuario es par.
            contador_pares += 1 #Incremento el contador de números pares en 1.
        else: #Si el número ingresado por el usuario es impar. 
            contador_impares += 1
        if num < 0: #Si el número ingresado por el usuario es negativo.
            contador_negativos += 1
        else: #Si el número ingresado por el usuario es positivo.   
            contador_positivos += 1 

print(f"Cantidad de números ingresados: {contador}") #Imprime la cantidad de números ingresados por el usuario.
print(f"Cantidad de números pares: {contador_pares}") #Imprime la cantidad de números pares ingresados por el usuario.
print(f"Cantidad de números impares: {contador_impares}") #Imprime la cantidad de números impares ingresados por el usuario.   
print(f"Cantidad de números negativos: {contador_negativos}") #Imprime la cantidad de números negativos ingresados por el usuario.
print(f"Cantidad de números positivos: {contador_positivos}") #Imprime la cantidad de números positivos ingresados por el usuario.  


#-----------------------------------------------------------------------------------------------------------------------------


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

contador = 0 #Inicializo la variable contador en 0 para contar los números ingresados por el usuario.
suma = 0 #Inicializo la variable suma en 0 para almacenar la suma de los números enteros ingresados por el usuario.

while contador != 100: #Una vez que se ingresen los 100 números contador llegará a 100 y finalizará el ciclo.
    
        num = int(input("Ingrese un número entero: ")) #Solicito al usuario que ingrese un número entero.
        contador += 1 #Incremento el contador en 1.
        suma += num #Suma el número ingresado por el usuario a la variable suma.
        

print(f"La media de los números ingresados es: {suma/contador}") #Imprime la media de los números ingresados por el usuario.


#-----------------------------------------------------------------------------------------------------------------------------


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_ingresado = int(input("Ingrese un número entero: ")) #El valor ingresado por el usuario se almacena en la variable num_ingresado.
num_absoluto = abs(num_ingresado)  # Tomamos el valor absoluto para trabajar sólo con los dígitos.
num_invertido = 0 # Inicializamos la variable num_invertido en 0 para almacenar el número invertido.

while num_absoluto > 0: #El bucle while se ejecuta mientras el número absoluto sea mayor que 0.

    # El operador módulo devuelve el residuo de la división entre el número absoluto y 10, que es el último dígito.
    digito = num_absoluto % 10  # Obtiene el último dígito a través del operador módulo.

    num_invertido = num_invertido * 10 + digito  # Va construyendo el número invertido multiplicando por 10 y sumando el último dígito.

    num_absoluto //= 10  # Elimina el último dígito del número original

# Si el número original era negativo, mantenemos el signo
if num_ingresado < 0:
    num_invertido *= -1

print("Número invertido:", num_invertido) # Imprime el número invertido.
