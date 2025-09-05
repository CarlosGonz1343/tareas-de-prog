from ollama import chat, generate
import sys
def usar_ollama_chat(prompt: str):
    """
    funcion para chatear con ollama usando formato de mensaje.
    """
    try:
        resp=chat(
            model="phi", #cobra caro el GPT XDDD
            messages=[
                {"role": "system", "content": "eres un asistente virtual util y amigable"},
                {"role": "user", "content": prompt}
            ]
        )
        print("\n respuesta (chat):")
        print(resp["message"]["content"])
    except Exception as e:
        print(f"error en usar_ollama_chat: {e}")

def usar_ollama_generate(prompt: str):
    """
    funcion para generar texto con un promt directo
    """
    try:
        resp=generate(
            model="phi",
            prompt=prompt
        )
        print("\n respuesta (generate):")
        print(resp["response"])
    except Exception as e:
        print(f"error en usar_ollama_generate: {e}")

def usar_ollama_stream(prompt: str):
    """
    funcion para tener respuesta en streaming (flujo de tiempo real)
    """
    try:
        stream=generate(
            model="phi",
            prompt=prompt,
            stream=True
        )
        for chunk in stream:
            print(chunk["response"], end="", flush=True)
        print("\n---fin del stream---")
    except Exception as e:
        print(f"error en usar_ollama_stream: {e}")

if __name__ == "__main__":
    print("=== proyecto Multi-IA con Ollama ===")
    print("1. chat")
    print("2. generate")
    print("3. stream")
    opcion=input("elige una opcion (1/2/3): ")

    prompt= input("\nescribe tu prompt:\n")

    if opcion == "1":
        usar_ollama_chat(prompt)
    elif opcion == "2":
        usar_ollama_generate(prompt)
    elif opcion == "3":
        usar_ollama_stream(prompt)
    else:
        print("opcion invalida")
        sys.exit(1)

