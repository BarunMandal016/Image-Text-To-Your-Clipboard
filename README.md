# Text Extraction and Clipboard Copier

This Python project captures screenshots from the clipboard, extracts text using OCR (Optical Character Recognition), and copies the extracted text to the clipboard. It also displays a notification to indicate that the text has been copied.

## Features

- Captures screenshots from the clipboard.
- Extracts text from the image using Tesseract OCR.
- Copies the extracted text to the clipboard.
- Displays a sliding notification to confirm the action.

## Requirements

- Python 3.6 or higher
- Tesseract OCR installed on your system ([Download Tesseract](https://github.com/tesseract-ocr/tesseract))
- Required Python libraries:
  - `Pillow`
  - `pytesseract`
  - `pyperclip`
  - `tkinter` (comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code.
2. Install the required Python libraries using pip:
   ```bash
   pip install pillow pytesseract pyperclip