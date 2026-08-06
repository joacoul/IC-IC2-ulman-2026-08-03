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