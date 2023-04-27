# Imprimir un mensaje de bienvenida
print("Bienvenido a la calculadora")

# Bucle while para permitir al usuario realizar múltiples cálculos
while True:
    # Mostrar las opciones de operación disponibles
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Solicitar al usuario que ingrese la opción deseada
    opcion = int(input("Ingrese una opción: "))

    # Si el usuario selecciona la opción 5, salir del bucle while y finalizar el programa
    if opcion == 5:
        print("Hasta luego")
        break

    # Solicitar al usuario que ingrese los dos números a calcular
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la operación correspondiente según la opción seleccionada por el usuario
    if opcion == 1:
        resultado = num1 + num2
    elif opcion == 2:
        resultado = num1 - num2
    elif opcion == 3:
        resultado = num1 * num2
    elif opcion == 4:
        # Verificar si el segundo número es cero antes de realizar la división
        if num2 == 0:
            print("Error: no se puede dividir entre cero")
            continue
        resultado = num1 / num2
    else:
        print("Opción inválida")
        continue

    # Imprimir el resultado de la operación
    print("El resultado es:", resultado)