import tkinter as tk
from tkinter import filedialog, ttk
import pyttsx3
import docx
import threading
from googletrans import Translator
import time

engine = pyttsx3.init()
translator = Translator()
speaking = False
paused = False
stop_signal = False

def read_file(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    return ""

def on_open():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Word files", "*.docx")])
    if file_path:
        content = read_file(file_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, content)

def highlight_sentence(sentence):
    text = text_box.get("1.0", tk.END)
    start = text.find(sentence)
    if start != -1:
        end = start + len(sentence)
        text_box.tag_remove("highlight", "1.0", tk.END)
        text_box.tag_add("highlight", f"1.0+{start}c", f"1.0+{end}c")
        text_box.tag_config("highlight", background="yellow")

def on_speak():
    global speaking, paused, stop_signal
    speaking = True
    paused = False
    stop_signal = False

    text = text_box.get("1.0", tk.END).strip()
    lang_code = lang_map[language_var.get()]

    try:
        if lang_code != 'en':
            translation = translator.translate(text, dest=lang_code)
            text = translation.text
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
    except Exception as e:
        print(f"Translation error: {e}")
        return

    sentences = [s.strip() + '.' for s in text.replace("\n", " ").split('.') if s.strip()]
    selected_voice = voice_combo.current()
    engine.setProperty('voice', voices[selected_voice].id)
    engine.setProperty('rate', int(speed_scale.get()))

    def speak_loop():
        for sentence in sentences:
            if stop_signal:
                break

            while paused:
                time.sleep(0.1)
                if stop_signal:
                    break

            highlight_sentence(sentence)
            engine.say(sentence)
            engine.runAndWait()

        text_box.tag_remove("highlight", "1.0", tk.END)

    threading.Thread(target=speak_loop).start()

def on_pause():
    global paused
    if speaking:
        paused = True

def on_resume():
    global paused
    if speaking and paused:
        paused = False

def on_stop():
    global stop_signal, speaking, paused
    stop_signal = True
    paused = False
    speaking = False
    engine.stop()
    text_box.tag_remove("highlight", "1.0", tk.END)

# Voices and GUI mappings
voices = engine.getProperty('voices')
lang_map = {
    'English': 'en',
    'Hindi': 'hi',
    'Telugu': 'te',
    'Tamil': 'ta',
    'Kannada': 'kn',
    'Bengali': 'bn',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Punjabi': 'pa',
}

# GUI Setup
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("700x600")

tk.Button(root, text="Open File", command=on_open).pack(pady=5)

text_box = tk.Text(root, wrap=tk.WORD, height=20, font=("Arial", 12))
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

voice_combo = ttk.Combobox(root, values=[v.name for v in voices])
voice_combo.current(0)
voice_combo.pack(pady=5)

speed_scale = tk.Scale(root, from_=100, to=250, label="Speed", orient=tk.HORIZONTAL)
speed_scale.set(150)
speed_scale.pack(pady=5)

language_var = tk.StringVar(value='English')
language_menu = ttk.Combobox(root, textvariable=language_var, values=list(lang_map.keys()))
language_menu.pack(pady=5)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Speak", command=on_speak, bg="green", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(control_frame, text="Pause", command=on_pause, bg="orange", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(control_frame, text="Resume", command=on_resume, bg="blue", fg="white", width=10).grid(row=0, column=2, padx=5)
tk.Button(control_frame, text="Stop", command=on_stop, bg="red", fg="white", width=10).grid(row=0, column=3, padx=5)

root.mainloop()
