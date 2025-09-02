import random
import string
import time
import sys
import os

#profe intente hacer una pantalla por cada cosa y hasta cargando, nomas para probar un poco
#pero veo que todavia no puedo enlazar bien las cosas jejeje

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def cargar(texto):
    for i in range(0, 101, 10):
        sys.stdout.write(f"\r{texto} {i}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def variables():
    limpiar()
    cargar("Cargando")
    while True:
        resp_variable = input("Agrega un valor (puede ser numero o palabra): ")
        try:
            valor = int(resp_variable)
        except ValueError:
            try:
                valor = float(resp_variable)
            except ValueError:
                valor = resp_variable
        print(f"{valor} es de tipo {type(valor)}")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def aritmeticos():
    limpiar()
    cargar("Cargando")
    while True:
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        print(f"Suma: {a+b}")
        print(f"Resta: {a-b}")
        print(f"Multiplicacion: {a*b}")
        if b != 0:
            print(f"Division: {a/b}")
        else:
            print("No se puede dividir entre 0")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def logicos_condicionales():
    limpiar()
    cargar("Cargando")
    while True:
        edad = int(input("Ingresa tu edad: "))
        if edad >= 18 and edad < 60:
            print("Eres un adulto")
        elif edad >= 60:
            print("Eres un adulto mayor")
        else:
            print("Eres menor de edad")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def funciones_recursividad():
    limpiar()
    cargar("Cargando")
    while True:
        num = int(input("Ingresa un numero para calcular su factorial: "))
        print(f"El factorial de {num} es {factorial(num)}")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def loop_for():
    limpiar()
    cargar("Cargando")
    while True:
        n = int(input("¿Hasta que numero quieres contar? "))
        for i in range(1, n+1):
            print(i, end=" ")
        print()
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def loop_while():
    limpiar()
    cargar("Cargando")
    while True:
        n = int(input("Ingresa un numero para contar hacia atras: "))
        while n >= 0:
            print(n, end=" ")
            n -= 1
        print()
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def listas():
    limpiar()
    cargar("Cargando")
    while True:
        lista = []
        while True:
            val = input("Agrega un elemento a la lista (o escribe 'fin' para terminar): ")
            if val.lower() == "fin":
                break
            lista.append(val)
        print(f"Lista completa: {lista}")
        print(f"Primer elemento: {lista[0] if lista else 'N/A'}")
        print(f"Ultimo elemento: {lista[-1] if lista else 'N/A'}")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def promedio_lista():
    limpiar()
    cargar("Cargando")
    while True:
        nums = []
        while True:
            val = input("Ingresa un numero (o escribe 'fin' para calcular el promedio): ")
            if val.lower() == "fin":
                break
            try:
                nums.append(float(val))
            except:
                print("Dato invalido")
        if nums:
            print(f"El promedio es: {sum(nums)/len(nums)}")
        else:
            print("No ingresaste numeros")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def palindromo():
    limpiar()
    cargar("Cargando")
    while True:
        palabra = input("Ingresa una palabra: ").lower()
        if palabra == palabra[::-1]:
            print("Es un palindromo")
        else:
            print("No es un palindromo")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def contador_vocales():
    limpiar()
    cargar("Cargando")
    while True:
        texto = input("Ingresa una cadena: ").lower()
        contador = sum(1 for c in texto if c in "aeiou")
        print(f"Numero de vocales: {contador}")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def conversor_temperatura():
    limpiar()
    cargar("Cargando")
    while True:
        opcion = int(input("1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius\nElige: "))
        temp = float(input("Ingresa la temperatura: "))
        if opcion == 1:
            print(f"{temp}C = {(temp*9/5)+32}F")
        elif opcion == 2:
            print(f"{temp}F = {(temp-32)*5/9}C")
        else:
            print("Opcion no valida")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def adivina_numero():
    limpiar()
    cargar("Cargando")
    while True:
        secreto = random.randint(1, 100)
        intentos = 0
        while True:
            intento = int(input("Adivina el numero (1-100): "))
            intentos += 1
            if intento == secreto:
                print(f"Correcto, lo lograste en {intentos} intentos")
                break
            elif intento < secreto:
                print("Muy bajo")
            else:
                print("Muy alto")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

def generador_contrasenas():
    limpiar()
    cargar("Cargando")
    while True:
        longitud = int(input("¿De cuantos caracteres quieres la contrasena? "))
        caracteres = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(caracteres) for _ in range(longitud))
        print(f"Contrasena generada: {password}")
        repetir = input("¿Finalizaste la tarea? (s/n): ").lower()
        if repetir == "s":
            break
    cargar("Regresando al menu principal")

while True:
    limpiar()
    print("Menu principal")
    print("1. Variables y Tipos de Datos")
    print("2. Operaciones Aritmeticas")
    print("3. Operadores Logicos y Condicionales")
    print("4. Funciones y Recursividad")
    print("5. Loops: For")
    print("6. Loops: While")
    print("7. Listas y Manipulacion")
    print("8. Promedio de una lista")
    print("9. Palindromo")
    print("10. Contador de vocales")
    print("11. Conversor de temperatura")
    print("12. Adivina el numero")
    print("13. Generador de contrasenas")
    print("14. Salir de la app")

    try:
        resp = int(input("Selecciona una opcion para ejecutar: "))
    except ValueError:
        print("Por favor ingresa un numero valido")
        time.sleep(1.5)
        continue

    match resp:
        case 1: variables()
        case 2: aritmeticos()
        case 3: logicos_condicionales()
        case 4: funciones_recursividad()
        case 5: loop_for()
        case 6: loop_while()
        case 7: listas()
        case 8: promedio_lista()
        case 9: palindromo()
        case 10: contador_vocales()
        case 11: conversor_temperatura()
        case 12: adivina_numero()
        case 13: generador_contrasenas()
        case 14:
            print("Salir de la app")
            break
        case _:
            print("Opcion no valida")
            time.sleep(1.5)
