def promedio(notas):
    if len(notas) == 0:
        return ("No hay notas para promediar")
    resultado = sum(notas)/len(notas)
    return resultado

def aprobo(notas, minimo = 6):
    prom = promedio(notas)
    if prom >= minimo:
        return (True)
    else:
        return (False)

def estadisticas(notas):
    return {
        "promedio": sum(notas)/len(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }

def reporte(notas):
    datos = estadisticas(notas)

    return f"Promedio: {datos['promedio']} | Máximo: {datos['maximo']} | Mínimo: {datos['minimo']}"

def duracion_pelicula(pelicula):
    return pelicula.get("duracion", "Desconocida")

# H1

def leer_peliculas(archivo_csv):
    peliculas = []
    with open(archivo_csv) as archivo:
        for indice, linea in enumerate(archivo):
            if indice == 0:
                continue
            partes = linea.strip().split(",")
            pelicula = {
                "titulo": partes[0],
                "anio": int(partes[1]),
                "puntaje": float(partes[2]),
                "genero": partes[3]
            }
            peliculas.append(pelicula)
    return peliculas

def extraer_puntajes(peliculas):
    puntajes = []
    for pelicula in peliculas:
        puntajes.append(pelicula["puntaje"])
    return puntajes