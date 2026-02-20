# Wednesday — Jay's Desktop Voice Assistant 🖤

<img src="https://i.pinimg.com/736x/b7/61/29/b76129d9062e30fe4416de7981e8b319.jpg" alt="">

> *"I am Wednesday. Your personal AI assistant."*

A desktop voice assistant built with Python, personalized exclusively for **Jay Suryawanshi**. Wednesday listens, speaks, and handles everyday tasks — from searching the web to telling jokes and taking voice notes — all through simple voice commands.

## ⚡ Features

| Command | What it does |
|---|---|
| **Wikipedia search** | Searches and reads out Wikipedia summaries |
| **Google search** | Searches anything on Google |
| **YouTube play/search** | Plays or searches videos on YouTube |
| **Open apps & websites** | Launches macOS apps or opens websites by name |
| **Sing a song** | Wednesday sings a random song for you |
| **Tell time / date** | Announces the current time or date |
| **Tell a joke** | Delivers a random programmer joke |
| **System report** | Reads out your system info |
| **Take a note** | Saves a voice note to `wednesday_notes.txt` |
| **Flip a coin** | Randomly picks Heads or Tails |
| **Goodbye** | Personalized farewell conversation |

## 🛠 Built With

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> Python · pyttsx3 · SpeechRecognition · pywhatkit · wikipedia

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Jay-Suryawansh7/Wednesday-.git
cd Wednesday-

# Install dependencies
pip install pyttsx3 SpeechRecognition pywhatkit wikipedia pyaudio

# Run Wednesday
python3 main.py
```

> **Note:** On macOS you may need to install PortAudio first:
> `brew install portaudio`

## 📁 Project Structure

```
├── main.py          # Entry point — command loop
├── aivoice.py       # Speech engine (speak & listen)
├── commands.py      # All voice command handlers
├── ironman.jpg      # Assistant avatar
└── README.md
```

## 👤 Author

**Jay Suryawanshi**

- GitHub: [@Jay-Suryawansh7](https://github.com/Jay-Suryawansh7)

## ⭐ Support

If this project helped you, give it a ⭐!
