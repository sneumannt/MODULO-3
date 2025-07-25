# Formulario simple que usa distintos tipos de datos

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estudiante = input("¿Eres estudiante? (sí/no): ").lower() == "sí"

print("\nResumen del formulario:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Peso: {peso} kg")
print(f"¿Es estudiante?: {'Sí' if estudiante else 'No'}")
