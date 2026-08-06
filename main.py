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

# C1
print("C1")

pelicula = {
    "titulo": "La Odisea",
    "anio": 2025,
    "director": "Christopher Nolan"
}

print(pelicula["titulo"])

# C2
print("C2")

pelicula["puntaje"]= 9.5
pelicula["anio"]= 2026

print(pelicula)

# C3
print("C3")

# print(pelicula["duracion"])

duracion = pelicula.get("duracion", "Desconocida")

print(duracion)

# C4
print("C4")

peliculas = [
    {"titulo": "Taxi Driver", "anio": 1976, "director": "Martin Scorsese"},
    {"titulo": "Bastardos Sin Gloria", "anio": 2009, "director": "Quentin Tarantino"},
    {"titulo": "El Padrino", "anio": 1972, "director": "Francis Ford Coppola"}
]

for p in peliculas:
    print(p.get("titulo", "Desconocido"))

# C5
print("C5")

director_buscado = "Quentin Tarantino"
encontrado = False

for p in peliculas:
    if p["director"] == "Quentin Tarantino":
        print(p["director"])
        encontrado = True

if not encontrado:
    print("No hay ninguna pelicula del director deseado")

# C6
print("C6")

datos_1 = {"titulo": "Dune", "anio": 2021}
datos_2 = {"puntaje": 8, "anio": 2024}

combinado = datos_1 | datos_2

print(combinado)

# Se toman los datos del diccionario que esta despues de |. 
# Utilizando | se crea un tercer diccionario, datos_1 y datos_2 quedan iguales, conservando sus datos originales.
# Utilizando update(), se actualiza el diccionario deseado.

# C7
print("C7")

frase = "Ingenieria en Computacion 2 es la continuacion de Ingenieria en Computacion 1"
palabras = frase.split()

conteo = {}

for p in palabras:
    if p in conteo:
        conteo[p] += 1
    else:
        conteo[p] = 1

print(conteo)


# C8
print("C8")

inventario = {
    "mouse": {"precio": 70000, "stock": 6},
    "teclado": {"precio": 120000, "stock": 4},
    "monitor": {"precio": 200000, "stock": 3}
}

print(f"El precio del monitor es de ${inventario['monitor']['precio']}")

# D1
print("D1")

from funciones import promedio

resultado_1 = promedio([7, 4, 9, 10, 6])
print(resultado_1)

resultado_2 = promedio([3, 3, 3])
print(resultado_2)

# D2
print ("D2")

from funciones import aprobo

aprobo_1_d2 = aprobo([7, 4, 9, 10, 6])
print(aprobo_1_d2)

aprobo_2_d2 = aprobo([4, 6, 7, 3, 2])
print(aprobo_2_d2)

# D3
print("D3")

from funciones import estadisticas

estadisticas_d3 = estadisticas([7, 4, 9, 10, 6])
print(estadisticas_d3)

# D4
print("D4")

aprobo_1_d4 = aprobo([7, 4, 9, 8, 6])
print(aprobo_1_d4)

aprobo_2_d4 = aprobo([7, 4, 9, 8, 6], minimo = 7)
print(aprobo_2_d4)

# D5
print("D5")

promedio_1_d5 = promedio([])
print(promedio_1_d5)

promedio_2_d5 = promedio([5, 6, 7])
print(promedio_2_d5)

# D6
print("D6")

from funciones import reporte

reporte_d6 = reporte([7, 8, 6, 10, 4])
print(reporte_d6)

