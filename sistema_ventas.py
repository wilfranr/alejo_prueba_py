#mostrar programas disponibles
#registrar ventas de cualquier programa 
#consultar los ingresos acumulados por programa
#mostrar el total general de infresos al dia
#salir del sistema

# Datos base
programa1 = "Java de Cero a Senior"
programa2 = "Python con IA Aplicada"
programa3 = "Mobile Senior con IA"

precio1 = 1800000
precio2 = 1800000
precio3 = 1800000

ventas1 = 0
ventas2 = 0
ventas3 = 0

def mostrar_programas():
    print("\n--- PROGRAMAS DISPONIBLES ---")
    print(f"1. {programa1} - ${precio1:,}")
    print(f"2. {programa2} - ${precio2:,}")
    print(f"3. {programa3} - ${precio3:,}")

def registrar_venta():
    global ventas1, ventas2, ventas3
    print("\n--- REGISTRAR VENTA ---")
    print("1. Java de Cero a Senior")
    print("2. Python con IA Aplicada")
    print("3. Mobile Senior con IA")
    opcion = input("Seleccione el programa (1-3): ")
    
    if opcion in ['1', '2', '3']:
        cantidad = input("Ingrese la cantidad de estudiantes: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if opcion == '1':
                ventas1 += cantidad
            elif opcion == '2':
                ventas2 += cantidad
            elif opcion == '3':
                ventas3 += cantidad
            print(" Venta registrada correctamente.")
        else:
            print(" Error: Ingrese un número válido.")
    else:
        print(" Opción inválida.")

def consultar_ingresos():
    ingreso1 = ventas1 * precio1
    ingreso2 = ventas2 * precio2
    ingreso3 = ventas3 * precio3

    print("\n--- INGRESOS POR PROGRAMA ---")
    print(f"{programa1}: ${ingreso1:,}")
    print(f"{programa2}: ${ingreso2:,}")
    print(f"{programa3}: ${ingreso3:,}")
#función total de ingresos
def total_ingresos():
    total = (ventas1 * precio1) + (ventas2 * precio2) + (ventas3 * precio3)
    print("\n Total general del día: ${:,}".format(total))

#Función menu para interactuar con el usuario
def menu():
    while True:
        print("\n===== SISTEMA DE VENTAS DEV SENIOR CODE =====")
        print("1. Mostrar programas disponibles")
        print("2. Registrar venta")
        print("3. Consultar ingresos por programa")
        print("4. Mostrar total general del día")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            mostrar_programas()
        elif opcion == '2':
            registrar_venta()
        elif opcion == '3':
            consultar_ingresos()
        elif opcion == '4':
            total_ingresos()
        elif opcion == '5':
            print(" ¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print(" Opción inválida.")

menu()
