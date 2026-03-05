import json


def leer_preguntas(path: str) -> list[str]:
    with open(path) as preguntas:
        return preguntas.read().splitlines()


def extraer_pregunta(pregunta: str) -> dict[str]:
    secciones = pregunta.split('|')
    pregunta = secciones[0]
    correcta = secciones[1]
    opciones = secciones[1:]
    return {
        "pregunta": pregunta,
        "correcta": correcta,
        "opciones": opciones
    }


def main():
    preguntas = leer_preguntas("preguntas.txt")
    preguntas = [extraer_pregunta(pregunta) for pregunta in preguntas]
    with open("preguntas.json", "w") as archivo:
        json.dump(preguntas, archivo)


if __name__ ==  "__main__":
    main()