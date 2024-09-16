from PIL import Image
import numpy as np
import os

class MathEncryptor:
    def __init__(self, image_path, key):
        """
        Initialize the MathEncryptor with the image path and key.
        :param image_path: Path to the input image.
        :param key: Encryption key used for operations.
        """
        self.image_path = image_path
        self.key = key
        self.image = Image.open(image_path).convert('RGB')  # Ensure RGB mode
        self.image_array = np.array(self.image, dtype=np.uint8)

    def generate_mask(self, array_shape):
        """
        Generate a mask based on a pseudo-random number generator and the key.
        :param array_shape: Shape of the image array.
        :return: Mask array.
        """
        np.random.seed(self.key)
        mask = np.random.randint(0, 256, size=array_shape, dtype=np.uint8)
        return mask

    def apply_math_operation(self, array, mask, operation):
        """
        Apply a mathematical operation to each pixel using a mask.
        :param array: The image array to process.
        :param mask: Mask to apply.
        :param operation: The operation to apply ('encrypt' or 'decrypt').
        :return: Processed image array.
        """
        if operation == 'encrypt':
            processed_array = np.bitwise_xor(array, mask)
        elif operation == 'decrypt':
            processed_array = np.bitwise_xor(array, mask)
        else:
            raise ValueError("Invalid operation. Choose 'encrypt' or 'decrypt'.")
        
        # Ensure pixel values stay within valid range
        processed_array = np.clip(processed_array, 0, 255)
        return processed_array

    def encrypt_and_save(self, output_path):
        """
        Encrypt the image and save the result to the specified path.
        :param output_path: Path to save the encrypted image.
        """
        mask = self.generate_mask(self.image_array.shape)
        encrypted_array = self.apply_math_operation(self.image_array, mask, 'encrypt')
        encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
        encrypted_img.save(output_path)

        # Save the mask to a file for later use
        np.save(output_path + '_mask.npy', mask)

    def decrypt_and_save(self, encrypted_image_path, output_path):
        """
        Decrypt an image and save the result to the specified path.
        :param encrypted_image_path: Path to the encrypted image.
        :param output_path: Path to save the decrypted image.
        """
        # Load the encrypted image
        encrypted_image = Image.open(encrypted_image_path).convert('RGB')
        encrypted_image_array = np.array(encrypted_image, dtype=np.uint8)

        # Load the mask from the file
        mask_path = encrypted_image_path + '_mask.npy'
        if os.path.exists(mask_path):
            mask = np.load(mask_path)
        else:
            raise FileNotFoundError("Mask file not found. Decryption cannot proceed.")

        decrypted_array = self.apply_math_operation(encrypted_image_array, mask, 'decrypt')
        decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
        decrypted_img.save(output_path)

# Main program execution starts here
if __name__ == "__main__":
    key = 123  # Encryption key for operations

    # Create an instance of MathEncryptor
    encryptor = MathEncryptor('C:/photo.jpg', key)
    
    # Encrypt the photo and save it
    encryptor.encrypt_and_save('C:/encrypted_photo.jpg')
    
    # Decrypt the photo and save it
    encryptor.decrypt_and_save('C:/encrypted_photo.jpg', 'C:/decrypted_photo.jpg')
