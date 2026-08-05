# A1
print("A1")

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
print("A2")

cantidad_string = "5"
precio = 100

cantidad_numero = int(cantidad_string)

resultado = cantidad * precio
print(resultado)
print(type(cantidad_string))
print(type(cantidad_numero))
print(type(precio))

# A3
print("A3")

celsius = [0, 100]
fahrenheit = []

for c in celsius:
    f = c * (9/5) + 32
    fahrenheit.append(f)

print (fahrenheit)

# A4
print("A4")

prueba = [7, 8, 10]

promedio_prueba = sum(prueba) / len(prueba)
promedio_prueba_redondeado = round(promedio_prueba, 1)

promedio_A1_redondeado = round(promedio, 1)

print(promedio_prueba_redondeado)
print(promedio_A1_redondeado)  

# A5
print("A5")

edad = [17, 18, 0]

for e in edad:  
    if e >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

# A6
print("A6")

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
print("A7")

km = 50

millas = km * 0.62
pies = millas * 5280

print(km)
print(millas)
print(pies)

# B1
print("B1")

playlist = ["Motor Psico", "Fell On Black Days", "Black", "Everlong", "I Sat by the Ocean"]

print(playlist)
print(playlist[0])
print(playlist[-1])

# B2
print("B2")

playlist.append("Yo Canibal")
playlist.append("Driven Under")

print(len(playlist))

# B3
print("B3")

puntajes = [120, 45, 300, 80, 210]

mas_alto = puntajes[0]
mas_bajo = puntajes[0]

for p in puntajes:
    if p > mas_alto:
        mas_alto = p
    if p < mas_bajo:
        mas_bajo = p

promedio_puntajes = sum(puntajes)/len(puntajes)

print(mas_alto, mas_bajo, promedio_puntajes)
print(max(puntajes), min(puntajes))

# B4
print("B4")

filtrados = []

for p in puntajes:
    if p > 100:
        filtrados.append(p)

print(filtrados)
print(puntajes)

# B5
print("B5")

# --- B5: Ranking ---
puntajes = [120, 45, 300, 80, 210]

ordenados = sorted(puntajes, reverse=True)

print(ordenados)
print(puntajes)

# B6
print("B6")

playlist_invertida = playlist[::-1]

print(playlist_invertida)
print(playlist)

# B7
print("B7")

numeros = [3, 5, 3, 8, 5, 1, 8, 8]

sin_repetidos = set(numeros)

print(sin_repetidos)

# B8
print("B8")

lecturas = [18, 23, 19, 27, 16, 18, 21, 22, 24, 17]

moviles = []

for i in range(len(lecturas)-2):
    ventana = lecturas[i : i+3]
    promedio_ventana = sum(ventana)/len(ventana)
    moviles.append(round(promedio_ventana, 2))

print(moviles)
print(len(moviles))