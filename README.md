# Assistente de Voz & IA Local

Um assistente em **Python** que ouve comandos de voz em português, responde por voz e executa ações locais ou delega perguntas a um modelo LLM (Ollama).

---

## 🚀 Funcionalidades

- Reconhecimento de fala via `speech_recognition` (Google API)  
- Síntese de voz com `pyttsx3`  
- Comandos locais:  
  - Saudação (“olá”)  
  - Consulta de hora ("me diga a hora")  
  - Pesquisa no Google ("pesquisar por")
  - Abrir notícias ("notícias de hoje")
  - Encerrar sessão (“sair”)  
- Fallback para IA: manda o prompt ao modelo local Ollama (`llama3:8b`)  
- Estrutura modular para áudio, comandos e IA  

---

## 📝 Pré-requisitos

- Python 3.10+  
- Microfone e saída de áudio configurados no sistema  
- Ollama instalado e modelo `llama3:8b` pronto para uso  
- (Opcional) Conta Twilio para envio de SMS, caso queira estender a funcionalidade  

---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/assistente-voz-ia.git
   cd assistente-voz-ia
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Verifique se o Ollama está funcionando:
   ```bash
   ollama run llama3:8b "Olá, mundo!"
   ```

---

## 🏃 Como usar

1. Execute o script principal:
   ```bash
   python main.py
   ```

2. Fale um comando em **português**:
   - “olá” → o assistente responde saudando  
   - “me diga a hora” → informa hora atual  
   - “pesquisar por <termo>” → abre pesquisa no Google  
   - “notícias de hoje” → abre Google News  
   - “sair” → encerra o assistente  
   - qualquer outra coisa → encaminha ao Ollama e fala a resposta  



