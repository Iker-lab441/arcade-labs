import json
import random


def extraer_preguntas(path: str) -> list[dict[str]]:
    with open(path) as preguntas:
        return json.load(preguntas)


def mostrar_pregunta_y_opciones(pregunta: dict[str]) -> None:
    print(pregunta["pregunta"])

    random.shuffle(pregunta["opciones"])

    for n, opcion in enumerate(pregunta["opciones"]):
        print(f"{chr(n + ord('a'))}. {opcion}")


def pedir_respuesta(pregunta: dict[str]) -> str:
    respuesta = -1

    while respuesta < 0 or respuesta >= len(pregunta["opciones"]):
        respuesta = input("Elige tu respuesta: ").lower()
        if len(respuesta) != 1:
            respuesta = -1
        else:
            respuesta = ord(respuesta) - ord('a')

    respuesta = pregunta["opciones"][respuesta]

    return respuesta


def es_respuesta_correcta(pregunta: dict[str], respuesta: str) -> bool:
    return respuesta == pregunta["correcta"]


def main():
    puntos_por_respuesta = 5

    preguntas = extraer_preguntas("preguntas.json")
    random.shuffle(preguntas)

    puntos = 0

    for pregunta in preguntas:
        mostrar_pregunta_y_opciones(pregunta)
        respuesta = pedir_respuesta(pregunta)

        if es_respuesta_correcta(pregunta, respuesta):
            print(f"¡Respuesta correcta! +{puntos_por_respuesta} puntos.")
            puntos += puntos_por_respuesta
        else:
            print("Respuesta incorrecta...")
        print()

    print(f"Has conseguido un total de {puntos} puntos.")


if __name__ == "__main__":
    main()