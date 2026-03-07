import sys
import os
from datetime import datetime
from PIL import Image

DELIMITER = "#####END#####"

def create_output_folder():
    date = datetime.now().strftime("%Y-%m-%d")
    folder = os.path.join("outputs", date)
    os.makedirs(folder, exist_ok=True)
    return folder


def embed(image_path, secret_file):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = bytearray(img.tobytes())

    with open(secret_file, "rb") as f:
        secret = f.read()

    payload = secret + DELIMITER.encode()

    bits = ''.join(format(byte, '08b') for byte in payload)

    if len(bits) > len(pixels):
        print("[-] Error: Secret file too large.")
        return

    for i, bit in enumerate(bits):
        pixels[i] = (pixels[i] & ~1) | int(bit)

    new_img = Image.frombytes(img.mode, img.size, bytes(pixels))

    folder = create_output_folder()
    output_path = os.path.join(folder, "stego_" + os.path.basename(image_path))

    new_img.save(output_path)

    print(f"[+] Data embedded successfully")
    print(f"[+] Saved to: {output_path}")


def extract(stego_image, output_file):

    img = Image.open(stego_image)
    pixels = bytearray(img.tobytes())

    bits = [str(pixel & 1) for pixel in pixels]

    chars = []

    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        char = chr(int(''.join(byte), 2))
        chars.append(char)

        if ''.join(chars).endswith(DELIMITER):
            break

    hidden_data = ''.join(chars).replace(DELIMITER, "")

    with open(output_file, "wb") as f:
        f.write(hidden_data.encode())

    print(f"[+] Secret extracted to: {output_file}")


def usage():
    print("""
CTK-STEGO Advanced

Embed:
  python3 ctk-stego.py embed <image> <secret_file>

Extract:
  python3 ctk-stego.py extract <stego_image> <output_file>
""")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        sys.exit()

    mode = sys.argv[1]

    if mode == "embed" and len(sys.argv) == 4:
        embed(sys.argv[2], sys.argv[3])

    elif mode == "extract" and len(sys.argv) == 4:
        extract(sys.argv[2], sys.argv[3])

    else:
        usage()
