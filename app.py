import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from datetime import datetime


def recognize_speech():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            root.update()

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)

            status_label.config(text="Recognizing...")
            root.update()

        text = recognizer.recognize_google(audio)

        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

        status_label.config(text="Speech recognized successfully.")

    except sr.UnknownValueError:
        status_label.config(text="Could not understand the speech.")
        messagebox.showwarning(
            "Recognition Error",
            "Sorry, I could not understand the speech."
        )

    except sr.RequestError:
        status_label.config(text="Speech service unavailable.")
        messagebox.showerror(
            "Connection Error",
            "Could not connect to the speech recognition service."
        )

    except Exception as e:
        status_label.config(text="An error occurred.")
        messagebox.showerror("Error", str(e))


def save_text():
    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning(
            "Empty Text",
            "There is no recognized text to save."
        )
        return

    filename = "output/recognized_text.txt"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(
            f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n"
        )
        file.write(text + "\n")

    messagebox.showinfo(
        "Saved",
        "Recognized text has been saved successfully."
    )


def clear_text():
    text_box.delete("1.0", tk.END)
    status_label.config(text="Ready")


root = tk.Tk()
root.title("ASR Tool - Automatic Speech Recognition")
root.geometry("700x500")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Automatic Speech Recognition Tool",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    root,
    text="Convert your speech into text",
    font=("Arial", 12)
)
subtitle_label.pack()

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 11)
)
status_label.pack(pady=15)

text_box = tk.Text(
    root,
    height=12,
    width=75,
    font=("Arial", 13),
    wrap=tk.WORD
)
text_box.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

record_button = tk.Button(
    button_frame,
    text="🎤 Start Recording",
    font=("Arial", 12, "bold"),
    command=recognize_speech,
    width=18
)
record_button.grid(row=0, column=0, padx=10)

save_button = tk.Button(
    button_frame,
    text="Save Text",
    font=("Arial", 12, "bold"),
    command=save_text,
    width=15
)
save_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    command=clear_text,
    width=15
)
clear_button.grid(row=0, column=2, padx=10)

footer = tk.Label(
    root,
    text="ASR Project | Python",
    font=("Arial", 10)
)
footer.pack(side=tk.BOTTOM, pady=15)

root.mainloop()
