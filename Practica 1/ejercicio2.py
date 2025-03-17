# Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius 
# y luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

temp = float(input("Ingrese una temperatura en grados celsius: "))
temp_f = (temp * 9) / 5 + 32
print ("en grados fahrenheit seria: ",temp_f,"°F")