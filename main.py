import speech_recognition as sr
import webbrowser
import pyttsx3
# from openai import OpenAI (exhausted their free plan so using gemini api)
import google.generativeai as genai
import requests
from gtts import gTTS
import pygame
from dotenv import load_dotenv
import os
from musicLibrary import music
USE_ONLINE_TTS = True

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

genai.configure(api_key=gemini_api_key)

# Text-to-speech function
def speak(text):
    print(f"Nova: {text}")
    if USE_ONLINE_TTS:
        tts = gTTS(text=text, lang='en')
        filename = "temp.mp3"
        tts.save(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        pygame.mixer.quit()
        os.remove(filename)
    else:
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate + 50)  # increase speed
        engine.say(text)
        engine.runAndWait()


# Listen & recognize voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

# Ask gemini
def ask_gemini(question):
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    prompt = f"{question} (Please answer briefly in 2-3 sentences)"
    response = model.generate_content(prompt)
    speak(response.text)

# Open website
def open_website(site):
    speak(f"Opening {site}")
    if site == "google":
        webbrowser.open("https://www.google.com")
    elif site == "youtube":
        webbrowser.open("https://www.youtube.com")
    elif site == "facebook":
        webbrowser.open("https://www.facebook.com")
    elif site == "linkedin":
        webbrowser.open("https://www.linkedin.com")
    else:
        speak("Sorry, I don't know that site.")

# Play music (demo: opens YouTube link)
def play_music():
    speak("Playing music")
    webbrowser.open("https://youtu.be/JgDNFQ2RaLQ?feature=shared")

def play_music_by_name(command):
    for song in music:
        if song.lower() in command:
            speak(f"Playing {song}")
            webbrowser.open(music[song])
            return
    speak("Sorry, I couldn't find that song.")
    
def get_news():
    api_key = news_api_key
    url = f"https://newsapi.org/v2/everything?q=india&apiKey={api_key}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data["status"] == "ok":
            articles = data["articles"][:5]
            for article in articles:
                speak(article["title"])
        else:
            speak("Sorry, I couldn't fetch the news.")
    except Exception as e:
        speak("Sorry, there was a problem fetching the news.")


# Main loop
def main():
    speak("Initializing Nova...")
    speak("Say 'Nova' to activate me.")
    while True:
        text = listen()
        if "nova" in text:
            speak("Ya?")
            command = listen()

            if "stop" in command or "exit" in command or "bye" in command:
                speak("Goodbye!")
                exit()

            elif "open" in command:
                if "google" in command:
                    open_website("google")
                elif "youtube" in command:
                    open_website("youtube")
                elif "facebook" in command:
                    open_website("facebook")
                elif "linkedin" in command:
                    open_website("linkedin")
                else:
                    speak("Website not recognized.")

            elif "play" in command:
                if "music" in command:
                    play_music()
                else:
                    play_music_by_name(command)

            elif "get news" in command:
                get_news()

            else:
                ask_gemini(command)

        else:
            speak("Wake word not detected. Say 'Nova' to start.")


if __name__ == "__main__":
    main()
