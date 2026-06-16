import pyttsx3
import subprocess
from PyPDF2 import PdfReader
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
root.withdraw()

book = askopenfilename(
    title="Choose a PDF",
    filetypes=[("PDF files", "*.pdf")]
)

if not book:
    print("No PDF selected.")
    quit()

# Opens the PDF in Preview so you can look at it while it reads
subprocess.Popen(["open", book])

pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

player = pyttsx3.init()

for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()

    if text:
        player.say(text)
        player.runAndWait()
    else:
        print(f"Page {num + 1} has no readable text.")