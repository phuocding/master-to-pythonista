import base64
import os.path


def checkFile(title, file_name, hint_or_show):
    if os.path.isfile(file_name):
        # print("File exist")

        f = open(file_name, "a")
        f.write(title + ": " + hint_or_show + "\n")
        f.close()

        print("Saved")
    else:
        print("File not exist")
        print("Creating a file...")

        f = open(file_name, "x")
        f = open(file_name, "a")
        f.write(title + ": " + hint_or_show + "\n")
        f.close()

        print("Saved")


def encode(title, key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        # print(type(key_c))

        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)

        enc.append(enc_c)
        # print(type(enc_c))

    # join list and encode
    j_enc = "".join(enc).encode()
    hint = base64.urlsafe_b64encode(j_enc).decode()

    checkFile(title, "decode.txt", hint)


def decode(title, key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)

        dec.append(dec_c)

    show = "".join(dec)

    checkFile(title, "encode.txt", show)


def main():
    print("Hello Phuoc!")

    while True:
        option = input(
            "Please choose MODE (e for encrypt, d for decrypt, exit for exit): "
        )

        if option == "e":
            _title = input("enter the title: ")
            _key = input("typing key (remember that if you want to encode): ")
            _clear = input("typing message: ")
            encode(_title, _key, _clear)
            continue
        elif option == "d":
            _title = input("enter the title: ")
            _key = input(
                "typing key (if you didn't remember, message show incorrectly): "
            )
            _enc = input("typing message hint: ")
            decode(_title, _key, _enc)
            continue
        elif option == "exit":
            print("See you soon!!!")
            break
        else:
            print("please choose again")
            continue


if __name__ == "__main__":
    main()