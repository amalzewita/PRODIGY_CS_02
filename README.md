# Image Encryption and Decryption Tool

This project provides a Python implementation of an image encryption and decryption tool using pixel manipulation techniques. The tool applies XOR operations with a generated mask to secure image data, ensuring confidentiality.

## Features

- **Encrypt an image** using XOR operations with a generated mask.
- **Decrypt an image** using the same key and mask.
- Handles **RGB images**.
- **Mask handling**: Saves and loads masks to ensure accurate decryption.

## How It Works

The encryption process involves applying an XOR operation between the image pixels and a randomly generated mask, then adjusting pixel values for added complexity. The decryption reverses the process using the same key and mask. Masks are saved with encrypted images to allow accurate decryption.

### Example

1. **Encryption**:
    - **Original Image**: `photo.jpg`
    - **Key**: `123`
    - **Encrypted Image**: `encrypted_photo.jpg`

2. **Decryption**:
    - **Encrypted Image**: `encrypted_photo.jpg`
    - **Decrypted Image**: `decrypted_photo.jpg` (should match the original image)

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages: Pillow, NumPy.

You can install the required packages using pip:

```bash
pip install pillow numpy
