#1)Función recursiva que calcula el factorial de un número


def factorial(n):
    while n < 0:
        print("Ingrese un número positivo.")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
   
#Programa principal
n = int(input("Introduzca un número positivo para calcular su factorial: "))
resultado = factorial(n)
#Imprimir resultado de cada número entreo desde 0 hasta n
for i in range(n + 1):
    print(f"El factorial de {i} es: {factorial(i)}")


#2) Función recursiva para calcular el valor de la serie de Fibonacci.

def fibonacci(n):
    if n < 0:
        print("Ingrese un número positivo.")
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Programa principal
n = int(input("Introduzca un número positivo para calcular el valor de la serie de Fibonacci: "))

while n < 0:
    print("Ingrese un número positivo.")
    n = int(input("Introduzca un número positivo para calcular el valor de la serie de Fibonacci: "))
# Imprimir resultado de cada número entre 0 hasta n
for i in range(n + 1):
    print(f"El valor de la serie de Fibonacci en la posición {i} es: {fibonacci(i)}")


#3) Función recursiva para calcular la potencia de un número  base elevado a un exponente.

def potencia(base, exponente):
  
    if exponente == 1:
        return base
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    elif exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
# Programa principal

base = int(input("Introduzca la base: "))
exponente = int(input("Introduzca el exponente: "))

print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")


#4) Función recursiva que reciba un numero entero positivo y devuelva su representación en binario com cadena de texto.
def decimal_a_binario(n):
    while n < 0:
        n = int(input("Ingrese por favor un número positivo."))    
    # Caso base
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
# Programa principal
n = int(input("Introduzca un número entero positivo para convertirlo a binario: ")) 

print(f"La representación en binario de {n} es: {decimal_a_binario(n)}")

5) Implemento de una función recursiva es_palindromo(palabra) que recibe una cadena de texto
 sin espacions ni tildes y devuelve True si es un palíndromo (se lee igual de izquierda a
 derecha que de derecha a izquierda) o False en caso contrario.

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 caracteres, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Verificar si el primer y último carácter son iguales
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva eliminando el primer y último carácter
    return es_palindromo(palabra[1:-1])

# Programa principal
palabra = input("Ingrese una palabra o frase sin espacios ni tildes: ").replace(" ", "").lower()
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}") #Verificación.


#6) Función recursiva llamada suma_digitos(n) que recibe un número entero positivo y 
# devuelve la suma de sus dígitos.

def suma_digitos(n):

    #Validación para asegurarse de que n es un número entero positivo.
    while n < 0:
        n = int(input("Ingrese por favor un número positivo."))

    # Caso base: si n es 0, la suma de sus dígitos es 0
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
# Programa principal
n = int(input("Introduzca un número entero positivo para calcular la suma de sus dígitos: "))   
print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")



#7) Función recursiva llamada contar_bloques que reciba el número de bloques en el nivel más bajo 
# y devuelva el número total de bloques que necesita para hacer la pirámide.

def contar_bloques(n):
    # Validación para asegurarse de que n es un número entero positivo.
    while n < 0:
        n = int(input("Ingrese por favor un número positivo."))

    # Caso base: si n es 0, no hay bloques
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)  # Suma el número de bloques del nivel actual con los bloques de los niveles inferiores
    
# Programa principal
n = int(input("Introduzca el número de bloques en el nivel más bajo de la pirámide: ")) 
print(f"El número total de bloques necesarios para hacer la pirámide es: {contar_bloques(n)}")



#8) Función recursiva llamada contar_digito(numero, digito) que recibe un número
#  entero positivo y un dígito (0-9) y devuelve la cantidad de veces que aparece
#  el dígito en el número.
def contar_digito(numero, digito):
    # Validación para asegurarse de que numero es un número entero positivo.
    while numero < 0:
        numero = int(input("Ingrese por favor un número positivo."))
    
    # Caso base: si el número es 0, no hay dígitos
    if numero == 0:
        return 0 if digito == 0 else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    
# Programa principal
numero = int(input("Introduzca un número entero positivo: "))
digito = int(input("Introduzca un dígito (0-9) para contar cuántas veces aparece en el número: "))
while digito < 0 or digito > 9:
    digito = int(input("Ingrese un dígito válido (0-9): "))

print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")
