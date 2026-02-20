from datetime import datetime
from aivoice import *
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import subprocess
import random


def greatings():
    print("Initializing.....")
    os.system("clear")
    wednesday_speak("Initialized Successfully...")
    os.system("clear")
    hour = int(datetime.datetime.now().hour)
    greet = ""
    text = ""
    if 0 <= hour < 12:
        greet = "Good morning Jay"
        text = "I am Wednesday, your personal AI Assistant. What can I do for you today?"
    elif 12 <= hour < 17:
        greet = "Good Afternoon Jay"
        text = "I am Wednesday. How was your morning Jay?"
    elif hour >= 17:
        greet = "Good evening Jay"
        text = "I am Wednesday. Hope your day was productive Jay"
    wednesday_speak(greet)
    wednesday_speak(text)
    os.system("clear")


def ar_wiki(text):
    query = text
    query = query.replace("wikipedia", "")
    query = query.replace("wednesday", "")
    result = wikipedia.summary(query, sentences=2)
    wednesday_speak("According to wikipedia")
    wednesday_speak(result)


def goosearch(query):
    if query == "google":
        query = query.replace("google", "")
    if "google" in query:
        query = query.replace(" google ", " ")
        query = query.replace("google ", " ")
        query = query.replace(" google", " ")
    if "search" in query:
        query = query.replace(" search ", " ")
        query = query.replace(" search", " ")
        query = query.replace("search ", " ")
    if "on" in query:
        query = query.replace(" on ", " ")
    " "
    if query == "":
        wednesday_speak("Please say 'Yes' if you want to Open Google and 'No' if want to search Anything")
        cmd = wednesday_listen()
        if cmd == "yes":
            wednesday_speak("Opening Google Jay")
            webbrowser.open("https://www.google.com")
        else:
            wednesday_speak("What to search Jay?")
            while True:
                search = wednesday_listen()
                if search is None or search == "":
                    continue
                else:
                    wednesday_speak(f"searching {search} on google Jay")
                    pywhatkit.search(search)
                    break
    else:
        search = query
        wednesday_speak(f"searching {search} on google Jay")
        pywhatkit.search(search)


def youtube(query):
    if query == "youtube":
        query = query.replace("youtube", "")
    if "youtube" in query:
        query = query.replace(" youtube", " ")
        query = query.replace(" youtube ", " ")
        query = query.replace(" on ", " ")
    " "
    if query == "":
        wednesday_speak("Please say 'Yes' if you want to Open Youtube and 'No' if want to search Anything")
        cmd = wednesday_listen()
        if cmd == "yes":
            wednesday_speak("Opening Youtube Jay")
            webbrowser.open("https://www.youtube.com")
        else:
            wednesday_speak("Jay, do you want to Search or Play Something on Youtube?")
            text = wednesday_listen()

            if "search" in text:
                wednesday_speak("What to search Jay?")
                while True:
                    search = wednesday_listen()
                    if search is None or search == "":
                        continue
                    else:
                        if "search" in search:
                            search = search.replace(" search ", " ")
                            search = search.replace("search ", " ")
                        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                        wednesday_speak(f"searching {search} on youtube Jay")
                        break
            else:
                wednesday_speak("What to play Jay?")
                while True:
                    search = wednesday_listen()
                    if search is None or search == "":
                        continue
                    else:
                        if " play " in search:
                            search = search.replace("play ", " ")
                            search = search.replace(" play ", " ")
                        pywhatkit.playonyt(search)
                        wednesday_speak(f"Playing {search} on youtube Jay")
                        break
    elif "play" in query:
        query = query.replace("play ", " ")
        query = query.replace(" play ", " ")
        pywhatkit.playonyt(query)
        wednesday_speak(f"Playing {query} on youtube Jay")

    elif "search" in query:
        query = query.replace(" search ", " ")
        query = query.replace("search ", " ")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        wednesday_speak(f"Searching {query} on youtube Jay")


# ── Website Launcher ─────────────────────────────────────────────────
WEBSITE_ALIASES = {
    "linkedin": "https://www.linkedin.com",
    "github": "https://www.github.com",
    "twitter": "https://www.twitter.com",
    "x": "https://www.x.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "reddit": "https://www.reddit.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://open.spotify.com",
    "chatgpt": "https://chat.openai.com",
    "whatsapp": "https://web.whatsapp.com",
    "amazon": "https://www.amazon.com",
    "stack overflow": "https://stackoverflow.com",
    "stackoverflow": "https://stackoverflow.com",
    "gmail": "https://mail.google.com",
    "drive": "https://drive.google.com",
    "maps": "https://maps.google.com",
}


# ── System App Launcher ──────────────────────────────────────────────
APP_ALIASES = {
    "calculator": "Calculator",
    "notes": "Notes",
    "safari": "Safari",
    "finder": "Finder",
    "terminal": "Terminal",
    "music": "Music",
    "calendar": "Calendar",
    "settings": "System Preferences",
    "system preferences": "System Preferences",
    "system settings": "System Settings",
    "photos": "Photos",
    "messages": "Messages",
    "mail": "Mail",
    "weather": "Weather",
    "clock": "Clock",
    "facetime": "FaceTime",
    "app store": "App Store",
    "activity monitor": "Activity Monitor",
    "text edit": "TextEdit",
    "textedit": "TextEdit",
    "preview": "Preview",
    "reminders": "Reminders",
}


