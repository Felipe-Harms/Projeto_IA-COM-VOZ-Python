import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import subprocess
import json

#inicia rec voz e sintizador 

recognizer = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    #ouve o comando de voz e retorna texto
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Escutando...")
        audio = recognizer.listen(source)
        try:
            print("Reconhecendo...")
            command = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse:{command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Desculpe. não entendi o que disse")
            return ""
        except sr.RequestError:
            print("Desculpe, o reconhecimento de voz não está disponível")
            return ""
        
def chat_with_ollama(prompt):
    """Envia a pergunta para o modelo do Ollama e retorna a resposta."""
    try:
        command = f'ollama run llama3:8b "{prompt}"'
        print(f"Executando comando: {command}")  # Verifique o comando
        response = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        
        if response.returncode == 0:
            return response.stdout.strip()  # Retorna a resposta limpa
        else:
            print(f"Erro no comando: {response.stderr}")
            return "Erro ao chamar a IA local."
    except Exception as e:
        print(f"Erro ao acessar o Ollama: {e}")
        return f"Erro: {e}"
    
def process_command(command):
    #processa o comando e executa a ação correspondente
    if "olá" in command:
        speak("Olá! Como posso ajuda-lo ?")
    elif "me diga a hora" in command:
        from datetime import datetime
        now = datetime.now()
        speak(f"Agora são {now.hour} e {now.minute} minutos.")
    if "pesquisar por" in command:
        search_term = command.replace("pesquisar por", "").strip()
        url = f"https://www.google.com/search?q={search_term}"
        speak(f"Pesquisando por {search_term}")
        webbrowser.open(url)
    if "notícias de hoje" in command:
        speak("Abrindo as últimas notícias")
        webbrowser.open("https://news.google.com/")
    elif "sair" in command:
        speak("Até logo")
        return True
    else:
        # Se não for um comando pré-definido, chama o Ollama
        speak("acessando inteligência artificial...")
        response = chat_with_ollama(command)
        print(f"Ollama: {response}")
        speak(response)
        return False

      
def main():
    speak("Olá! Eu sou Cortana, como posso ajudar ?")
    while True:
        command = listen()
        if command:
            if process_command(command):
                break

if __name__ == "__main__":
    main()