# 🌟 Nova - Voice-Activated Virtual Assistant

Nova is a Python-based voice-activated virtual assistant that can browse the web, play music, fetch news, and answer your questions using Google's Gemini API.\
Inspired by AI assistants like Alexa and Google Assistant.

---

## ✨ **Features**

✅ **Voice Recognition**

- Listens for and recognizes voice commands with `speech_recognition`.
- Activates when it hears the wake word **"Nova"**.

✅ **Text-to-Speech**

- Reads responses aloud.
- Uses:
  - `gTTS` (Google Text-to-Speech) + `pygame` for online speech.
  - `pyttsx3` for local/offline speech.

✅ **Web Browsing**

- Opens Google, YouTube, Facebook, or LinkedIn on command.

✅ **Music Playback**

- Plays predefined songs using YouTube links from `musicLibrary.py`.

✅ **News Fetching**

- Fetches and reads out the latest India news headlines using NewsAPI.

✅ **Gemini API Integration**

- Answers general queries with responses from Gemini (Gemini 1.5 Flash).

---

## 🧠 **Workflow**

1. **Initialization**
   - Greets user: *"Initializing Nova..."*
2. **Wake Word Detection**
   - Listens for "Nova".
   - On detection: says *"Ya?"*
3. **Command Processing**
   - Opens websites, plays music, fetches news, or answers questions via Gemini.
4. **Speech Output**
   - Speaks the result back to you.

---

## 📦 **Libraries Used**

- `speech_recognition`
- `webbrowser`
- `pyttsx3`
- `gTTS`
- `pygame`
- `requests`
- `google.generativeai` (Gemini)
- `os`
- `dotenv`
- `musicLibrary` (custom)

---

## ⚙ **Setup & Installation**

1. **Clone the repository:**

```bash
git clone https://github.com/Shreya-nipunge/Voice-Activated-Virtual-Assistant.git
cd Voice-Activated-Virtual-Assistant
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add your API keys:**

- Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

- Open `.env` and add your keys:

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key
```

4. **Run the project:**

```bash
python main.py
```

---

## 📁 **Project Structure**

```
├── main.py
├── musicLibrary.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 **How to Use**

- Say **"Nova"** to wake the assistant.
- Then:
  - *"Open Google"* → opens Google.
  - *"Play Dynamite"* → plays song from `musicLibrary.py`.
  - *"Get news"* → fetches and reads headlines.
  - *Any question* → answered by Gemini.

To stop Nova, say **"stop"**, **"exit"**, or **"bye"**.

---

## 🛡 **Note**

Your real API keys should **never** be committed to GitHub.\
This project uses `.env` to keep them private.

---

✨ *Made with Python for learning and fun!*

