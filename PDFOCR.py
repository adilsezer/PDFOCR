import os
import pytesseract
import PIL
import fitz
from tkinter import filedialog
from tkinter import *


def extractText(dirpath):
    pdfs = [p for p in os.listdir(dirpath) if p.endswith(".pdf")]
    mat = fitz.Matrix(2.0, 2.0)
    pdfOCR = ""

    for pdf in pdfs:
        pdfName = os.path.splitext(pdf)[0]
        with fitz.open(dirpath + "/" + pdf) as doc:
            for page in doc:
                pix = page.getPixmap(matrix=mat)
                pix.writePNG(f"{dirpath}/{pdfName}(page {page.number}).png")
                pdfOCR += pytesseract.image_to_string(
                    PIL.Image.open(f"{dirpath}/{pdfName}(page {page.number}).png")
                )
                os.remove(f"{dirpath}/{pdfName}(page {page.number}).png")

    writeTxt(f"{dirpath}/OCR.txt", pdfOCR)


def writeTxt(filename, OCRText):
    OCRText = "".join([s for s in OCRText.splitlines(True) if s.strip()])
    with open(filename, "w", encoding="utf8") as txtfile:
        txtfile.write(OCRText)


pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"
root = Tk()
root.withdraw()
dirpath = filedialog.askdirectory()
extractText(dirpath)
print("Done")
