import openai  # Importar la biblioteca openai
import sys     # Importar la biblioteca system

openai.api_key = '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'   # llave unica para ejecutar la API

# Verificar si se proporciona el argumento "--convers" en los argumentos de línea de comandos
convers_flag = "--convers" in sys.argv

if convers_flag:
    sys.argv.remove("--convers")  # Remover la opción para que no interfiera con argparse u otros parsers de argumentos

buffer = []  # Inicializar el buffer de consultas
last_query = ""  # Inicializar la última consulta realizada

def chatGPT(query):
    """
    Realiza una consulta a la API de OpenAI para obtener una respuesta generada por GPT-3.5.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": query}
            ],
            temperature=0.7,  
            max_tokens=150,   
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error al generar respuesta:", e)
        return None

def main():
    """
    Función principal que maneja la interacción con el usuario y la comunicación con la API de OpenAI.
    """
    global last_query  # Permitir el acceso a la variable global last_query

    # Mensaje de bienvenida
    print("Bienvenido a ChatGPT en Python. Puedes empezar a escribir y recibirás respuestas generadas por GPT-3.5.")
    print("Escribe 'exit' para salir.")

    # Bucle principal para interactuar con el usuario
    while True:
        try:
            user_query = input("You: ")  # Obtener la consulta del usuario

            # Verificar si el usuario quiere salir del programa
            if user_query.lower() == "exit":
                print("Hasta luego!")
                if last_query:
                    print("La última consulta fue:", last_query)
                break
            
            # Verificar si la consulta del usuario está en blanco
            if user_query.strip() == "":
                print("Por favor, ingresa una consulta válida.")
                continue

            # Verificar si estamos en modo conversación
            if convers_flag:
                buffer.append(user_query)  # Agregar la consulta al buffer

                # Utilizar la última consulta realizada agregada a todas las anteriores
                response = chatGPT(" ".join(buffer))

                if response is not None:
                    print("ChatGPT:", response)
                    buffer.append(response)  # Agregar la respuesta al buffer para ser re-enviada

            else:
                response = chatGPT(user_query)
                print("ChatGPT:", response)

            last_query = user_query  # Guardar la última consulta realizada

        except KeyboardInterrupt:
            print("Interrumpiste el programa.")
            break
        except Exception as e:
            print("Se produjo un error:", e)

if __name__ == "__main__":
    main()
