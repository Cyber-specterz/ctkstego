# CTK-STEGO 🔐

**Basic Steganography Tool (No Password)**
Created by **@cyber_specterz**

---

## 📌 Overview

**CTK-STEGO** is a simple and fast command-line steganography tool that allows you to hide secret files inside images and extract them later.

This tool uses **LSB (Least Significant Bit) steganography** to embed data inside image pixels without visibly altering the image.

It is designed for **educational purposes, cybersecurity learning, and demonstrations**.

---

## ⚡ Features

* Hide any file inside an image
* Extract hidden files from stego images
* Fast processing using byte-level operations
* Automatic output folder creation
* Output files organized by **date**
* Simple command line interface
* Lightweight and easy to use

---

## 📂 Project Structure

```
CTK-STEGO/
│
├── ctk-stego.py
├── README.md
└── outputs/
    └── YYYY-MM-DD/
        └── stego_image.png
```

When embedding data, the output image will automatically be saved inside a dated folder.

Example:

```
outputs/2026-03-07/stego_image.png
```

---

## 🛠 Requirements

Python 3.x

Install required library:

```
pip install pillow
```

---

## 🚀 Usage

### 1️⃣ Embed Secret File Into Image

```
python3 ctk-stego.py embed <image> <secret_file>
```

Example:

```
python3 ctk-stego.py embed image.png secret.txt
```

Output will automatically be saved in:

```
outputs/YYYY-MM-DD/stego_image.png
```

---

### 2️⃣ Extract Hidden File

```
python3 ctk-stego.py extract <stego_image> <output_file>
```

Example:

```
python3 ctk-stego.py extract outputs/2026-03-07/stego_image.png extracted.txt
```

---

## 🧠 How It Works

CTK-STEGO uses **Least Significant Bit (LSB) steganography**.

Each pixel in an image contains color values (RGB). The tool modifies the **least significant bit** of these values to store hidden data.

Because only the smallest bit is modified, the visual appearance of the image remains almost identical.

Process:

1. Convert secret file into binary data
2. Modify pixel LSB values
3. Save the modified image
4. Extract binary data later using the delimiter

---

## 📖 Example Workflow

Step 1 – Prepare files

```
image.png
secret.txt
```

Step 2 – Embed secret

```
python3 ctk-stego.py embed image.png secret.txt
```

Step 3 – Share the generated stego image

```
outputs/2026-03-07/stego_image.png
```

Step 4 – Extract hidden data

```
python3 ctk-stego.py extract stego_image.png extracted.txt
```

---

## ⚠ Disclaimer

This tool is created for:

* Cybersecurity education
* Learning steganography
* Ethical hacking demonstrations
* Research purposes

Do **not** use this tool for illegal activities.

---

## 🧑‍💻 Author

**@cyber_specterz**

Cybersecurity Researcher
Creator of **CTK Tools**

---

## ⭐ Future Improvements

Planned upgrades for future versions:

* Password protected steganography
* AES encryption
* Faster embedding using NumPy
* Multi-file embedding
* GUI interface
* Detection resistance improvements
* File size capacity checker

---

**CTK-STEGO – Learn Steganography Practically 🔐**
