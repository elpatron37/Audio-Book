import tkinter as tk
from tkinter import filedialog
import pyttsx3
import PyPDF2

def convert_pdf_to_audio():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        status_label.config(text="No readable text found in PDF.")
root = tk.Tk()
root.title("PDF to Audiobook")
root.geometry("400x200")

label = tk.Label(root, text="Select a PDF to convert to audio")
label.pack()

convert_button = tk.Button(root, text="Choose PDF", command=convert_pdf_to_audio)
convert_button.pack()

status_label = tk.Label(root)
status_label.pack()

root.mainloop()
