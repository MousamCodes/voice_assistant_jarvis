# **Jarvis – Python Voice Assistant**

Jarvis is a simple yet powerful Python-based voice assistant designed to perform basic tasks using voice commands. It leverages speech recognition and text-to-speech technology to interact with users in real-time.

---

## **Features**
- **Website Interaction**
  - Open popular websites like **Google**, **YouTube**, **Instagram**, and **GitHub**.
  - Perform **Google searches** directly through voice commands.
  
- **Music Playback**
  - Play predefined songs from a custom `musicLibrary.py` file.

- **Voice Command Recognition**
  - Responds to the wake word **"Jarvis"** and executes specific commands.  

- **Text-to-Speech Feedback**
  - Uses `pyttsx3` for natural-sounding voice responses.

---

## **Technologies Used**
- **Python 3.x** – Core programming language.
- **SpeechRecognition** – Converts speech to text.  
- **pyttsx3** – Converts text to speech (offline).  
- **Webbrowser** – Handles website interactions.  
- **pocketsphinx (optional)** – For offline speech recognition.
- ![Python](https://img.shields.io/badge/Python-3.x-blue) 
- ![License](https://img.shields.io/badge/License-MIT-green)

---

## **How It Works**
1. Say **"Jarvis"** to activate the assistant.  
2. Give a command like:
   - `open google`
   - `search in google Python tutorials`
   - `play <song_name>`
3. Jarvis processes the command and responds via voice.

---


## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/MousamCodes/voice_assistant_jarvis.git
   cd voice_assistant_jarvis
