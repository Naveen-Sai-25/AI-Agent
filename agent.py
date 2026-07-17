import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import pyautogui
import urllib.parse
import datetime
import time
import os
import ctypes
import psutil
# ===============================
# CONFIGURATION
# ===============================

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Fail-safe security switch: Slam mouse cursor into any corner of the screen to abort typing
pyautogui.FAILSAFE = True

engine = pyttsx3.init()
engine.setProperty("rate", 170)

recognizer = sr.Recognizer()

# Dictionary to map AI names to their respective direct query URLs
AI_PLATFORMS = {
    "gemini": "https://gemini.google.com/app?q={}",
    "chatgpt": "https://chatgpt.com/?q={}",
    "claude": "https://claude.ai/new?q={}",
    "perplexity": "https://www.perplexity.ai/?q={}"
}


# ===============================
# SPEAK
# ===============================

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# ===============================
# LISTEN
# ===============================

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You:", command)
        return command

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""


# ===============================
# UTILITY OS FUNCTIONS
# ===============================

def open_chrome():
    subprocess.Popen(CHROME_PATH)

def google_search(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    subprocess.Popen([CHROME_PATH, url])

def youtube_search(query):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
    subprocess.Popen([CHROME_PATH, url])

def lock_laptop():
    ctypes.windll.user32.LockWorkStation()

def shutdown_laptop():
    os.system("shutdown /s /t 0")

def restart_laptop():
    os.system("shutdown /r /t 0")

def cancel_shutdown():
    os.system("shutdown /a")


# ===============================
# SMART MULTI-COMMAND INTERCEPTOR
# ===============================

def process_multiple_commands(full_command):
    if full_command == "":
        return

    # Create a compressed version to easily check for platform name fragments (e.g., "chat gpt" -> "chatgpt")
    clean_command_no_spaces = full_command.replace(" ", "")

    # SMART AI CHECK: If you mentioned an AI platform, DO NOT split the sentence up by "and".
    # This keeps your complete prompt together as one entity.
    is_ai_command = any(ai_name in clean_command_no_spaces for ai_name in AI_PLATFORMS.keys())
    
    if is_ai_command:
        execute(full_command)
        return

    # STANDARD SPLITTING (For non-AI commands like: "open calculator and open notepad")
    normalized = full_command.replace("and then", "split_here")
    normalized = normalized.replace(" and ", " split_here ")
    normalized = normalized.replace(" then ", " split_here ")

    commands_list = normalized.split("split_here")

    # Cycle through each command consecutively
    for sub_command in commands_list:
        sub_command = sub_command.strip()
        if sub_command:
            execute(sub_command)


# ===============================
# COMMAND EXECUTION ENGINE
# ===============================

def execute(command):
    if command == "":
        return

    # Strict Exit Check (Prevents false triggers from words like "perplexity")
    if command.strip() == "exit" or command.strip() == "stop":
        speak("Goodbye")
        exit()

    # --- DYNAMIC MULTI-AI ROUTER ---
    clean_command_no_spaces = command.replace(" ", "")

    for ai_name, url_template in AI_PLATFORMS.items():
        if ai_name in clean_command_no_spaces:
            if "search" in command or "ask" in command:
                # Clean up structure words to isolate your prompt accurately
                query = command.replace("search", "").replace("ask", "").replace(ai_name, "").replace("ai", "").replace("for", "").strip()
                
                # Double-check cleanup for fragmented parts of the name (like a leftover "gpt" from "chat gpt")
                query = query.replace("gpt", "").strip()
                
                speak(f"Searching {ai_name.capitalize()} for your query.")
                
                # Format encoded browser URLs
                formatted_url = url_template.format(query.replace(" ", "%20"))
                subprocess.Popen([CHROME_PATH, formatted_url])
                return 
            
            else:
                speak(f"Opening {ai_name.capitalize()}")
                base_url = url_template.split('?')[0]
                subprocess.Popen([CHROME_PATH, base_url])
                return

    # Open Chrome (Standard browser window)
    if "open chrome" in command:
        speak("Opening Chrome")
        open_chrome()

    # Standard Google Search
    elif "search" in command and "youtube" not in command:
        query = command.replace("search", "").replace("google", "").strip()
        speak(f"Searching Google for {query}")
        google_search(query)

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        subprocess.Popen([CHROME_PATH, "https://youtube.com"])

    # Search YouTube
    elif "youtube" in command and "search" in command:
        query = command.replace("search", "").replace("youtube", "").strip()
        speak(f"Searching YouTube for {query}")
        youtube_search(query)
    
    # Smart Notepad & Live Dictation Control with Target Deletion
    elif "type" in command or "open notepad" in command:
        text_to_type = command.partition("type")[2].strip()

        speak("Opening Notepad. Live dictation active.")
        subprocess.Popen("notepad.exe")
        time.sleep(1.5)

        if text_to_type:
            pyautogui.write(text_to_type + " ", interval=0.03)

        while True:
            print("Listening for dictation...")
            live_speech = listen().lower().strip() 

            if "stop writing" in live_speech or "stop typing" in live_speech:
                speak("Stopping dictation mode.")
                break

            elif live_speech.startswith("delete "):
                target_word = live_speech.replace("delete ", "").strip()
                if target_word:
                    speak(f"Deleting {target_word}")
                    pyautogui.hotkey('ctrl', 'f')
                    time.sleep(0.2)
                    pyautogui.write(target_word)
                    pyautogui.press('enter')
                    time.sleep(0.2)
                    pyautogui.press('escape')
                    time.sleep(0.1)
                    pyautogui.press('backspace')
                continue

            if live_speech == "":
                continue

            pyautogui.write(live_speech + " ", interval=0.03) 
            
    # Open Calculator
    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")

    # Screenshot
    elif "take screenshot" in command:
        filename = "screenshot.png"
        pyautogui.screenshot(filename)
        speak("Screenshot saved.")

    # Tell Time
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # Lock Laptop
    elif "lock laptop" in command or "lock my laptop" in command or "lock computer" in command:
        speak("Locking your laptop.")
        lock_laptop()

    # Open Whatsapp Web
    elif "open whatsapp web" in command:
        speak("Opening WhatsApp Web")
        subprocess.Popen([CHROME_PATH, "https://web.whatsapp.com"])

    # Open VS Code
    elif "open vs code" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")
    
    # Open File Explorer
    elif "open file explorer" in command or "open files" in command:
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")

    elif "volume up" in command or "increase volume" in command:
        speak("Raising volume")
        for _ in range(5): # Press 5 times to bump volume up by 10%
            pyautogui.press("volumeup")

    elif "volume down" in command or "decrease volume" in command:
        speak("Lowering volume")
        for _ in range(5):
            pyautogui.press("volumedown")

    elif "mute" in command or "unmute" in command:
        speak("Toggling mute")
        pyautogui.press("volumemute")

    # --- BATTERY STATUS ---
    elif "battery" in command or "power status" in command:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = "plugged in" if battery.power_plugged else "running on battery"
            speak(f"Your battery is at {percent} percent and is currently {plugged}.")
        else:
            speak("I couldn't read the battery status.")

    # Make sure to run: pip install pyperclip

# --- VOICE TO CLIPBOARD ---
    elif "copy to clipboard" in command or "remember text" in command:
        text_to_copy = command.replace("copy to clipboard", "").replace("remember text", "").strip()
        if text_to_copy:
            pyperclip.copy(text_to_copy)
            speak("Text copied to clipboard. You can now paste it anywhere.")
        else:
            speak("What text would you like me to copy?")

    # --- ACTIVE WINDOW CONTROL ---
    elif "close this window" in command or "close current application" in command:
        speak("Closing the active window.")
        pyautogui.hotkey('alt', 'f4')

    # --- DYNAMIC APP LAUNCHER (CATCH-ALL) ---
    elif command.startswith("open "):
        app_name = command.replace("open ", "").strip()
        
        # Block items already handled by explicit browser routers
        if app_name not in ["chrome", "youtube", "whatsapp web"]:
            try:
                speak(f"Attempting to launch {app_name}")
                # Dynamic launch via Windows Run dialog string
                subprocess.Popen(f"{app_name}.exe", shell=True)
            except Exception:
                speak(f"I couldn't find an application named {app_name}.")
                
    # Unknown Command Fallback
    else:
        speak("Sorry, I don't know that command yet.")


# ===============================
# MAIN RUNTIME LOOP
# ===============================

if __name__ == "__main__":
    speak("Hello Naveen, How Can I Help You ?")

    while True:
        command = listen()
        
        # Route voice data through the smart multi-command processor
        process_multiple_commands(command)