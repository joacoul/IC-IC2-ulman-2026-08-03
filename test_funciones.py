import pytest
from funciones import promedio, aprobo, estadisticas, duracion_pelicula

# G1

def test_promedio():
    resultado = promedio([7, 4, 9, 10, 6])
    assert resultado == 7.2

# G2

# def test_promedio_falla():
#    resultado = promedio([7, 4, 9, 10, 6])
#    assert resultado == 7.3

# G3

def test_aprobo_caso_aprueba():
    assert aprobo([7, 8, 9]) == True

def test_aprobo_caso_no_aprueba():
    assert aprobo([5, 4, 3]) == False

def test_aprobo_caso_limite():
    assert aprobo([6, 6, 6]) == True

# G4   

def test_estadisticas():
    resultado = estadisticas([7, 4, 9, 10, 6])
    assert resultado["promedio"] == 7.2
    assert resultado["maximo"] == 10
    assert resultado["minimo"] == 4

# G5

def test_duracion_pelicula_sin_dato():
    pelicula_sin_duracion = {"titulo": "Dune", "anio": 2021}
    resultado = duracion_pelicula(pelicula_sin_duracion)
    assert resultado == "Desconocida"

# G6

def test_promedio_lista_vacia():
    resultado = promedio([])
    assert resultado == "No hay notas para promediar"

# G7

@pytest.mark.parametrize("notas, esperado", [
    ([7, 8, 9], True),
    ([5, 4, 3], False),
    ([6, 6, 6], True),
])

def test_aprobo_parametrizado(notas, esperado):
    assert aprobo(notas) == esperado