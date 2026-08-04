# A1

notas = [7, 4, 9, 10, 6]

total = sum(notas)
cantidad = len(notas)
promedio = total / cantidad

print(promedio)

if promedio >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# A2

cantidad_string = "5"
precio = 100

cantidad_numero = int(cantidad_string)

resultado = cantidad * precio
print(resultado)
print(type(cantidad_string))
print(type(cantidad_numero))
print(type(precio))

# A3

celsius = [0, 100]
fahrenheit = []

for c in celsius:
    f = c * (9/5) + 32
    fahrenheit.append(f)

print (fahrenheit)

# A4
prueba = [7, 8, 10]

promedio_prueba = sum(prueba) / len(prueba)
promedio_prueba_redondeado = round(promedio_prueba, 1)

promedio_A1_redondeado = round(promedio, 1)

print(promedio_prueba_redondeado)
print(promedio_A1_redondeado)  

# A5
edad = [17, 18, 0]

for e in edad:  
    if e >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

# A6
alumnos = list(range(1, 31))

pares = []
impares = []

for numero in alumnos:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(len(pares))
print(len(impares))

# A7

km = 50

millas = km * 0.62
pies = millas * 5280

print(km)
print(millas)
print(pies)