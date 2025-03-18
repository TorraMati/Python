import random
import sys

# Verifico si respuesta son digitos enteros positivos y si esta dentro del rango
def chequeo():
    respuesta = input("Respuesta: ")
    if respuesta.isdigit():
        respuesta_entera = int(respuesta)
        if respuesta_entera in {1,2,3,4}:
            return respuesta_entera - 1
    print("Respuesta no valida")
    sys.exit(1)

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Inicializo puntos en 0
puntos = 0.0
# Combinamos las 3 listas en una lista de tuplas
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for question, answer_options, correct_answers in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer_options):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = chequeo()
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers:
            print("¡Correcto!")
            # Sumo puntos si acierto
            puntos += 1
            break
        else:
            # Descuento puntos si fallo
            puntos -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answer_options[correct_answers])

    # Se imprime un blanco al final de la pregunta
    print()
# Se imprime el puntaje obtenido    
print("Puntaje obtenido: ",puntos)    