# 🤖 Jarvis Voice Assistant


Jarvis is an **AI-powered Python voice assistant** that listens to your commands and performs tasks like opening websites, playing music, fetching live news, and answering general questions using OpenAI GPT.

---

## 🚀 Features
- **Voice Activation:** Wake Jarvis with the keyword `Jarvis`.
- **AI Chat Mode:** Uses OpenAI GPT (ChatGPT) for intelligent responses.
- **Website Control:** Open popular websites like Google, YouTube, Facebook, and LinkedIn.
- **Music Playback:** Play your favorite songs from a predefined music library.
- **Real-Time News:** Fetch and read top headlines using [NewsAPI](https://newsapi.org/).
- **Text-to-Speech:** Natural speech using `gTTS` (Google Text-to-Speech).
- **Speech Recognition:** Powered by the `speech_recognition` library.

---

## 🛠️ Technologies Used
- **Python 3.x**
- **SpeechRecognition** (Voice input)
- **gTTS / pyttsx3** (Text-to-Speech)
- **Webbrowser** (Website automation)
- **OpenAI API** (AI-powered responses)
- **NewsAPI** (Real-time headlines)
- **Pygame** (MP3 playback)

---

## 📂 Project Structure
Jarvis/
│
├── main.py # Main script (entry point)
├── musicLibrary.py # Dictionary of songs and links
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```
   ```bash
    pip install -r requirements.txt
   ```

2. **Add API Keys**
   
   ```bash
    newsapi = "<Your NewsAPI Key Here>"
    client = OpenAI(api_key="<Your OpenAI API Key Here>")
   ```
3. **Run the Project**
   
   ``` 
   python main.py
   ```

## 🧠 Example Commands

- **"Jarvis, open Google"**
- **"Jarvis, play despacito"**
- **"Jarvis, what's the news?"**
- **"Jarvis, who is Elon Musk?"** (AI response from GPT)


## REQUIREMENTS
- speechrecognition
- pyttsx3
- gTTS
- pygame
- requests
- openai
