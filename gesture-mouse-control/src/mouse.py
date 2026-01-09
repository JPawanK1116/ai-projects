import speech_recognition as sr
import pyautogui
import time

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source, phrase_time_limit=3)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, didn't catch that.")
        except sr.RequestError:
            print("API unavailable")
    return ""

def move_mouse_by_command(command):
    move_distance = 100  # adjust speed/distance here
    if "top" in command:
        pyautogui.move(0, -move_distance)
    elif "d" in command:
        pyautogui.move(0, move_distance)
    elif "left" in command:
        pyautogui.move(-move_distance, 0)
    elif "right" in command:
        pyautogui.move(move_distance, 0)
    elif "click" in command:
        pyautogui.click()
    elif "double click" in command:
        pyautogui.doubleClick()
    elif "stop" in command:
        print("Stopping voice control.")
        return False
    return True

def main():
    running = True
    while running:
        cmd = listen_command()
        if cmd:
            running = move_mouse_by_command(cmd)
        time.sleep(0.5)

if __name__ == "__main__":
    print("Say 'stop' to end the program.")
    main()
