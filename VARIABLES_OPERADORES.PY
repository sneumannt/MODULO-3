# Conversor de temperaturas de Celsius a Fahrenheit y Kelvin

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius} °C equivalen a {fahrenheit} °F y {kelvin} K")

