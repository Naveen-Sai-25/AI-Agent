# 🎙️ AI Voice Assistant for Windows

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Windows](https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows)
![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-success?style=for-the-badge)
![Automation](https://img.shields.io/badge/Desktop-Automation-orange?style=for-the-badge)

**An intelligent Python voice assistant capable of controlling your Windows PC using voice commands.**

</div>

---

# 📌 Features

## 🎤 Voice Recognition

- Listen to voice commands
- Convert speech to text
- Text-to-Speech responses

---

## 🌐 AI Platform Integration

Supports voice commands for:

- ChatGPT
- Gemini
- Claude
- Perplexity AI

### Example

```text
Search ChatGPT for Python decorators
Ask Gemini about quantum computing
Open Claude
```

---

## 🔍 Web Search

Search Google

```text
Search Artificial Intelligence
```

Search YouTube

```text
Search YouTube Python Tutorial
```

Open websites

- YouTube
- WhatsApp Web
- Chrome

---

## 💻 Windows Automation

Open applications

- Chrome
- Calculator
- Notepad
- Visual Studio Code
- File Explorer

Launch any application

```text
Open Spotify
Open Discord
Open Telegram
```

---

## 📝 Smart Live Dictation

Open Notepad and continuously dictate text.

```text
Type Hello everyone

Delete project

Stop writing
```

---

## 📷 Screenshot

```text
Take Screenshot
```

---

## 🔊 Volume Controls

```text
Volume Up

Volume Down

Mute
```

---

## 🔐 System Controls

```text
Lock Laptop

Shutdown Laptop

Restart Laptop

Cancel Shutdown
```

---

## 🔋 Battery Status

```text
Battery Status
```

Returns

- Battery Percentage
- Charging Status

---

## 🕒 Tell Time

```text
What is the time?
```

---

## 📋 Clipboard Support

```text
Copy to Clipboard Hello World
```

---

## 🖥️ Active Window Control

```text
Close This Window
```

---

## ⚡ Multiple Commands

Execute multiple commands in one sentence.

```text
Open Chrome and Open Calculator

Open Notepad then Open VS Code
```

---

# 🛠️ Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- PyAutoGUI
- psutil
- pyperclip
- subprocess
- ctypes
- urllib
- webbrowser

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Naveen-Sai-25/AI-Voice-Assistant.git
```

---

## 2️⃣ Navigate to the Project

```bash
cd AI-Voice-Assistant
```

---

## 3️⃣ Install Dependencies

Using requirements.txt

```bash
pip install -r requirements.txt
```

Or install manually

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install pyautogui
pip install psutil
pip install pyperclip
```

If PyAudio fails

```bash
pip install pipwin
pipwin install pyaudio
```

---

# ▶️ Run the Project

```bash
python agent.py
```

---

# 📂 Project Structure

```text
AI-Voice-Assistant/
│
├── agent.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ How This Project Works

The AI Voice Assistant continuously listens for voice commands, converts them into text, identifies the requested action, and executes it on the Windows system.

## 🏗️ Workflow

```text
                User Speaks
                     │
                     ▼
        🎤 SpeechRecognition Library
                     │
                     ▼
          Convert Speech to Text
                     │
                     ▼
        Command Processing Engine
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Browser Tasks   Windows Tasks   AI Platforms
      │              │              │
      ▼              ▼              ▼
 Chrome         Calculator      ChatGPT
 YouTube        Notepad         Gemini
 Google         VS Code         Claude
 WhatsApp       Explorer        Perplexity
      │              │              │
      └──────────────┼──────────────┘
                     ▼
           🗣️ Text-to-Speech Response
```

---

# 📖 Step-by-Step Working

## Step 1 — Initialize the Assistant

When `agent.py` starts, it initializes:

- Speech Recognition
- Text-to-Speech Engine
- Microphone
- Command Router
- Windows Automation Modules

```python
recognizer = sr.Recognizer()
engine = pyttsx3.init()
```

---

## Step 2 — Listen for Voice Commands

The assistant waits for the user to speak.

Example

```text
Open Chrome
```

or

```text
Search ChatGPT for Machine Learning
```

SpeechRecognition converts the spoken audio into text.

---

## Step 3 — Process the Command

The recognized text is analyzed to determine the requested action.

| Voice Command | Action |
|---------------|--------|
| Open Chrome | Launch Chrome |
| Open Calculator | Open Calculator |
| Search Python | Google Search |
| Open ChatGPT | Launch ChatGPT |
| Lock Laptop | Lock Windows |
| Battery Status | Display Battery Information |

---

## Step 4 — Execute the Command

The assistant performs the requested operation using Windows APIs and Python libraries.

Examples

- Open Applications
- Search Google
- Search YouTube
- Launch AI Platforms
- Take Screenshots
- Lock Laptop
- Control Volume
- Open File Explorer
- Live Dictation
- Clipboard Operations

---

## Step 5 — Respond Back

After executing the command, the assistant confirms the action using Text-to-Speech.

Example

```text
Opening Chrome...

Searching Google for Python...

Locking your laptop...

Screenshot saved.
```

---

# 🧠 Command Processing Architecture

```text
Voice Input
     │
     ▼
SpeechRecognition
     │
     ▼
Speech to Text
     │
     ▼
process_multiple_commands()
     │
     ▼
execute()
     │
     ├───────────────┐
     │               │
     ▼               ▼
AI Commands     Windows Commands
     │               │
     ▼               ▼
Browser        Automation
     │               │
     └───────┬───────┘
             ▼
      Text-to-Speech
```

---

# 📚 Python Libraries Used

| Library | Purpose |
|----------|---------|
| SpeechRecognition | Speech-to-Text |
| PyAudio | Microphone Input |
| pyttsx3 | Text-to-Speech |
| PyAutoGUI | Keyboard, Mouse & Screenshot Automation |
| psutil | Battery & System Information |
| pyperclip | Clipboard Operations |
| subprocess | Launch Windows Applications |
| webbrowser | Open Websites |
| ctypes | Windows API Access |
| urllib | Encode Search Queries |

---

# 💡 Example Voice Commands

```text
Open Chrome

Open Calculator

Open VS Code

Open File Explorer

Search Python Programming

Search YouTube Arduino Tutorial

Open ChatGPT

Search ChatGPT for Binary Search

Ask Gemini about Artificial Intelligence

Open Claude

Open Perplexity

Take Screenshot

Volume Up

Volume Down

Mute

Lock Laptop

Battery Status

Copy to Clipboard Hello World

What is the Time

Close This Window

Open Chrome and Open Calculator

Open Notepad then Open VS Code
```

---

# 🛠️ System Requirements

- Windows 10 / Windows 11
- Python 3.10+
- Working Microphone
- Internet Connection
- Google Chrome Installed

---

# 🚀 Future Improvements

- ✅ Wake Word Detection
- ✅ Offline Speech Recognition
- ✅ Weather Information
- ✅ Email Automation
- ✅ AI Memory
- ✅ Music Player Controls
- ✅ Smart Home Integration
- ✅ Face Recognition Login
- ✅ Linux & macOS Support

---

# 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository

git checkout -b feature-name

git commit -m "Added new feature"

git push origin feature-name
```

Then create a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Challa Naga Sai Lakshmi Naveen**

📧 Email: **naveensaichalla@gmail.com**

🌐 GitHub: https://github.com/Naveen-Sai-25

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

**Happy Coding! 🚀**

</div>
