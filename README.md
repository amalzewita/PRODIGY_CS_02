# Image Encryption and Decryption Tool

This Python project provides a basic image encryption and decryption tool using pixel manipulation techniques. It applies XOR operations with a generated mask to secure image data and ensure confidentiality.

## Features

- **Encryption**: Encrypts an image using XOR operations with a mask generated based on an encryption key.
- **Decryption**: Decrypts an encrypted image using the same key and mask.
- **Mask Handling**: Saves and loads masks to ensure accurate decryption.

## Requirements

- Python 3.x
- Pillow (`PIL` package)
- NumPy

You can install the required packages using pip:

```bash
pip install pillow numpy
