#Definición de función separador

def separador():
    print("_____________________________________________________________")


#1)
#Definición de funciones
def imprimir_hola_mundo():
    print("¡Hola, mundo!")  

#Programa principal
imprimir_hola_mundo() # Llamada a la función
# No es necesario imprimir el resultado de la función, ya que la función ya imprime el mensaje

separador()  

#2)
#Definición de funciones
def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}!")  

#Programa principal
nombre_usuario = input("Cuál es tu nombre? ")  # Solicita el nombre del usuario
saludar_usuario(nombre_usuario)  # Llamada a la función con el nombre del usuario

separador()  

#3)
#Definición de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuál es tu edad? ")
residencia = input("¿Dónde vives? ")

informacion_personal(nombre, apellido, edad, residencia)  # Llamada a la función con los datos del usuario

separador() 

#4)
#Definición de funciones
def calcular_area_circulo(radio):
     pi = 3.14159
     area = pi * (radio ** 2)
     return area  # Devuelve el área del círculo

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro  # Devuelve el perímetro del círculo

#Programa principal
radio = float(input("Introduzca el radio de un círculo: "))  # Solicita el radio del círculo

area = calcular_area_circulo(radio)  # Llama a la función para calcular el área
perimetro = calcular_perimetro_circulo(radio)  # Llama a la función para calcular el perímetro
print(f"El área del círculo es: {area} y el perímetro del círculo es: {perimetro}")  

separador()

#5)
#Definición de funciones
def segundos_a_horas(segundos):
    horas = segundos // 3600  # Calcula las horas
    return horas # Devuelve las horas

#Programa principal
segundos = int(input("Introduzca la cantidad de segundos: "))  # Solicita la cantidad de segundos
horas = segundos_a_horas(segundos)  # Llama a la función para convertir segundos a horas
if horas == 1:
    print(f"{segundos} segundos son {horas} hora.")  # Imprime el resultado de la conversión en singular
else:
    print(f"{segundos} segundos son {horas} horas.")  # Imprime el resultado de la conversión

separador()

#6)
#Definición de funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):  # Itera del 1 al 10
        resultado = numero * i  # Calcula el resultado de la multiplicación
        print(f"{numero} x {i} = {resultado}")  # Imprime el resultado de la multiplicación

#Programa principal
numero = int(input("Introduzca un número para ver su tabla de multiplicar: "))  # Solicita un número al usuario
tabla_multiplicar(numero)  # Llama a la función para mostrar la tabla de multiplicar del número ingresado

separador()

#7)
#Definición de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0: # b debe ser diferente de cero para evitar errores de división por cero
        division = a / b
    else:
        division = "Error: División por cero"
    
    return suma, resta, multiplicacion, division  # Devuelve una tupla con los resultados

#Programa principal
a = float(input("Ingrese el primer número: "))  # Solicita al usuario el primer número
b = float(input("Ingrese el segundo número: "))  # Solicita al usuario el segundo número
resultados = operaciones_basicas(a, b)  # Llama a la función con los números ingresados
print(f"Suma: {resultados[0]}")  # Imprime la suma
print(f"Resta: {resultados[1]}")  # Imprime la resta
print(f"Multiplicación: {resultados[2]}")  # Imprime la multiplicación
print(f"División: {resultados[3]}")  # Imprime la división o el mensaje de error si corresponde

separador()

#8)
#Definición de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)  # Calcula el IMC
    return imc  # Devuelve el IMC calculado

# Programa principal
peso = float(input("Introduzca su peso en Kg: "))  # Solicita el peso del usuario
altura = float(input("Introduzca su altura en metros: "))  # Solicita la altura del usuario
imc = calcular_imc(peso, altura)  # Llama a la función para calcular el IMC
print(f"Su IMC es: {imc:.2f}")  # Muestra el IMC calculado con dos decimales

separador()

#9)
#Definición de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 # Calculo de la temperatura en Fahrenheit
    return fahrenheit  # Devuelve la temperatura en Fahrenheit

# Programa principal
celsius = float(input("Introduzca la temperatura en grados Celsius: "))  # Solicita la temperatura en Celsius
fahrenheit = celsius_a_fahrenheit(celsius)  # Llama a la función para convertir Celsius a Fahrenheit
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")  # Muestra la temperatura en Fahrenheit

separador()

#10)
#Definición de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio  # Devuelve el promedio de los tres números

#Programa principal
numero1 = float(input("Ingrese el primer número: "))  # Solicita el primer número
numero2 = float(input("Ingrese el segundo número: "))  # Solicita el segundo número
numero3 = float(input("Ingrese el tercer número: "))  # Solicita el tercer número
promedio = calcular_promedio(numero1, numero2, numero3)  # Llama a la función para calcular el promedio
print(f"El promedio de los números {numero1}, {numero2} y {numero3} es: {promedio}")  # Imprime el resultado del promedio

separador()
