#!/usr/bin/env python3

import sys
import os
from PIL import Image
from colorama import Fore, init

init(autoreset=True)

END_MARK = "CTK_END_MARK"


def show_banner():
    print(Fore.CYAN + """

   ██████╗████████╗██╗  ██╗
  ██╔════╝╚══██╔══╝██║ ██╔╝
  ██║        ██║   █████╔╝
  ██║        ██║   ██╔═██╗
  ╚██████╗   ██║   ██║  ██╗
   ╚═════╝   ╚═╝   ╚═╝  ╚═╝

      CTK-STEGO
      by @cyber_specterz

""")


def make_output_folder():
    folder = "outputs"

    if not os.path.exists(folder):
        os.mkdir(folder)

    return folder


def check_capacity(img, data_len):

    space = len(img.tobytes())

    if data_len > space:
        print(Fore.RED + "[-] file too big for this image")
        sys.exit(1)


def embed(img_path, secret_path, inplace=False):

    if not os.path.isfile(img_path):
        print("image not found")
        return

    if not os.path.isfile(secret_path):
        print("secret file not found")
        return

    print(Fore.YELLOW + "[*] opening image")

    img = Image.open(img_path)
    img = img.convert("RGB")

    pixels = bytearray(img.tobytes())

    print(Fore.YELLOW + "[*] loading secret")

    with open(secret_path, "rb") as f:
        secret = f.read()

    data = secret + END_MARK.encode()

    bits = ""

    for b in data:
        bits += format(b, "08b")

    check_capacity(img, len(bits))

    print(Fore.YELLOW + "[*] hiding data")

    for i in range(len(bits)):
        pixels[i] = (pixels[i] & ~1) | int(bits[i])

    result = Image.frombytes(img.mode, img.size, bytes(pixels))

    if inplace:

        result.save(img_path)

        print(Fore.GREEN + "[+] done. data hidden in original image")

    else:

        out = make_output_folder()
        name = "stego_" + os.path.basename(img_path)

        save_path = os.path.join(out, name)

        result.save(save_path)

        print(Fore.GREEN + "[+] saved:", save_path)


def extract(img_path, output_file):

    if not os.path.isfile(img_path):
        print("image not found")
        return

    print(Fore.YELLOW + "[*] reading image")

    img = Image.open(img_path)
    pixels = bytearray(img.tobytes())

    bits = []

    for p in pixels:
        bits.append(str(p & 1))

    text = ""

    for i in range(0, len(bits), 8):

        byte = bits[i:i+8]

        if len(byte) < 8:
            break

        char = chr(int("".join(byte), 2))

        text += char

        if text.endswith(END_MARK):
            break

    text = text.replace(END_MARK, "")

    with open(output_file, "wb") as f:
        f.write(text.encode())

    print(Fore.GREEN + "[+] extracted to", output_file)


def help_menu():

    print("""
usage:

embed:
  python3 ctk-stego.py embed image.png secret.txt

embed in-place:
  python3 ctk-stego.py embed image.png secret.txt --inplace

extract:
  python3 ctk-stego.py extract image.png output.txt
""")


def main():

    show_banner()

    if len(sys.argv) < 2:
        help_menu()
        return

    cmd = sys.argv[1]

    if cmd == "embed":

        if len(sys.argv) < 4:
            help_menu()
            return

        image = sys.argv[2]
        secret = sys.argv[3]

        inplace = "--inplace" in sys.argv

        embed(image, secret, inplace)

    elif cmd == "extract":

        if len(sys.argv) != 4:
            help_menu()
            return

        extract(sys.argv[2], sys.argv[3])

    else:
        help_menu()


if __name__ == "__main__":
    main()
