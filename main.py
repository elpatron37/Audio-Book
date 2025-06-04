import tkinter as tk
from tkinter import filedialog
import pyttsx3
import PyPDF2

def convert_pdf_to_audio():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not filepath:
        return

    try:
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

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# GUI
root = tk.Tk()
root.title("PDF to Audiobook")
root.geometry("400x200")

label = tk.Label(root, text="Select a PDF to convert to audio", font=("Arial", 14))
label.pack(pady=20)

convert_button = tk.Button(root, text="Choose PDF", command=convert_pdf_to_audio, font=("Arial", 12))
convert_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="red")
status_label.pack(pady=10)

root.mainloop()
