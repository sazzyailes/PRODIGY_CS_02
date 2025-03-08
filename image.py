from PIL import Image
import numpy as np
import argparse

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image_array = np.array(image)
    
    np.random.seed(key)  # Set seed for reproducibility
    random_mask = np.random.randint(0, 256, image_array.shape, dtype=np.uint8)
    
    encrypted_array = np.bitwise_xor(image_array, random_mask)
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)  # XOR again to decrypt
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (integer)")
    
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.key)
    elif args.mode == "decrypt":
        decrypt_image(args.input, args.output, args.key)
