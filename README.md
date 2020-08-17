# PDFOCR
An OCR project to read all PDF files in a folder with Tesseract library and write text into a txt file

## Requirements
* Pillow 7.2.0
* PyMuPDF 1.17.5
* PyPDF2 1.26.0
* pytesseract 0.3.5

## External Dependencies:
Tesseract-OCR: https://github.com/tesseract-ocr/tesseract/wiki

## Running from source
    $ git clone https://github.com/sezerad/PDFOCR.git
    $ cd PDFOCR
    $ pip install -r requirements.txt
    $ python PDFOCR.py

## Screenshots
### Example PDF Document
![Alt text](https://github.com/sezerad/PDFOCR/blob/master/screenshots/ExamplePDF.png?raw=true "PDF OCR")
### Extracted Text
![Alt text](https://github.com/sezerad/PDFOCR/blob/master/screenshots/ExampleResult.png?raw=true "PDF OCR")
