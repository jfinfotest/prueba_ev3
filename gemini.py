from google import genai

# Función que genera la respuesta
def generar_respuesta(prompt: str) -> str:
    if not prompt:
        return "Por favor, ingresa un tema o pregunta."
    try:
        client = genai.Client(api_key="AIzaSyAl-dcF-3pWwNx7-owuCkJlpj_C3h0yqbI")  # Código original
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt  # Código original con prompt dinámico
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Lógica principal (interfaz de consola)
print("Chat con Gemini")
print("Ingresa un tema o pregunta para obtener una respuesta generada por Gemini.")
print("Escribe 'salir' para terminar.\n")

while True:
    prompt = input("Escribe tu pregunta o tema: ").strip()
    if prompt.lower() == 'salir':
        print("¡Hasta luego!")
        break
    if prompt:
        print("Generando respuesta...\n")
        respuesta = generar_respuesta(prompt)
        print("Respuesta:")
        print(respuesta)
        print("\n" + "="*50 + "\n")
    else:
        print("Por favor, ingresa un tema o pregunta válida.\n")
