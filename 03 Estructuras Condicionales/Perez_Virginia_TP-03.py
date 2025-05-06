#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#  deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_minima = 18
edad_ingresada = int(input("Ingrese su edad: "))

if edad_minima <= edad_ingresada:
    if edad_ingresada == 0:
        print("No puede ingresar cero.")
    else:
        print("Es mayor de edad.")
    
else:
    if edad_ingresada == 0:
        print("No puede ingresar cero.")
    else:
        print("Es menor de edad.")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
#  deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota_ingresada = int(input("Ingrese su nota: "))

if nota_ingresada >= 6 and nota_ingresada <= 10:
    print("Aprobado")

elif nota_ingresada < 6 and nota_ingresada >= 0:
    print("Desaprobado")
    
else:
    print("Nota no válida")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par,
#  imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario,
#  imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#  operador de módulo (%) en Python para evaluar si un número es par o impar.

num_ing = int(input("Ingrese un número entero par: ")) 
num_par = num_ing % 2 

if num_par == 0 and num_ing != 0:
    # Si el número es par y no es cero
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")
    


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#  siguientes categorías pertenece:
#  ● Niño/a: menor de 12 años.
#  ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#  ● Adulto/a joven: mayor o igual que 18 años
#  y menor que 30 años.
#  ● Adulto/a: mayor o igual que 30 años.


edad_rango = int(input("Ingrese su edad: "))

if edad_rango < 12 and edad_rango >= 0:
    # Se agrega la condición edad_rango >= 0 para evitar errores si el usuario ingresa un número negativo
    print("Niño/a") 

elif 12 <= edad_rango < 18:
    print("Adolescente")

elif 18 <= edad_rango < 30:
    print("Adulto/a joven")

elif edad_rango >= 30:
    print("Adulto/a")

else:
    print("Edad no válida. Por favor, ingrese un número positivo.")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#  (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada,
#  imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene 
# un iterable tal como una lista o un string.

contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")  
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media
#  y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random   

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]


print("Lista de números aleatorios:", numeros_aleatorios)
print(f"La media es ", mean(numeros_aleatorios),".")
print(f"La mediana es ", median(numeros_aleatorios),".")
print(f"La moda es ", mode(numeros_aleatorios),".")
print("El sesgo es: ", end="")

if mean (numeros_aleatorios) > median (numeros_aleatorios) and median (numeros_aleatorios) > mode (numeros_aleatorios):
    print("Sesgo positivo o a la derecha.")
elif mean (numeros_aleatorios) < median (numeros_aleatorios) and median (numeros_aleatorios) < mode (numeros_aleatorios):
    print("Sesgo negativo o a la izquierda.")
elif mean (numeros_aleatorios) == median (numeros_aleatorios) and median (numeros_aleatorios) == mode (numeros_aleatorios):
    print("Sin sesgo.")
else:
    print("No se puede determinar el sesgo.")


#7) Escribir un programa que solicite una frase o palabra al usuario.
#  Si el string ingresado termina con vocal, añadir un signo de exclamación
#  al final e imprimir el string resultante por pantalla; en caso contrario,
#  dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase_palabra = input("Ingrese una frase o palabra: ")  

if frase_palabra[-1].lower() in "aeiou":
    print(frase_palabra, "!")
else:
    print(frase_palabra)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada 
# por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#  lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
op = int(input("Ingrese 1 para imprimir su nombre en mayúsculas, 2 para imprimir su nombre en minúsculas o 3 si quiere la primer letra en mayúscula: "))

if op == 1:
    print(nombre.upper())   
elif op == 2:
    print(nombre.lower())
elif op == 3:
    print(nombre.title())


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud 
# en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3 and magnitud_terremoto >= 0:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")  
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)") 
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Error: La magnitud del terremoto no es válida.")



#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
# qué mes del año es y qué día es. El programa deberá utilizar esa información para
#  imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# El programa debe funcionar para ambos hemisferios y para todos los meses del año.

hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = input("¿Qué mes del año es? (1-12): ").strip()
dia = int(input("¿Qué día es? (1-31): ").strip())
estacion = ""

# Verificamos si el hemisferio es norte o sur

if hemisferio == "S":

    if (mes == "12" and dia >= 21 and dia <= 31) or (mes == "1" and dia >= 1 and dia <=31) or (mes == "2" and dia >= 1 and dia <=28) or (mes == "3" and dia < 20)  and dia >= 1:
        estacion = "Verano"
    elif (mes == "3" and dia >= 20 and dia <= 31) or (mes == "4" and dia >= 1 and dia <=30) or (mes == "5" and dia >= 1 and dia <=31) or (mes == "6" and dia < 21) and dia >= 1 :
        estacion = "Otoño"
    elif (mes == "6" and dia >= 21 and dia <= 30) or (mes == "7" and dia >= 1 and dia <=31) or (mes == "8" and dia >= 1 and dia <=31) or (mes == "9" and dia < 22) and dia >= 1:
        estacion = "Invierno"
    elif (mes == "9" and dia >= 22 and dia <= 30) or (mes == "10" and dia >= 1 and dia <=31) or (mes == "11" and dia >= 1 and dia <=30) or (mes == "12" and dia < 21) and dia >= 1:
        estacion = "Primavera"

    if (estacion == "Invierno" or estacion == "Verano" or estacion == "Otoño" or estacion == "Primavera"):
        print(f"Te encontrás en {estacion}.")

    else:
        print("Fecha no válida")


elif hemisferio == "N":

    if (mes == "6" and dia >= 21 and dia <= 30) or (mes == "7" and dia >= 1 and dia <=31) or (mes == "8" and dia >= 1 and dia <=31) or (mes == "9" and dia < 22) and dia >= 1:
        estacion = "Verano"
    elif (mes == "9" and dia >= 22 and dia <=30 ) or (mes == "10" and dia >= 1 and dia <=31) or (mes == "11" and dia >= 1 and dia <=30) or (mes == "12" and dia < 21) and dia >= 1:
        estacion = "Otoño"
    elif (mes == "12" and dia >= 21 and dia <= 31) or (mes == "1" and dia >= 1 and dia <=31) or (mes == "2" and dia >= 1 and dia <=28) or (mes == "3" and dia < 20) and dia >= 1:
        estacion = "Invierno"
    elif (mes == "3" and dia >= 20 and dia <= 31) or (mes == "4" and dia >= 1 and dia <=30) or (mes == "5" and dia >= 1 and dia <=31) or (mes == "6" and dia < 21) and dia >= 1:
        estacion = "Primavera"

    if estacion == "Invierno" or estacion == "Verano" or estacion == "Otoño" or estacion == "Primavera": 
        print(f"Te encontrás en {estacion}.")

    else:
        print("Fecha no válida")

else:
    print ("Hemisferio no válido")