def open_app(query):
    """Open a website in the browser or a macOS system app by voice command."""
    query = query.replace("open", "").replace("launch", "").replace("start", "").strip()

    # Detect if the user explicitly wants a browser / website
    browser_mode = False
    for kw in ["browser", "website", "site", "on my browser", ".com", ".in", ".org"]:
        if kw in query:
            browser_mode = True
            query = query.replace(kw, "").strip()
            break

    # ── 1. Check if it's a known website ──
    for alias, url in WEBSITE_ALIASES.items():
        if alias in query:
            wednesday_speak(f"Opening {alias.title()} in your browser Jay")
            webbrowser.open(url)
            return

    # ── 2. If browser mode or name looks like a website, open as URL ──
    site_name = query.strip().replace(" ", "")
    if browser_mode or site_name:
        # Check system apps first ONLY if not in browser mode
        if not browser_mode:
            for alias, real_name in APP_ALIASES.items():
                if alias in query:
                    wednesday_speak(f"Opening {real_name} Jay")
                    subprocess.Popen(["open", "-a", real_name])
                    return

        # Open as a website — construct URL from the name
        if site_name:
            url = f"https://www.{site_name}.com"
            wednesday_speak(f"Opening {site_name.title()} in your browser Jay")
            webbrowser.open(url)
            return

    # ── 3. Fall back to system app ──
    app_name = query.strip().title()
    if app_name:
        wednesday_speak(f"Trying to open {app_name} Jay")
        try:
            subprocess.Popen(["open", "-a", app_name])
        except Exception:
            wednesday_speak(f"Sorry Jay, I could not find {app_name}")
    else:
        wednesday_speak("Which app would you like me to open Jay?")
        while True:
            ans = wednesday_listen()
            if ans is None or ans == "":
                continue
            else:
                open_app(ans)
                break


# ── Sing a Song ──────────────────────────────────────────────────────
SONGS = [
    "Twinkle twinkle little star, how I wonder what you are, up above the world so high, like a diamond in the sky",
    "You are my sunshine, my only sunshine, you make me happy when skies are gray",
    "Happy birthday to you, happy birthday to you, happy birthday dear Jay, happy birthday to you",
    "La la la la la, I love to sing for you Jay, la la la la la, hope it makes you smile",
    "Row row row your boat, gently down the stream, merrily merrily merrily merrily, life is but a dream",
    "Old MacDonald had a farm, E I E I O, and on his farm he had a cow, E I E I O",
    "Jingle bells jingle bells jingle all the way, oh what fun it is to ride in a one horse open sleigh",
]


def sing_a_song():
    """Sing a random song."""
    wednesday_speak("Alright Jay, let me sing something for you!")
    song = random.choice(SONGS)
    wednesday_speak(song)
    wednesday_speak("I hope you enjoyed that Jay!")


# ── Tell Time ────────────────────────────────────────────────────────
def tell_time():
    """Announce the current time."""
    now = datetime.datetime.now()
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    period = now.strftime("%p")
    wednesday_speak(f"Jay, the time is {hour}:{minute} {period}")


# ── Tell Date ────────────────────────────────────────────────────────
def tell_date():
    """Announce the current date."""
    now = datetime.datetime.now()
    day = now.strftime("%A")
    date_str = now.strftime("%d %B %Y")
    wednesday_speak(f"Jay, today is {day}, {date_str}")


# ── Tell a Joke ──────────────────────────────────────────────────────
JOKES = [
    ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
    ("Why was the computer cold?", "It left its Windows open!"),
    ("What do you call a computer that sings?", "A Dell!"),
    ("Why did the developer go broke?", "Because he used up all his cache!"),
    ("What is a computer's favourite snack?", "Micro chips!"),
    ("Why do Java developers wear glasses?", "Because they can't C sharp!"),
    ("What did the router say to the doctor?", "It hurts when IP!"),
    ("Why was the JavaScript developer sad?", "Because he didn't Node how to Express himself!"),
]


def tell_joke():
    """Tell a random joke."""
    setup, punchline = random.choice(JOKES)
    wednesday_speak(setup)
    import time
    time.sleep(1)
    wednesday_speak(punchline)


# ── System Report ────────────────────────────────────────────────────
def system_report():
    """Read out basic system information."""
    import platform
    sys_name = platform.system()
    node = platform.node()
    release = platform.release()
    machine = platform.machine()
    wednesday_speak(f"Jay, you are running {sys_name} on a {machine} machine")
    wednesday_speak(f"System name is {node}, release version {release}")


# ── Take a Note ──────────────────────────────────────────────────────
def take_note():
    """Take a voice note and save it to a text file."""
    wednesday_speak("What would you like me to note down Jay?")
    while True:
        note = wednesday_listen()
        if note is None or note == "":
            continue
        else:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("wednesday_notes.txt", "a") as f:
                f.write(f"[{now}] {note}\n")
            wednesday_speak(f"Done Jay, I have noted: {note}")
            break


# ── Flip a Coin ──────────────────────────────────────────────────────
def flip_coin():
    """Flip a coin and announce the result."""
    result = random.choice(["Heads", "Tails"])
    wednesday_speak(f"I flipped a coin and it landed on {result} Jay!")
