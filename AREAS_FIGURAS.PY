# Cálculo del área de diferentes figuras geométricas

def area_cuadro(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    pi = 3.1416
    return pi * radio ** 2

print("--- Cálculo de Áreas ---")
print("1. Cuadro")
print("2. Rectángulo")
print("3. Círculo")

opcion = input("Elige una figura: ")

if opcion == "1":
    lado = float(input("Lado del cuadro: "))
    print(f"Área: {area_cuadro(lado)}")
elif opcion == "2":
    base = float(input("Base del rectángulo: "))
    altura = float(input("Altura: "))
    print(f"Área: {area_rectangulo(base, altura)}")
elif opcion == "3":
    radio = float(input("Radio del círculo: "))
    print(f"Área: {area_circulo(radio)}")
else:
    print("Opción no válida.")

