# 🖼️ Image to Text OCR using PyTesseract

This project extracts text from images using **Python** and the **PyTesseract** library, which is a wrapper for Google’s Tesseract OCR engine. It reads an image, performs Optical Character Recognition (OCR), and saves the extracted text to a `.txt` file.

---

## 📂 Project Files

* `ocr_extractor.py` – Python script to extract text from an image.
* `Sample_Image.png` – Sample input image (you can replace this with your own image).
* `Sample_Output.txt` – File where the extracted text will be saved.
* `requirements.txt` – List of required Python packages.
* `README.md` – Project documentation.

---

## 🚀 How to Run the Project

### 1. Install Python Packages

```bash
pip install pytesseract pillow
```

### 2. Install Tesseract-OCR

Make sure you have **Tesseract-OCR** installed on your system.

* 📥 [Download Tesseract here](https://github.com/tesseract-ocr/tesseract)

For Windows users:

* Example installation path:
  `C:\Program Files\Tesseract-OCR\tesseract.exe`

Update this path in the Python script if your installation is in a different location:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

### 3. Run the Python Script

```bash
python ocr_extractor.py
```

* The extracted text will be printed in the terminal.
* The extracted text will also be saved in `Sample_Output.txt`.

---

## 🔍 Project Explanation

* Load an image using **Pillow (PIL)**.
* Use **PyTesseract** to perform OCR and extract text from the image.
* Print the extracted text in the terminal.
* Save the extracted text to a `.txt` file.

---

## 📷 Example Output

**Input Image:** `Sample_Image.png`

**Extracted Text Example:**

```text
This is an example of text extracted from the image.
```

---

## ✅ Future Improvements

* Add image preprocessing (like grayscale and thresholding) to improve OCR accuracy.
* Allow user to upload multiple images.
* Build a simple GUI for user-friendly operation.

---

## 🤝 Connect with Me

**Developer:** Akash Kumar
**GitHub:** \[[Your GitHub Profile Link]](https://github.com/aakashhkumar)
**LinkedIn:** \[[Your LinkedIn Profile Link]](https://www.linkedin.com/in/aakashhkumar/)

---

